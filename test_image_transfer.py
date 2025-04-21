import cv2
import numpy as np
import os
import requests as rq
import time
import json
from DataTransmition import ImageReceiver, ImageSender, UDPSender, UDPReceiver

resolutions = {
    "no-split" : (300, 300),
    "4 splits" : (600, 600),
    "HD"       : (1280, 720),
    "Full HD"  : (1920, 1080),
    "Ultra HD" : (3840, 2160),
}

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("NODE_NUMBER", type=int)
args = parser.parse_args()
NODE_NUMBER = args.NODE_NUMBER

USER_1 = "nxg05093"
IP_1 = "192.168.1.8"
PORT_TEXT_1 = 12345
PORT_TEXT_1 = 12346


USER_2 = "root"
IP_2 = "192.168.1.7"
PORT_TEXT_2 = 12347
PORT_IMG_2 = 12348

def sync_clock():
    if os.getuid() != 0:
        exit("Must be root")

    for i in range(10):
        os.system("date -s \"$(ssh {}@{})\"".format(USER_1, IP_1))

    print("syncing ended")

def node1():

    IS1 = ImageSender(IP_2, PORT_IMG_2, (300, 300))
    US1 = UDPSender(IP_2, PORT_TEXT_2)
    UR1 = UDPReceiver(IP_1, PORT_TEXT_1)
    
    

def node2():

    IR2 = ImageReceiver(IP_2, PORT_IMG_2, (300, 300))
    UR2 = UDPReceiver(IP_2, PORT_TEXT_2)
    US2 = UDPSender(IP_1, PORT_TEXT_1)

    
        
if __name__ == "__main__":
    if NODE_NUMBER == 1:
        node1()
    else:
        node2()