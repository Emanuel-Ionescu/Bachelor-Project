import json
with open('./resources/data/config.json', 'r') as file:
    hardware_data = json.load(file)

IMAGE_PROCESSORS = [
    hardware_data["Platform"]["ImageProcessing1"],
    hardware_data["Platform"]["ImageProcessing2"]
    ]
FEEDBACKS = [
    hardware_data["Platform"]["GUIFeedback1"],
    hardware_data["Platform"]["GUIFeedback2"]
]
CAMERAS = list(hardware_data["Camera"].values())
TAPO_CAM_AUTH = {
    "User" : "TapoCam",
    "Password" : "salut123"
}
CAMERA_RESOLUTION = (1280, 720)
FRAME_SLICE_INFO = [
    [int(CAMERA_RESOLUTION[0]/4), int(3 * CAMERA_RESOLUTION[0]/4), int(CAMERA_RESOLUTION[1]/4), int(3 * CAMERA_RESOLUTION[1]/4), "w:0.25:0.5,h:0.25:0.5"], 
    [0                          , int(CAMERA_RESOLUTION[0]/2)    , 0                          , int(CAMERA_RESOLUTION[1]/2)    , "w:0.00:0.5,h:0.00:0.5"],
    [0                          , int(CAMERA_RESOLUTION[0]/2)    , int(CAMERA_RESOLUTION[1]/2), CAMERA_RESOLUTION[1]           , "w:0.50:0.5,h:0.00:0.5"],
    [int(CAMERA_RESOLUTION[0]/2), CAMERA_RESOLUTION[0]           , 0                          , int(CAMERA_RESOLUTION[1]/2)    , "w:0.00:0.5,h:0.50:0.5"],
    [int(CAMERA_RESOLUTION[0]/2), CAMERA_RESOLUTION[0]           , int(CAMERA_RESOLUTION[1]/2), CAMERA_RESOLUTION[1]           , "w:0.50:0.5,h:0.50:0.5"]
]

from HumanDetection import Model
from DataTransmition import ImageReceiver, UDPSender, ImageSender
import numpy as np
import threading 
import time
import argparse
import os
import cv2
import multiprocessing as mpc

pipeline = 'imxcompositor_g2d name=comp sink_0::xpos=0 sink_0::ypos=0 sink_1::xpos=0 sink_1::ypos=720 ' \
    '! queue ! appsink sync=false rtspsrc location="rtsp://{cam1_u}:{cam1_p}@{cam1_ip}/stream2" ! rtph264depay ! h264parse ! queue ! v4l2h264dec ' \
    '! queue ! comp. rtspsrc location="rtsp://{cam2_u}:{cam2_p}@{cam2_ip}/stream2" ! rtph264depay ! h264parse ! queue ! v4l2h264dec ! queue ! comp.'.format(
    cam1_u  = TAPO_CAM_AUTH["User"],
    cam1_p  = TAPO_CAM_AUTH["Password"],
    cam1_ip = CAMERAS[0]["IP"],
    cam2_u  = TAPO_CAM_AUTH["User"],
    cam2_p  = TAPO_CAM_AUTH["Password"],
    cam2_ip = CAMERAS[1]["IP"] 
)
FRAME_QUEUES = [mpc.Queue(1), mpc.Queue(1)]


def main(ID : int, frame_queue : mpc.Queue):
    loading_time = time.time()
    try:
        AI = Model(use_NPU=True)
    except:
        AI = Model(use_NPU=True, download=True)
    loading_time = time.time() - loading_time
    print("ML loaded in", loading_time, "seconds")

    IS = ImageSender(IMAGE_PROCESSORS[ID-1]["IP"], IMAGE_PROCESSORS[ID-1]["PORT"])
    FDBK = UDPSender(FEEDBACKS[ID-1]["IP"], FEEDBACKS[ID-1]["PORT"])
    frame = frame_queue.get(block=True)
    faces = AI.find_faces(frame)
    body = AI.find_body(frame)
    fps_time = time.time()
    print("Test frames recieved!")

    print("Starting...")
    while True:
        if frame_queue.empty() is True:
            time.sleep(0.02)
            continue

        os.system("clear")
        print("                         \rFPS:", 1/(time.time() - fps_time), end='\r')
        fps_time =  time.time()
        to_be_sent = {}
        frame = frame_queue.get()
        IS.send(frame)
        # message = message.split()[0]
        # option, width, height = message.split(',')
        option = "all"

        # if(option == "add"):
        #     username = width # working on older code where the second argument was width
        #     faces = AI.find_faces(frame)
        #     face = faces[0][0]
        #     face *= 300
        #     G = [(face[0]+face[2]) * .5, (face[1]+face[3]) * .5]
        #     to_be_sent["G"].append(str(G[0]/300) + ", " + str(G[1]/300))
        #     dist = min(face[2] - face[0], face[3] - face[1]) * .5

        #     face[0] = G[0] - dist
        #     face[1] = G[1] - dist
        #     face[2] = G[0] + dist
        #     face[3] = G[1] + dist

        #     face = np.array(face, np.int32)

        #     cropped_frame = frame[face[0] : face[2], face[1] : face[3]]
        #     mask = AI.id_face(cropped_frame)
        #     with open('./resources/data/users.json', 'r') as file:
        #         users_data = json.load(file)
            
        #     if username in users_data.keys() is False:
        #         users_data[username] = []
            
        #     users_data[username].append(str(mask))

        #     with open('./resources/data/users.json', 'w') as file:
        #         json.dump(users_data, file)
        #     continue

        if(option == "all" or option == "face"):
            faces = AI.find_faces(frame.copy())

            # recursive splitting the frame
            if faces is None:
                faces = []
                for slice_info in FRAME_SLICE_INFO:
                    x1, x2, y1, y2, args = slice_info
                    _, xa, _ = args.split(',')[0].split(':')
                    _, ya, _ = args.split(',')[1].split(':')
                    print(frame.shape)
                    aux = frame.copy()[y1 : y2, x1 : x2]
                    print(aux.shape)
                    slice_faces = AI.find_faces(aux)
                    if slice_faces is not None:
                        for f in slice_faces:
                            f_aux = f
                            f_aux[0][0] += float(xa)
                            f_aux[0][1] += float(ya)
                            f_aux[0][2] += float(xa)
                            f_aux[0][3] += float(ya)
                            faces.append(f_aux)

            if faces is not [] or faces != []:
                print(len(faces))
                to_be_sent["faces"]  = []
                to_be_sent["scores"] = []
                to_be_sent["G"]      = []
                to_be_sent["masks"]  = []  

                for face in faces:
                    to_be_sent["faces"].append(str(list( face[0]))[1:-1])
                    to_be_sent["scores"].append(str(face[1]))

                    face = face[0]
                    face *= 300
                    G = [(face[0]+face[2]) * .5, (face[1]+face[3]) * .5]
                    to_be_sent["G"].append(str(G[0]/300) + ", " + str(G[1]/300))
                    dist = min(face[2] - face[0], face[3] - face[1]) * .5

                    face[0] = G[0] - dist
                    face[1] = G[1] - dist
                    face[2] = G[0] + dist
                    face[3] = G[1] + dist

                    face = np.array(face, np.int32)

                    cropped_frame = frame[face[0] : face[2], face[1] : face[3]]
                    #mask = AI.id_face(cropped_frame)
                    #to_be_sent["masks"].append(str(mask)[1:-1])
            else:
                print("None")

        print("Body: ", end="")

        if(option == "all" or option == "body"):
            body = AI.find_body(frame)
            if body is not None:
                print("Found")
                to_be_sent["body"] = {
                        "x"     : np.array(body[0], dtype=np.int32).tolist(),
                        "y"     : np.array(body[1], dtype=np.int32).tolist(),
                        # "score" : np.array(body[2], dtype=np.int32).tolist()
                    }
            else:
                print("None")

        to_be_sent["ID"] = ID
        to_be_sent["offset"] = "0,0"
        to_be_sent["sent-time"] = "t" + str(time.time())
        FDBK.send(json.dumps(to_be_sent))


if __name__ == "__main__":
    proc = [
        mpc.Process(target=main, args=(1, FRAME_QUEUES[0])),
        mpc.Process(target=main, args=(2, FRAME_QUEUES[1]))
    ]

    proc[0].start()
    proc[1].start()

    while True:
        CAM = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
        ok = True
        while ok:
            ok, raw_frame = CAM.read()
            raw_frame = cv2.cvtColor(raw_frame, cv2.COLOR_BGRA2BGR)
            frame = [raw_frame[i * 720 : (i + 1) * 720, :, :] for i in range(2)]
            for i in range(2):
                if FRAME_QUEUES[i].empty():
                    FRAME_QUEUES[i].put(frame[i])
            

