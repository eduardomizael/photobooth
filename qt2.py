import sys
import time
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal, QRect, QRunnable, QThreadPool, QSize
from PyQt5.QtGui import QPixmap, QImage, QIcon
from qt_window import Ui_MainWindow
from image_composer import ImageComposer
from PIL import Image


class WebcamTask(QRunnable):
    def run(self):
        capture = cv2.VideoCapture(0)

        while True:
            ret, frame = capture.read()
            if ret:
                self.update_signal.emit(frame)
            else:
                break


class WebcamThread(QThread):
    update_signal = pyqtSignal(np.ndarray)

    def run(self):
        capture = cv2.VideoCapture(0)

        while True:
            ret, frame = capture.read()
            if ret:
                self.update_signal.emit(frame)
            else:
                break

class TakePictureThread(QThread):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):
        def show_counter():
            time.sleep(1)
            self.window.img_counter.setPixmap(self.window.counters[2])
            self.window.img_counter.setVisible(True)
            time.sleep(1)
            self.window.img_counter.setPixmap(self.window.counters[1])
            time.sleep(1)
            self.window.img_counter.setPixmap(self.window.counters[0])
            time.sleep(1)
            self.window.img_counter.setVisible(False)
        
        def toggle_flash():
            flash = self.window.flash_label
            flare = self.window.flare_label

            flare.setVisible(True)
            flare.raise_()
            time.sleep(0.1)
            flash.setVisible(True)
            flash.raise_()
            time.sleep(0.1)

            flash.setVisible(False)
            flare.setVisible(False)

        show_counter()
        toggle_flash()
        self.window.take_picture(1)
        show_counter()
        toggle_flash()
        self.window.take_picture(2)
        show_counter()
        toggle_flash()
        self.window.take_picture(3)
        self.window.compose()

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.showFullScreen()

        self.img_takes = [QPixmap(f"img{i}.jpg") for i in range(1, 4)]
        self.counters = [QPixmap(f"elements/counter_{i}.png") for i in range(1, 4)]

        self.img_take1.setPixmap(QPixmap())
        self.img_take2.setPixmap(QPixmap())
        self.img_take3.setPixmap(QPixmap())
        self.img_counter.setVisible(False)

        self.webcam_thread = WebcamThread()
        self.webcam_thread.update_signal.connect(self.update_image)
        self.webcam_thread.start()

        self.raw_frame = None
        self.actual_frame = None

        self.pushButton.clicked.connect(self.take_pictures)
        self.img_preview.clicked.connect(self.clear_pictures)

    def toggle_flash(self):
            flash = self.flash_label
            flare = self.flare_label

            flare.setVisible(True)
            flare.raise_()
            time.sleep(0.1)
            flash.setVisible(True)
            flash.raise_()
            time.sleep(0.1)

            flash.setVisible(False)
            flare.setVisible(False)

    def take_picture(self, control):
        match control:
            case 1:
                self.img_take1.setPixmap(self.actual_frame)
                self.img1 = self.frame_to_pil(self.raw_frame)
            case 2:
                self.img_take2.setPixmap(self.actual_frame)
                self.img2 = self.frame_to_pil(self.raw_frame)
            case 3:
                self.img_take3.setPixmap(self.actual_frame)
                self.img3 = self.frame_to_pil(self.raw_frame)

    def clear_pictures(self):
        # self.img_take1.setPixmap(self.img_takes[0])
        # self.img_take2.setPixmap(self.img_takes[1])
        # self.img_take3.setPixmap(self.img_takes[2])
        self.img_preview.setVisible(False)
        self.img1 = None
        self.img2 = None
        self.img3 = None
        self.pushButton.setEnabled(True)

    def take_pictures(self):
        self.pushButton.setEnabled(False)
        self.tp_thread = TakePictureThread(self)
        self.tp_thread.start()

    def frame_to_pixmap(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        return pixmap

    def frame_to_pil(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        return Image.fromarray(frame)

    def update_image(self, frame):
        self.raw_frame = frame
        self.actual_frame = self.frame_to_pixmap(frame)
        self.img_cam.setPixmap(self.actual_frame)

    def compose(self) -> None:
        """Compor a imagem final.
        :return: None
        """
        imgs = [self.img1, self.img2, self.img3]
        # imgs = []
        # for i in range(4):
        #     imgs.append(self.frame_to_pil(self.raw_frame))

        ic = ImageComposer(images=imgs)
        composed_photo = ic.photo_compose()
        composed_media = ic.media_compose()
        self.load_preview_image(str(composed_photo[1]))
    
    def load_preview_image(self, path) -> None:
        """Carrega a imagem de preview.
        :param path: Caminho do arquivo
        :return: None
        """
        icon = QIcon()
        icon.addFile(path, self.img_preview.size(), QIcon.Normal, QIcon.Off)
        self.img_preview.setIcon(icon)
        self.img_preview.setIconSize(self.img_preview.size())
        # pixmap = QPixmap(path)
        # pixmap = pixmap.scaled(self.img_preview.size(), Qt.KeepAspectRatio)
        # self.img_preview.setPixmap(pixmap)
        self.img_preview.setVisible(True)
        self.img_preview.raise_()


if __name__ == "__main__":
    pass