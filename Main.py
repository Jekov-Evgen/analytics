from GUI.MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    
    w = MainWindow()
    
    app.exec()