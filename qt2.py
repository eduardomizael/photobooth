import sys
import time
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from qt_window import Ui_MainWindow


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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.showFullScreen()

        self.img_take1.setPixmap(QPixmap("img1.jpg"))
        self.img_take2.setPixmap(QPixmap("img2.jpg"))
        self.img_take3.setPixmap(QPixmap("img3.jpg"))
        self.img1_taken = False
        self.img2_taken = False
        self.img3_taken = False
        self.counters = [QPixmap(f"elements/counter_{i}.png") for i in range(1, 4)]
        self.img_counter.setVisible(False)

        self.webcam_thread = WebcamThread()
        self.webcam_thread.update_signal.connect(self.update_image)
        self.webcam_thread.start()

        self.actual_frame = None

        self.pushButton.clicked.connect(self.img_take)


    def update_image(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.actual_frame = pixmap
        self.img_cam.setPixmap(pixmap)

    def show_counter(self, take_img):
        self.img_counter.setVisible(True)
        self.img_counter.setPixmap(self.counters[2])
        time.sleep(1)
        self.img_counter.setPixmap(self.counters[1])
        time.sleep(1)
        self.img_counter.setPixmap(self.counters[0])
        time.sleep(1)
        self.img_counter.setVisible(False)
        if take_img == 1:
            self.img_take1.setPixmap(self.actual_frame)
        elif take_img == 2:
            self.img_take2.setPixmap(self.actual_frame)
        elif take_img == 3:
            self.img_take3.setPixmap(self.actual_frame)

    def img_take(self):
        QTimer.singleShot(2000, lambda: self.show_counter(3))
        
        QTimer.singleShot(3000, lambda: self.show_counter(2))
        QTimer.singleShot(4000, lambda: self.show_counter(1))
        QTimer.singleShot(5000, lambda: self.img_counter.setVisible(False))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())