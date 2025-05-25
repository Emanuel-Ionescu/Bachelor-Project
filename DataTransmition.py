from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import datetime
import cv2
import numpy as np
import socket
import time

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

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = frame.shape
        rows, cols = height//300 + 1, width//300 + 1 
        s_height = int(height/rows)
        s_width = int(width/rows)


        ID = str(int(time.time() * 1000))
        slice_index = 0
        self.sock.sendto(f"start/{ID}/{rows}/{cols}/{s_height}/{s_width}".encode(), (self.dest_ip, self.dest_port))
        self.sock.sendto(aux_data.encode(), (self.dest_ip, self.dest_port))
        for i in range(1, rows):
            for e in range(1, cols):
                slice_index += 1
                s_frame = frame[ (i-1) * s_height : i * s_height, (e-1) * s_width : e * s_width]
                _, buffer = cv2.imencode('.jpg',s_frame,(cv2.IMWRITE_JPEG_QUALITY,90))
                self.sock.sendto(f"{slice_index:02d}".encode() + bytes(buffer), (self.dest_ip, self.dest_port)) 
        self.sock.sendto(f"end/{ID}".encode(), (self.dest_ip, self.dest_port))


class ImageReceiver:

    def __init__(self, MY_IP_ADDR, MY_PORT):
        self.host_ip = MY_IP_ADDR
        self.host_port = MY_PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        buffer_size = 64 * 1024 * 48 # create image queue of 48 packets
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, buffer_size)
        self.sock.bind((self.host_ip, self.host_port))
        self.frame = None
        print("Image reciever created:", self.host_ip, self.host_port)

    def receive(self):
        buffer, _ = self.sock.recvfrom(65000)

        if buffer.decode().split("/")[0] == "start":
            ID, rows, cols, s_height, s_width = list(map(int, buffer.decode().split('/')[1:])) 
            aux_data, _ = self.sock.recvfrom(65000)

            frame = np.zeros((rows * s_height, cols * s_width, 3), dtype=np.uint8)

            for i in range(rows * cols):
                buffer, _ = self.sock.recvfrom(65000)
                
                # if recieved end/start unexpected
                if buffer.decode().split('/') == "end" or buffer.decode().split('/') == "start":
                    return aux_data.decode(), frame

                index, img_buffer = int(buffer[:2].decode()), buffer[2:]
                nparr = np.frombuffer(img_buffer,np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                i = index // rows + 1
                e = index % cols  + 1
                frame[ (i-1) * s_height : i * s_height, (e-1) * s_width : e * s_width] = img

        return aux_data.decode(), frame


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
