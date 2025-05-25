DEBUG = True
def ECHO(arg):
    if DEBUG:
        print(arg)

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

from HumanDetection import Model
from DataTransmition import ImageReceiver, UDPSender
import numpy as np
import threading 
import time
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("ID", help="Image Processor ID", type=int)
args = parser.parse_args()
ID = args.ID

def loading_bar(est):
    dt = 10/est
    l = 0
    for i in range(est * 10):
        print("Loading:", str(int(l))+'%', '█' * int(l/10) + '-' * (10 - int(l/10)), end='\r')
        l += dt
        time.sleep(0.1)
    print("                            ", end='\r')


def main():

    loading_time = time.time()
    estimated_loading_time = 2

    t1 = threading.Thread(target=loading_bar, args=(estimated_loading_time,))
    t1.start()

    IR = ImageReceiver(IMAGE_PROCESSORS[ID-1]["IP"], IMAGE_PROCESSORS[ID-1]["PORT"])
    FDBK = UDPSender(FEEDBACKS[ID-1]["IP"], FEEDBACKS[ID-1]["PORT"])

    try:
        AI = Model(use_NPU=True)
        #AI.getDetails()
    except:
        AI = Model(use_NPU=True, download=True)

    loading_time = time.time() - loading_time
    t1.join()
    print("ML loaded in", loading_time, "seconds")

    message, frame = IR.receive()

    faces = AI.find_faces(frame)
    body = AI.find_body(frame)

    print("Test frames recieved!")
    fps_time = time.time()

    print("Starting...")
    while True:
        
        os.system("clear")
        print("                         \rFPS:", 1/(time.time() - fps_time), end='\r')
        fps_time =  time.time()

        to_be_sent = {}

        message, frame = IR.receive()
        message = message.split()[0]
        option, width, height = message.split(',')

        print("\nInstruction:", message)
        print("Face: ", end="")

        if(option == "add"):
            username = width # working on older code where the second argument was width
            faces = AI.find_faces(frame)
            face = faces[0][0]
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
            mask = AI.id_face(cropped_frame)
            with open('./resources/data/users.json', 'r') as file:
                users_data = json.load(file)
            
            if username in users_data.keys() is False:
                users_data[username] = []
            
            users_data[username].append(str(mask))

            with open('./resources/data/users.json', 'w') as file:
                json.dump(users_data, file)
            continue

        if(option == "all" or option == "face"):
            faces = AI.find_faces(frame)
            if faces is not None:
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
                    ECHO("Math made")
                    #mask = AI.id_face(cropped_frame)
                    ECHO("ID ready")
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
        to_be_sent["offset"] = width + "," + height
        to_be_sent["sent-time"] = "t" + str(time.time())
        FDBK.send(json.dumps(to_be_sent))


if __name__ == "__main__":
    main()