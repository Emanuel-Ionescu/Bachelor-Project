import json
with open('./resources/data/config.json', 'r') as file:
    hardware_data = json.load(file)

from HA_controller import Controller
import socket

def main():
    controller = Controller(hardware_data["Platform"]["HomeAssistant"]["Token"])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((
        hardware_data["Platform"]["HomeAssistant"]["IP"],
        hardware_data["Platform"]["HomeAssistant"]["PORT"]
    ))

    print("Home Assisntant controller started!")
    while True:
        command, addr = sock.recvfrom(1024)
        command = command.decode()
        print("Recieved command:", command)

        device_type = command.split(':')[0]
        if device_type == "LIGHT":
            _, bulb, action = command.split(':')
            if action.find("COLOR") != -1:
                r,g,b = action.split('(')[1].split(')')[0].split(',')
                controller.set(bulb, "ON", {"rgb_color" : [r, g, b]})
            else:
                controller.set(bulb, action)



if __name__ == "__main__":
    main()