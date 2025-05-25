from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import datetime
import cv2
import numpy as np
import socket

class ImageSender:

    def __init__(self, DEST_IP_ADDR, DEST_PORT, RESOLUTION):
        self.dest_ip = DEST_IP_ADDR
        self.dest_port = DEST_PORT
        self.resolution = RESOLUTION
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Image sender created:", self.dest_ip, self.dest_port)

    def send(self, frame = None, aux_data : str = " "):
        if frame is None:
            return
        if len(aux_data) > 32:
            aux_data = aux_data[:32]
        elif len(aux_data) < 32:
            aux_data = aux_data.ljust(32)

        s_frame = cv2.resize(frame, self.resolution, cv2.INTER_LINEAR) # to be changd if nedded
        s_frame = cv2.cvtColor(s_frame, cv2.COLOR_BGR2RGB)

        _, buffer = cv2.imencode('.jpg',s_frame,(cv2.IMWRITE_JPEG_QUALITY,80))
        self.sock.sendto(aux_data.encode() + bytes(buffer), (self.dest_ip, self.dest_port))


class ImageReceiver:

    def __init__(self, MY_IP_ADDR, MY_PORT):
        self.host_ip = MY_IP_ADDR
        self.host_port = MY_PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        buffer_size = 64 * 1024 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buffer_size)
        self.sock.bind((self.host_ip, self.host_port))
        print("Image reciever created:", self.host_ip, self.host_port)

    def receive(self):
        buffer, _ = self.sock.recvfrom(65000)
        aux_data = buffer[:32]
        nparr = np.frombuffer(buffer[32:],np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return aux_data.decode(), img


class UDPSender:
    def __init__(self, IP_ADDR, PORT):
        self.dest_ip = IP_ADDR
        self.dest_port = PORT
        
        t = datetime.datetime.now()
        self.key_parts = []
        self.aes = AES.new("1234567890123456".encode("utf-8"), AES.MODE_CBC, 'This is an IV456'.encode("utf-8"))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("UDP sender created:", self.dest_ip, self.dest_port)

    def send(self, text : str):
        cip = self.aes.encrypt(pad(text.encode("utf-8"), 16))
        self.sock.sendto(bytes(cip), (self.dest_ip, self.dest_port))

class UDPReceiver:

    def __init__(self, IP_ADDR, PORT):
        self.host_ip = IP_ADDR
        self.host_port = PORT
        
        t = datetime.datetime.now()
        self.key_parts = []
        self.aes = AES.new("1234567890123456".encode("utf-8"), AES.MODE_CBC, 'This is an IV456'.encode("utf-8"))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.sock.bind((self.host_ip, self.host_port))
        print("UDP receiver created:", self.host_ip, self.host_port)

    def receive(self):
        cip, _ = self.sock.recvfrom(65000)
        return unpad(self.aes.decrypt(cip), 16)
