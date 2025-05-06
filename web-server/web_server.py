import json
with open('../resources/data/config.json', 'r') as file:
    hardware_data = json.load(file)

CAMERAS = list(hardware_data["Camera"].values())

import sys
sys.path.append("..")

import flask as fsk
import os
import cv2
import numpy as np
import multiprocessing as mpc
import time
import socket
import datetime
from DataTransmition import UDPSender

US = UDPSender(
    hardware_data["Platform"]["GUIWebCommands"]["IP"],
    hardware_data["Platform"]["GUIWebCommands"]["PORT"]
)

def main():

    app = fsk.Flask("SmartHome")
    app.secret_key = "nxp12345"

    @app.route('/')
    def init():
        return fsk.redirect(fsk.url_for("livingroom"))
    
    '''
    Rooms loading functions
    & display
    '''

    @app.route('/livingroom')
    def livingroom():
        return fsk.render_template("livingroom.html")
    

    @app.route('/bedroom1')
    def bedroom1():
        return fsk.render_template("bedroom1.html")

    '''
    Camera functions
    '''

    def gen_frames(room):  
        
        frame_dict = {
            "Bedroom1"   : '',
            "Livingroom" : ''
        }

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
        cam = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

        while True:
            ok, frame = cam.read()
            if ok:
                for i, k in enumerate(frame_dict.keys()):
                    frame_dict[k] = frame[i * 720 : (i + 1) * 720, :, :]

                if room in frame_dict.keys():
                    ret, buffer = cv2.imencode('.jpg', frame_dict[room])
                    frame = buffer.tobytes()
            else:
                frame = np.random.randint(255, size=(16,9,3),dtype=np.uint8)
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    @app.route('/video_feed_livingroom')
    def video_feed_livingroom():
        return fsk.Response(gen_frames("Livingroom"), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    @app.route('/video_feed_bedroom_1')
    def video_feed_bedroom_1():
        return fsk.Response(gen_frames("Bedroom1"), mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route('/camera_move', methods=["POST", "GET"])
    def camera_move():
        room      = fsk.request.json.get("room", 0)
        direction = fsk.request.json.get("direction", 0)
        US.send("CAMERA:{}:{}".format(room, direction))

        return fsk.jsonify({"message":"Camera moved"})

    app.logger.disabled = True
    app.run(debug=False, host="0.0.0.0", port=80)

if __name__ == "__main__":
    main()