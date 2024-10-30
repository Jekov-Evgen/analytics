from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
from GUI.Style import CONST_STYLE_WINDOW
from tkinter import filedialog


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(300, 250)
        self.setWindowTitle("Программа анализа видео на ютуб")
        self.setStyleSheet(CONST_STYLE_WINDOW)
        self.setWindowIcon(QIcon("Image\icon.jpg"))
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Выберите нужный вам файл Exel")
        instructions_1 = QLabel(text="В нем должны быть ссылки на видео")
        
        select_file = QPushButton(text="Выбрать файл")
        select_file.clicked.connect(self.file_selection)
        
        control_UI.addWidget(instructions)
        control_UI.addWidget(instructions_1)
        control_UI.addWidget(select_file)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def file_selection(self):
        self.file_path = filedialog.askopenfilename(
                title="Выберите файл",
                filetypes=[("Exel", "*.xlsx"), ("Все файлы", "*.*")]
                )