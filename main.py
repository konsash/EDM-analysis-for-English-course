import sys

from PyQt6 import QtCore, QtWidgets
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class Ui_MainWindow:
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setStyleSheet("QWidget{background-color: rgba(33, 193, 255, 50);}")
        self.open_file = False
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 20, 250, 20))
        self.label_1.setText("Введите минимальное возможное значение")
        self.label_1.setStyleSheet("background-color: none;")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 45, 250, 20))
        self.label_2.setText("Введите максимальное возможное значение")
        self.label_2.setStyleSheet("background-color: none;")

        self.min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min.setValue(0)
        self.min.setRange(-1000000000000000000, 1000000000000000000)
        self.min.setGeometry(QtCore.QRect(280, 20, 100, 20))
        self.min.setStyleSheet("background-color: none;")
        self.max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max.setValue(100)
        self.max.setRange(-1000000000000000000, 1000000000000000000)
        self.max.setGeometry(QtCore.QRect(280, 45, 100, 20))
        self.max.setStyleSheet("background-color: none;")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 20, 150, 20))
        self.label_3.setText("Выберите файл .csv")
        self.label_3.setStyleSheet("background-color: none;")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 45, 150, 20))
        self.label_4.setText("Выберите столбец файла")
        self.label_4.setStyleSheet("background-color: none;")

        self.column = QtWidgets.QSpinBox(self.centralwidget)
        self.column.setValue(1)
        self.column.setRange(0, 100)
        self.column.setGeometry(QtCore.QRect(560, 45, 40, 20))
        self.column.setStyleSheet("background-color: none;")
        self.fio_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fio_btn.setGeometry(QtCore.QRect(560, 20, 23, 23))
        self.fio_btn.setText("📂")
        self.fio_btn.clicked.connect(lambda: self.handle_fio_btn())
        self.fio_btn.setStyleSheet("background-color: none;")

        self.a_ot_field = QtWidgets.QTextEdit(self.centralwidget)
        self.a_ot_field.setGeometry(QtCore.QRect(20, 95, 190, 495))
        self.a_ot_field.setReadOnly(True)
        self.a_ot_field.setStyleSheet("background-color: none;")

        self.begin_btn = QtWidgets.QPushButton(self.centralwidget)
        self.begin_btn.setGeometry(QtCore.QRect(250, 70, 100, 20))
        self.begin_btn.setText("Сделать прогноз")
        self.begin_btn.setStyleSheet("background-color: none;")

        self.label_graf = QtWidgets.QLabel(self.centralwidget)
        self.label_graf.setGeometry(QtCore.QRect(220, 95, 570, 495))
        self.label_graf.setStyleSheet("background-color: none;")
        self.lay = QtWidgets.QGridLayout(self.label_graf)
        self.plot_graph = pg.PlotWidget()
        self.lay.addWidget(self.plot_graph)

    def handle_fio_btn(self) -> None:
        """
        Метод обрабатывающий кнопку открытия файлового менеджера.
        Позволяет пользователю выбрать текстовый файл для кодирования
        его содержимого.
        """

        file_dialog = QFileDialog(self.MainWindow, "Выберите файл", "",
                                  "csv файлы (*.csv)")

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                file_path = selected_files[0]
                with open(file_path, "r", encoding="utf-8") as file:
                    file_contents = file.read()
                    self.a_ot_field.setPlainText(file_contents)
        self.open_file = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    Ui_MainWindow(MainWindow)
    MainWindow.show()
    app.exec()
