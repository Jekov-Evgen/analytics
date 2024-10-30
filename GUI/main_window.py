from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QWidget, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon
from DataProcessing import getting_data_from_links
from GUI.style import CONST_STYLE_WINDOW

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(350, 250)
        self.setWindowTitle("Программа анализа видео на ютуб")
        self.setStyleSheet(CONST_STYLE_WINDOW)
        self.setWindowIcon(QIcon("Image\icon.jpg"))
        
        self.error = None
        
        control_UI = QVBoxLayout()
        size_control = QHBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите ссылки на ваши видео через: ")
        allocation = QLabel(text="';'")
        allocation.setObjectName('allocation')
        self.entering_links = QLineEdit()
        
        start_of_analysis = QPushButton(text="Провести анализ")
        start_of_analysis.clicked.connect(self.file_selection)
        
        size_control.addWidget(instructions)
        size_control.addWidget(allocation)
        
        control_UI.addLayout(size_control)
        control_UI.addWidget(self.entering_links)
        control_UI.addWidget(start_of_analysis)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def file_selection(self):
        try:
            receiving_data = str(self.entering_links.text()).split(';')
            
            getting_data_from_links(receiving_data)
        except:
            self.error = QMessageBox()
            self.error.setWindowTitle("Ошибка ввода")
            self.error.setText("Вы совершили ошибку ввода")
            self.error.show()