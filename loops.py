import json
with open('./resources/data/config.json', 'r') as file:
    hardware_data = json.load(file)

CAMERAS = list(hardware_data["Camera"].values())

IMAGE_PROCESSORS = [
    hardware_data["Platform"]["ImageProcessing1"],
    hardware_data["Platform"]["ImageProcessing2"]
    ]

FEEDBACKS = [
    hardware_data["Platform"]["GUIFeedback1"],
    hardware_data["Platform"]["GUIFeedback2"]
]

TAPO_CAM_AUTH = {
    "User" : "TapoCam",
    "Password" : "salut123"
}

WEBCOMMANDS = hardware_data["Platform"]["GUIWebCommands"]

from PySide6.QtCore import QTimer, Signal, Slot, Qt, QThread
from PySide6.QtGui import QPixmap, QPainter, QImage

import DataTransmition
import cv2
import numpy as np
import os
import time
import pytapo
import queue

class UpdateCamera(QThread):
    changePixmap = Signal(QImage, int)
    
    def __init__(self):
        super().__init__()
        self.AI_data = [None, None]
        self.IR = [
            DataTransmition.ImageReceiver(IMAGE_PROCESSORS[0]["IP"], IMAGE_PROCESSORS[0]["PORT"]),
            DataTransmition.ImageReceiver(IMAGE_PROCESSORS[1]["IP"], IMAGE_PROCESSORS[1]["PORT"])
        ]
        self.frame = [None, None]
        self.used_cams = 2
        
    def run(self):
        ok = True
        while ok:
            if ok:                
                for i in range(self.used_cams):
                    _, self.frame[i] = self.IR[i].receive()
                    self.frame[i] = cv2.cvtColor(self.frame[i], cv2.COLOR_BGR2RGBA)

                    if self.AI_data[i] is not None:
                        recv_time = float(self.AI_data[i]["sent-time"][1:])
                        try:
                            for G, score, face in zip(self.AI_data[i]["G"], self.AI_data[i]["scores"], self.AI_data[i]["faces"]):
                                f = [float(coord) for coord in face.split(',')]
                                g = [float(coord) for coord in G.split(',')]
                                self.frame[i] = cv2.rectangle(
                                    self.frame[i], 
                                    (int(f[1] * self.frame[i].shape[1]), int(f[0] * self.frame[i].shape[0])), 
                                    (int(f[3] * self.frame[i].shape[1]), int(f[2] * self.frame[i].shape[0])), 
                                    (255, 0, 0, 255), 2)
                                self.frame[i] = cv2.putText(
                                    self.frame[i], 
                                    "Score: " + score, 
                                    (int(f[1] * self.frame[i].shape[1]), int(f[0] * self.frame[i].shape[0]) - 5),
                                    1, 1, (255, 0, 0, 255), 2)
                                self.frame[i] = cv2.putText(
                                    self.frame[i], 
                                    str(round(time.time() - recv_time, 1)) + " secs ago", 
                                    (int(f[1] * self.frame[i].shape[1]), int(f[0] * self.frame[i].shape[0]) - 17),
                                    1, 1, (255, 0, 0, 255), 2)
                                self.frame[i] = cv2.rectangle(
                                    self.frame[i], 
                                    (int(g[1] * self.frame[i].shape[1]) - 7, int(g[0] * self.frame[i].shape[0]) - 7), 
                                    (int(g[1] * self.frame[i].shape[1]) + 7, int(g[0] * self.frame[i].shape[0]) + 7), 
                                    (255, 0, 0, 255), 6)
                        except:
                            print("No face found!", "CAM", i)
                            
                        self.AI_data[i] = None

                    h, w, ch = self.frame[i].shape
                    bytesPerLine = ch * w
                    qt_frame = QImage(self.frame[i].data, w, h, bytesPerLine, QImage.Format_RGBA8888)
                    self.changePixmap.emit(qt_frame, i)

    def set_AI_results(self, json_like, index):
        self.AI_data[index] = json_like

    def send_frame_to_save_user(self, username):
        self.IS[0].send(self.frame[0], "add,{},##".format(username))

    def send_frame_to_remove_user(self, username):
        self.IS[0].send(self.frame[0], "remove,{},##".format(username))

class MoveCamera(QThread):
    def __init__(self):
        super().__init__()
        self.controller = []
        self.commands_queue = queue.Queue()

    @Slot(int, str)
    def move(self, cam_id, direction):
        self.commands_queue.put((cam_id, direction))

    def run(self):

        not_ok = True
        while not_ok:
            try:
                for cam in CAMERAS:
                    self.controller.append(
                        pytapo.Tapo(cam["IP"], TAPO_CAM_AUTH["User"], TAPO_CAM_AUTH["Password"])
                    )
                print("Cams controlls seted up")
                not_ok = False
            except Exception as e:
                not_ok = True
                print("Camera setup error:", e)
                
        while True:
            if self.commands_queue.empty():
                time.sleep(0.01)
            else:
                id, direction = self.commands_queue.get()
                x = 0
                y = 0
                if(direction == "UP"):
                    y = 10
                if(direction == "DOWN"):
                    y = -10
                if(direction == "RIGHT"):
                    x = 10
                if(direction == "LEFT"):
                    x = -10
                try:
                    self.controller[id].moveMotor(x, y)
                except Exception as e:
                    print("Camera move error:", e)

class GetWebCommands(QThread):
    send_camera_move = Signal(int, str)
    def __init__(self):
        super().__init__()
        self.RES = DataTransmition.UDPReceiver(WEBCOMMANDS["IP"], WEBCOMMANDS["PORT"])

    def run(self):
        while True:
            time.sleep(0.05)
            msg = self.RES.receive()

            try:
                msg = str(msg)

                option, arg1, arg2 = msg.split(':')
                if option == "CAMERA":
                    for i, cam in enumerate(CAMERAS): 
                        if cam["Location"] == arg1: 
                            cam_id = i

                    self.send_camera_move.emit(cam_id, arg2) 

            except Exception as e:
                print(e)


class GetAIResults(QThread):
    send_json = Signal(dict, int)
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.RES = DataTransmition.UDPReceiver(FEEDBACKS[index]["IP"], FEEDBACKS[index]["PORT"])

    def run(self):
        while True:
            time.sleep(0.05)
            msg = self.RES.receive()
            try:
                json_like = json.loads(msg)
                self.send_json.emit(json_like, self.index)
            except Exception as e:
                print(e)
