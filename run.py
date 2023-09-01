#! venv/Scripts/python

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from qt2 import MainWindow
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())