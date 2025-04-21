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

from PySide6.QtCore import QTimer, Signal, Slot, Qt, QThread
from PySide6.QtGui import QPixmap, QPainter, QImage

import DataTransmition as DataTransmition
import cv2
import numpy as np
import os
import time
import pytapo
import queue

ON_BOARD = False
ON_COMPUTER = True

if not ON_BOARD:
    class DummyCam():
        def __init__(self):
            self.frame = np.random.rand(1440, 1280, 3) * 255
            self.frame = np.array(self.frame, dtype=np.uint8)

        def read(self):
            return True, self.frame
        
        def release(self):
            pass

if ON_COMPUTER:
    class NonGstCam():
        def __init__(self):
            self.cam1= cv2.VideoCapture("rtsp://{cam1_u}:{cam1_p}@{cam1_ip}/stream2".format(
                cam1_u  = CAMERAS[0]["Auth"]["User"],
                cam1_p  = CAMERAS[0]["Auth"]["Password"],
                cam1_ip = CAMERAS[0]["IP"]
            ))
            self.cam2 = cv2.VideoCapture("rtsp://{cam2_u}:{cam2_p}@{cam2_ip}/stream2".format(
                cam2_u  = CAMERAS[1]["Auth"]["User"],
                cam2_p  = CAMERAS[1]["Auth"]["Password"],
                cam2_ip = CAMERAS[1]["IP"] 
            ))

            ok1, self.frame1 = self.cam1.read()
            ok2, self.frame2 = self.cam2.read()

            if (ok1 and ok2) is not True:
                print("CAM error")

        def read(self):
            ok1, self.frame1 = self.cam1.read()
            ok2, self.frame2 = self.cam2.read()

            if (ok1 and ok2) is not True:
                return False, None
            
            return True, cv2.vconcat([self.frame1, self.frame2])

class UpdateCamera(QThread):
    changePixmap = Signal(QImage, int)
    
    def __init__(self):
        super().__init__()
        if ON_BOARD:
            pipeline = 'imxcompositor_g2d name=comp sink_0::xpos=0 sink_0::ypos=0 sink_1::xpos=0 sink_1::ypos=720 ' \
                '! queue ! appsink sync=false rtspsrc location="rtsp://{cam1_u}:{cam1_p}@{cam1_ip}/stream2" ! rtph264depay ! h264parse ! queue ! v4l2h264dec ' \
                '! queue ! comp. rtspsrc location="rtsp://{cam2_u}:{cam2_p}@{cam2_ip}/stream2" ! rtph264depay ! h264parse ! queue ! v4l2h264dec ! queue ! comp.'.format(
                cam1_u  = CAMERAS[0]["Auth"]["User"],
                cam1_p  = CAMERAS[0]["Auth"]["Password"],
                cam1_ip = CAMERAS[0]["IP"],
                cam2_u  = CAMERAS[1]["Auth"]["User"],
                cam2_p  = CAMERAS[1]["Auth"]["Password"],
                cam2_ip = CAMERAS[1]["IP"] 
            )
        
            self.cam = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
        elif ON_COMPUTER:
            self.cam = NonGstCam()
        else:
            self.cam = DummyCam()

        self.used_cams = len(CAMERAS)
        ok, self.raw_frame = self.cam.read()
        self.IS = []
        self.AI_data = []
        for i in range(self.used_cams):
            self.IS.append(DataTransmition.ImageSender(IMAGE_PROCESSORS[i]["IP"], IMAGE_PROCESSORS[i]["PORT"], [300, 300]))
            self.AI_data.append(None)
        
    def run(self):
        ok = True
        while ok:
            ok, self.raw_frame = self.cam.read()
            if ok:
                self.raw_frame = cv2.cvtColor(self.raw_frame, cv2.COLOR_BGR2RGBA)
                frame = [self.raw_frame[i * 720 : (i + 1) * 720, :, :] for i in range(self.used_cams)] 

                for i in range(self.used_cams):
                    self.IS[i].send(frame[i])
                    
                    if self.AI_data[i] is not None:
                        recv_time = float(self.AI_data[i]["sent-time"][1:])
                        try:
                            for G, score, face in zip(self.AI_data[i]["G"], self.AI_data[i]["scores"], self.AI_data[i]["faces"]):
                                f = [float(coord) for coord in face.split(',')]
                                g = [float(coord) for coord in G.split(',')]
                                frame[i] = cv2.rectangle(
                                    frame[i], 
                                    (int(f[1] * frame[i].shape[1]), int(f[0] * frame[i].shape[0])), 
                                    (int(f[3] * frame[i].shape[1]), int(f[2] * frame[i].shape[0])), 
                                    (255, 0, 0, 255), 2)
                                frame[i] = cv2.putText(
                                    frame[i], 
                                    "Score: " + score, 
                                    (int(f[1] * frame[i].shape[1]), int(f[0] * frame[i].shape[0]) - 5),
                                    1, 1, (255, 0, 0, 255), 2)
                                frame[i] = cv2.putText(
                                    frame[i], 
                                    str(round(time.time() - recv_time, 1)) + " secs ago", 
                                    (int(f[1] * frame[i].shape[1]), int(f[0] * frame[i].shape[0]) - 17),
                                    1, 1, (255, 0, 0, 255), 2)
                                frame[i] = cv2.rectangle(
                                    frame[i], 
                                    (int(g[1] * frame[i].shape[1]) - 7, int(g[0] * frame[i].shape[0]) - 7), 
                                    (int(g[1] * frame[i].shape[1]) + 7, int(g[0] * frame[i].shape[0]) + 7), 
                                    (255, 0, 0, 255), 6)
                        except:
                            print("No face found!")
                            
                        self.AI_data[i] = None

                    h, w, ch = frame[i].shape
                    bytesPerLine = ch * w
                    qt_frame = QImage(frame[i].data, w, h, bytesPerLine, QImage.Format_RGBA8888)
                    self.changePixmap.emit(qt_frame, i)

    def set_AI_results(self, json_like, index):
        self.AI_data[index] = json_like

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
                        pytapo.Tapo(cam["IP"], cam["Auth"]["User"], cam["Auth"]["Password"])
                    )
                not_ok = False
            except:
                not_ok = True

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
                    print(e)

class GetAIResults(QThread):
    send_json = Signal(dict, int)
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.RES = DataTransmition.UDPReceiver(FEEDBACKS[index]["IP"], FEEDBACKS[index]["PORT"])

    def run(self):
        while True:
            time.sleep(0.1)
            msg = self.RES.receive()
            try:
                json_like = json.loads(msg)
                self.send_json.emit(json_like, self.index)
            except Exception as e:
                print(e)
