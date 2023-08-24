import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1920, 1080)  # Tamanho da tela
        self.setWindowState(Qt.WindowFullScreen)  # Tela em fullscreen

        # Background
        background_label = QLabel(self)
        background_pixmap = QPixmap(r"elements\Fundo.png")
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, 1920, 1080)  # Tamanho da tela

        button_image = QPushButton(self)
        button_pixmap = QPixmap(r"elements\btn.png")  # Substitua pelo caminho da sua imagem
        button_icon = QIcon(button_pixmap)
        button_image.setIcon(button_icon)
        button_image.setIconSize(button_icon.rect().size())
        button_image.setGeometry(928, 858, 464, 206) 


        overlay_label = QLabel(self)
        overlay_pixmap = QPixmap(r"elements\screen_overlay.png")
        overlay_label.setPixmap(overlay_pixmap)
        overlay_label.setGeometry(0, 0, 1920, 1080)


        # Fotos menores
        photo_size = (338, 190)
        photo_positions = [(92, 100), (92, 356), (92, 617)]
        for i, position in enumerate(photo_positions):
            photo_label = QLabel(self)
            photo_label.setGeometry(position[0], position[1], photo_size[0], photo_size[1])
            photo_label.setStyleSheet("border: 2px solid white;")
            self.show_webcam_preview(photo_label)  # Função para mostrar o preview da webcam

    def show_webcam_preview(self, label):
        # Simulação de captura da webcam usando uma imagem (substitua por código de captura real)
        webcam_image = QImage("img1.jpg")  # Substitua pela captura real da webcam
        webcam_pixmap = QPixmap.fromImage(webcam_image).scaled(338, 190, Qt.KeepAspectRatio)
        label.setPixmap(webcam_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
