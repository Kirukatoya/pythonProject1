import math

from PySide2 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5 import uic

#import pro
#from ui_pro import *

qt_creator = "pro.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        #self.ui = Ui_MainWindow()
        self.setupUi(self)

        # установить event filter для кнопок
        self.HelpBtn.installEventFilter(self)
        self.HomeBtn.installEventFilter(self)
        self.InformationBtn.installEventFilter(self)
        self.NewTaskBtn.installEventFilter(self)
        self.OkBtn.installEventFilter(self)

        self.HumansPerHour.installEventFilter(self)




        # Создаем QWidget для отображения
        #self.help_widget = QWidget()
        #self.home_widget = QWidget()
        #self.information_widget = QWidget()
        #self.new_task2_widget = QWidget()

        # Добавляем QWidget в QStackedWidget
        #self.stackedWidget.addWidget(self.help_widget)
        #self.stackedWidget.addWidget(self.information_widget)
        #self.stackedWidget.addWidget(self.new_task_widget)
        #self.stackedWidget.addWidget(self.new_task2_widget)

        #self.show()


    def eventFilter(self, source, event):
        if source == self.HelpBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(1)
            print("HelpBtn event filter")

        if source == self.NewTaskBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(3)
            print("NewTaskBtn event filter")

        if source == self.InformationBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(2)
            print("InformationBtn event filter")

        if source == self.HomeBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(0)
            print("HomeBtn event filter")

        if source == self.OkBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(4)
            print("OkBtn event filter")
            self.OkBtn.clicked.connect(self.ras)

        if source == self.HumansPerHour and event.type() == QtCore.QEvent.MouseButtonPress:
            print("нажал")

        return super().eventFilter(source, event)


    def click(self):
        print("нажитие")

    def ras(self):
        # Получение введенных данных
        per_hour = float(self.lineEdit_7.text())
        service_channels = int(self.lineEdit_6.text())
        service_intensity = float(self.lineEdit_5.text())
        service_time = float(self.lineEdit_8.text())
        print("xb", per_hour)

        # Расчет показателей
        # Нагрузка системы
        system_load = per_hour / service_intensity

        # Вероятность простоя системы
        idle_probability = (1 + sum([(system_load ** i / math.factorial(i) for i in range(1, service_channels + 1))]) + (system_load ** (service_channels + 1) / math.factorial(service_channels) * (service_channels - system_load)) ** -1)

        # Вероятность образования очереди
        poch = ((idle_probability**(service_channels+1)) / math.factorial(service_channels) * (service_channels - idle_probability))

        # Средняя длина очереди
        avg_queue_length = (service_channels / service_channels - service_intensity) * poch

        # Среднее время ожидания в очереди
        avg_waiting_time = avg_queue_length / per_hour

        # Среднее число занятых каналолов
        avg_number_channels = system_load

        # Среднее время прибывания в системе
        sistem_time = avg_waiting_time + service_time

        # Вставка рассчитанных показателей
        self.lineEdit.setText(str(idle_probability))
        self.lineEdit_2.setText(str(avg_queue_length))
        self.lineEdit_3.setText(str(avg_waiting_time))
        self.lineEdit_4.setText(str(system_load))
        self.lineEdit_10.setText(str(poch))
        self.lineEdit_11.setText(str(avg_number_channels))
        self.lineEdit_12.setText(str(sistem_time))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #window = MainWindow()
    sys.exit(app.exec_())
