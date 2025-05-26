import json
with open('./resources/data/config.json', 'r') as file:
    hardware_data = json.load(file)

ROOMS_ALIASES = []
for camera in hardware_data["Camera"].values():
    ROOMS_ALIASES.append(camera["Location"])

LIGHT_SOURCES = hardware_data["SmartDevice"]["Light"]

CAMS_NUM = len(hardware_data["Camera"].keys())

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Signal, Slot, Qt, QSize
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QGraphicsScene
from window import Ui_MainWindow
import color_picker
import loops
import socket

class ColorPicker(QMainWindow):
    
    color = Signal(int, int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = color_picker.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

        self.ui.bttn_00ff00.clicked.connect(self.color_pressed)
        self.ui.bttn_00ff55.clicked.connect(self.color_pressed)
        self.ui.bttn_55ff00.clicked.connect(self.color_pressed)
        self.ui.bttn_00ffaa.clicked.connect(self.color_pressed)
        self.ui.bttn_55ff55.clicked.connect(self.color_pressed)
        self.ui.bttn_aaff00.clicked.connect(self.color_pressed)
        self.ui.bttn_00ffff.clicked.connect(self.color_pressed)
        self.ui.bttn_55ffaa.clicked.connect(self.color_pressed)
        self.ui.bttn_aaff55.clicked.connect(self.color_pressed)
        self.ui.bttn_ffff00.clicked.connect(self.color_pressed)
        self.ui.bttn_00aaff.clicked.connect(self.color_pressed)
        self.ui.bttn_aaffff.clicked.connect(self.color_pressed)
        self.ui.bttn_ffffff.clicked.connect(self.color_pressed)
        self.ui.bttn_ffffaa.clicked.connect(self.color_pressed)
        self.ui.bttn_ffaa00.clicked.connect(self.color_pressed)
        self.ui.bttn_0055ff.clicked.connect(self.color_pressed)
        self.ui.bttn_55aaff.clicked.connect(self.color_pressed)
        self.ui.bttn_aaaaff.clicked.connect(self.color_pressed)
        self.ui.bttn_00aaff.clicked.connect(self.color_pressed)
        self.ui.bttn_ffaa55.clicked.connect(self.color_pressed)
        self.ui.bttn_ff5500.clicked.connect(self.color_pressed)
        self.ui.bttn_0000ff.clicked.connect(self.color_pressed)
        self.ui.bttn_5500ff.clicked.connect(self.color_pressed)
        self.ui.bttn_aa00ff.clicked.connect(self.color_pressed)
        self.ui.bttn_ff00ff.clicked.connect(self.color_pressed)
        self.ui.bttn_ff00aa.clicked.connect(self.color_pressed)
        self.ui.bttn_ff0055.clicked.connect(self.color_pressed)
        self.ui.bttn_ff0000.clicked.connect(self.color_pressed)
  
        self.ui.exit_button.clicked.connect(self.close)

    @Slot()
    def color_pressed(self):
        s = self.sender()
        hex_color = s.objectName().split("_")[1]
        self.color.emit(int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16))


class MainWindow(QMainWindow):

    move_camera = Signal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # ==========================================================================================
    # WEB
    # ==========================================================================================

        self.web_commands_thread = loops.GetWebCommands()

    # ==========================================================================================
    # LIGHTS
    # ==========================================================================================

        self.commands_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.color_picker_dialog = ColorPicker()
        self.color_picker_dialog.color.connect(self.set_lights_color)

        self.lights_location = "Livingroom"
        for room in ROOMS_ALIASES:
            self.ui.light_location_selector.addItem(room)
        self.ui.light_source_selector.addItem("All")
        for option in LIGHT_SOURCES.keys():
            if LIGHT_SOURCES[option]["Location"] == "Livingroom":
                self.ui.light_source_selector.addItem(option)
        self.ui.light_location_selector.currentTextChanged.connect(self.set_lights_location)

        self.ui.lights_off_bttn.clicked.connect(self.set_lights_off)
        self.ui.lights_on_bttn.clicked.connect(self.set_lights_on)
        self.ui.lights_color_bttn.clicked.connect(self.color_picker_dialog.show)


    # ==========================================================================================
    # CAMERA
    # ==========================================================================================

        self.cam_in_use = 0
        for i in range(CAMS_NUM):
            self.ui.camera_location_selector.addItem(str(i) + " : " + str(ROOMS_ALIASES[i]))

        self.ui.camera_location_selector.currentIndexChanged.connect(self.set_camera_location)
        self.camera_thread = loops.UpdateCamera()
        self.camera_thread.changePixmap.connect(self.set_camera_image)
        self.camera_thread.start()

        self.camera_controll_thread = loops.MoveCamera()
        self.ui.camera_bttn_up.clicked.connect(self.cam_move_pressed_up)
        self.ui.camera_bttn_down.clicked.connect(self.cam_move_pressed_down)
        self.ui.camera_bttn_right.clicked.connect(self.cam_move_pressed_right)
        self.ui.camera_bttn_left.clicked.connect(self.cam_move_pressed_left)
        self.move_camera.connect(self.camera_controll_thread.move)
        self.camera_controll_thread.start()

        self.AI_result1_thread = loops.GetAIResults(0)
        self.AI_result1_thread.send_json.connect(self.camera_thread.set_AI_results)
        self.AI_result1_thread.start()
        self.AI_result2_thread = loops.GetAIResults(1)
        self.AI_result2_thread.send_json.connect(self.camera_thread.set_AI_results)
        self.AI_result2_thread.start()

        # connection with web
        self.web_commands_thread.send_camera_move.connect(self.camera_controll_thread.move)
        self.web_commands_thread.start()

    # ==========================================================================================
    # TEMPERATURE
    # ==========================================================================================

        self.temperature_text = "{}°C\n{}"
        self.temperature_data = [22, "Hot"]

        self.ui.temperature_up_bttn.clicked.connect(self.set_temperature_up)
        self.ui.temperature_down_bttn.clicked.connect(self.set_temperature_down)
        self.ui.temperature_hot_bttn.clicked.connect(self.set_temperature_hot)
        self.ui.temperature_cold_bttn.clicked.connect(self.set_temperature_cold)
        self.ui.temperature_dry_bttn.clicked.connect(self.set_temperature_dry)
        self.ui.temperature_turbo_bttn.clicked.connect(self.set_temperature_turbo)

        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))

    # ==========================================================================================
    # USERS
    # ==========================================================================================

        self.ui.add_user_bttn.clicked.connect(self.add_user)
        self.ui.remove_user_bttn.clicked.connect(self.remove_user)

    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    # LIGHTS FUNCTIONS
    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

    @Slot(str)
    def set_lights_location(self, option):
        self.lights_location = option 
        self.ui.light_source_selector.clear()
        self.ui.light_source_selector.addItem("All")
        for opt in LIGHT_SOURCES.keys():
            if LIGHT_SOURCES[opt]["Location"] == option:
                self.ui.light_source_selector.addItem(opt)

    @Slot(int, int, int)
    def set_lights_color(self, r, g, b):
        bulbs = []
        if self.ui.light_source_selector.currentText() == "All":
            for opt in LIGHT_SOURCES.keys():
                if LIGHT_SOURCES[opt]["Location"] == self.lights_location:
                    bulbs.append(opt)
        else:
            bulbs.append(self.ui.light_source_selector.currentText())

        for bulb in bulbs:
            self.commands_sock.sendto(
                "LIGHT:{}:COLOR({},{},{})".format(bulb, r,g,b).encode(),
                (
                    hardware_data["Platform"]["HomeAssistant"]["IP"],
                    hardware_data["Platform"]["HomeAssistant"]["PORT"]
                )
            )

    @Slot()
    def set_lights_off(self):
        bulbs = []
        if self.ui.light_source_selector.currentText() == "All":
            for opt in LIGHT_SOURCES.keys():
                if LIGHT_SOURCES[opt]["Location"] == self.lights_location:
                    bulbs.append(opt)
        else:
            bulbs.append(self.ui.light_source_selector.currentText())

        for bulb in bulbs:
            self.commands_sock.sendto(
                "LIGHT:{}:OFF".format(bulb).encode(),
                (
                    hardware_data["Platform"]["HomeAssistant"]["IP"],
                    hardware_data["Platform"]["HomeAssistant"]["PORT"]
                )
            )

    @Slot()
    def set_lights_on(self):
        bulbs = []
        if self.ui.light_source_selector.currentText() == "All":
            for opt in LIGHT_SOURCES.keys():
                if LIGHT_SOURCES[opt]["Location"] == self.lights_location:
                    bulbs.append(opt)
        else:
            bulbs.append(self.ui.light_source_selector.currentText())

        for bulb in bulbs:
            self.commands_sock.sendto(
                "LIGHT:{}:ON".format(bulb).encode(),
                (
                    hardware_data["Platform"]["HomeAssistant"]["IP"],
                    hardware_data["Platform"]["HomeAssistant"]["PORT"]
                )
            )


    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    # CAMERA FUNCTIONS
    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

    @Slot(str)
    def set_camera_location(self, option):
        self.cam_in_use = option  

    @Slot(QImage, int)
    def set_camera_image(self, image, cam_num):
        if cam_num == self.cam_in_use:
            # image = image.scaled(
            #     self.ui.camera_display.width() - 10,
            #     self.ui.camera_display.height() - 10,
            #     Qt.AspectRatioMode.KeepAspectRatio)
            self.ui.camera_display.setPixmap(QPixmap.fromImage(image))

        # if ROOMS_ALIASES[cam_num] == "Livingroom":
        #     self.ui.user_camera_display.setPixmap(QPixmap.fromImage(image.copy(390, 110, 890, 610)))

    @Slot()
    def cam_move_pressed_up(self):
        self.move_camera.emit(self.cam_in_use, "UP")

    @Slot()
    def cam_move_pressed_down(self):
        self.move_camera.emit(self.cam_in_use, "DOWN")

    @Slot()
    def cam_move_pressed_right(self):
        self.move_camera.emit(self.cam_in_use, "RIGHT")

    @Slot()
    def cam_move_pressed_left(self):
        self.move_camera.emit(self.cam_in_use, "LEFT")

    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    # TEMPERATURE FUNCTIONS
    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

    @Slot()
    def set_temperature_up(self):
        if self.temperature_data[0] < 32: 
            self.temperature_data[0] += 1
        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))

    @Slot()
    def set_temperature_down(self):
        if self.temperature_data[0] > 16: 
            self.temperature_data[0] -= 1
        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))

    @Slot()
    def set_temperature_hot(self):
        self.temperature_data[1] = "Hot"
        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))

    @Slot()
    def set_temperature_cold(self):
        self.temperature_data[1] = "Cold"
        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))

    @Slot()
    def set_temperature_dry(self):
        self.temperature_data[1] = "Dry"
        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))

    @Slot()
    def set_temperature_turbo(self):
        self.temperature_data[1] = "Turbo"
        self.ui.temperature_display.setText(self.temperature_text.format(*self.temperature_data))


    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    # USERS FUNCTIONS
    # +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

    @Slot()
    def add_user(self):
        user = self.ui.username_entry.text()

    def remove_user(self):
        user = self.ui.username_entry.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showFullScreen()
    import time
    time.sleep(100)
    sys.exit(app.exec())
    
