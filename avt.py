import math
from PyQt5.QtGui import QDoubleValidator
from PySide2 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

# import pro
# from ui_pro import *

qt_creator = "pro.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        validator = QDoubleValidator()
        self.lineEdit_7.setValidator(validator)
        self.lineEdit_6.setValidator(validator)
        self.lineEdit_8.setValidator(validator)

        # установить event filter для кнопок
        self.HelpBtn.installEventFilter(self)
        self.HomeBtn.installEventFilter(self)
        self.InformationBtn.installEventFilter(self)
        self.NewTaskBtn.installEventFilter(self)
        self.OkBtn.installEventFilter(self)
        self.clearBtn.installEventFilter(self)
        self.backBtn.installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.HelpBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(1)
            print("HelpBtn event filter")

        if source == self.NewTaskBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(3)
            self.clearr()
            print("NewTaskBtn event filter")

        if source == self.InformationBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(2)
            print("InformationBtn event filter")

        if source == self.HomeBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(0)
            print("HomeBtn event filter")

        if source == self.OkBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            if self.lineEdit_7.text() and self.lineEdit_6.text() and self.lineEdit_8.text():
                self.stackedWidget.setCurrentIndex(4)
                self.ras()

            else:
                print("Пожалуйста заполните поля ввода")

                self.textEdit_9.setText("\n\n\n\n\n\n  Пожалуйста заполните поля ввода")
                # self.textEdit_9.setVisible(not self.textEdit_9.isVisible())

            print("OkBtn event filter")
        if source == self.clearBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.clearr()
            print("clearBtn event filter")

        if source == self.backBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.stackedWidget.setCurrentIndex(3)
            print("backBtn event filter")

        return super().eventFilter(source, event)

    def ras(self):
        # Получение введенных данных
        per_hour = float(self.lineEdit_7.text())
        service_channels = int(self.lineEdit_6.text())
        service_time = float(self.lineEdit_8.text())
        per_hour = per_hour / 60
        print(per_hour)
        # Расчет показателей
        service_intensity = (1 / service_time)
        print(service_intensity)

        # Нагрузка системы
        system_load = per_hour / service_intensity
        if system_load / service_channels < 1:
            print("нагрузка системы", system_load)

            # Вероятность простоя системы

            def calculate_idle_probability(system_load, service_channels):
                idle_probability = 1

                for i in range(service_channels + 1):
                    idle_probability += (system_load ** i) / math.factorial(i)

                idle_probability += (system_load ** (service_channels + 1)) / (
                        math.factorial(service_channels) * (service_channels - system_load))

                return (1 / idle_probability)

            idle_probability = round((calculate_idle_probability(system_load, service_channels)), 3)
            print("Веростность простоя системы", idle_probability, "%")

            # Вероятность образования очереди
            poch = round((((system_load ** (service_channels + 1)) / (
                    math.factorial(service_channels) * (service_channels - system_load))) * idle_probability), 2)
            print("Вероятность образования очереди", poch)

            # Средняя число заявок в очереди
            avg_queue_length = round((((system_load ** (service_channels + 1)) / (
                    service_channels * math.factorial(service_channels) * (
                    1 - (system_load / service_channels)) ** 2)) * idle_probability), 2)
            print("Средняя число заявок в очереди", avg_queue_length)

            # Среднее время ожидания в очереди
            avg_waiting_time = round((avg_queue_length / per_hour), 2)
            print("Среднее время ожидания в очереди", avg_waiting_time)

            # Среднее число занятых каналолов
            avg_number_channels = system_load
            print("Число занятых каналов", avg_number_channels)

            # Среднее время прибывания в системе
            sistem_time = avg_waiting_time + service_time
            print("Среднее время прибывания в системе", sistem_time)

            # Коэфициэнт занятых обслуживанием каналов
            kof = round((system_load / service_channels), 2)
            print("Коэффициэнт занятых обслуживанием каналов", kof)

            idle_probability = idle_probability * 100
            poch = poch * 100

            # Вставка рассчитанных показателей
            self.lineEdit.setText(str(idle_probability) + "%")
            self.lineEdit_2.setText(str(avg_queue_length))
            self.lineEdit_3.setText(str(avg_waiting_time) + " минут")
            self.lineEdit_4.setText(str(system_load))
            self.lineEdit_10.setText(str(poch) + "%")
            self.lineEdit_11.setText(str(avg_number_channels))
            self.lineEdit_12.setText(str(sistem_time) + " минут")
            self.lineEdit_5.setText(str(kof))
            if poch > 70:
                self.textEdit.setText("Вам необходимо увеличить кол-во каналов обслуживания, так как показатель среднего числа занятых каналов "
                                      "указывает на то, что система справляется, но слишком загружена."
                                      "\nТак же вероятность образования очереди слишком большая, что негативно скажется на посетителях."
                                      "\nКоэффициент занятых обслуживанием каналов также указывает на большую загрузку системы."
                                      "\n\nНагрузка системы: Показывает среднее количество запросов, поступающих в систему за единицу времени."
                                      "\n\nВероятность простоя системы: Вероятность того, что все каналы обслуживания будут свободны в определенный момент времени."
                                      "\n\nСреднее время ожидания в очереди: Показывает ожидаемое время, которое запросы проводят в очереди перед обслуживанием. "
                                      "Если среднее время ожидания слишком высоко, это может указывать на необходимость оптимизации системы или "
                                      "добавления ресурсов для ускорения обработки запросов.")

            elif poch > 50:
                self.textEdit.setText("Показатель среднего числа занятых каналов "
                                      "указывает на то, что система справляется с потоком посетителей."
                                      "\nВероятность образования очереди указывает на отличное функционирование системы."
                                      "\nКоэффициент занятых обслуживанием каналов также указывает на хорошую работу."
                                      "\n\nНагрузка системы: Показывает среднее количество запросов, поступающих в систему за единицу времени."
                                      "\n\nВероятность простоя системы: Вероятность того, что все каналы обслуживания будут свободны в определенный момент времени."
                                      "\n\nСреднее время ожидания в очереди: Показывает ожидаемое время, которое запросы проводят в очереди перед обслуживанием. "
                                      "Если среднее время ожидания слишком высоко, это может указывать на необходимость оптимизации системы или "
                                      "добавления ресурсов для ускорения обработки запросов.")
            elif poch < 50:
                self.textEdit.setText("Вам необходимо уменьшить кол-во каналов обслуживания, так как показатель среднего числа занятых каналов"
                                      "указывает на то, что используются не все каналы обслуживания."
                                      "\nТак же вероятность образования очереди слишком мала, что также говорит о том, что в системе слишком много "
                                      "каналов обслуживания."
                                      "\nКоэффициент занятых обслуживанием каналов также указывает на недостаточную нагрузку."
                                      "\n\nНагрузка системы: Показывает среднее количество запросов, поступающих в систему за единицу времени."
                                      "\n\nВероятность простоя системы: Вероятность того, что все каналы обслуживания будут свободны в определенный момент времени."
                                      "\n\nСреднее время ожидания в очереди: Показывает ожидаемое время, которое запросы проводят в очереди перед обслуживанием. "
                                      "Если среднее время ожидания слишком высоко, это может указывать на необходимость оптимизации системы или "
                                      "добавления ресурсов для ускорения обработки запросов.")











    def clearr(self):
        self.lineEdit_7.clear()
        self.lineEdit_6.clear()
        self.lineEdit_8.clear()
        self.textEdit_9.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window = MainWindow()
    sys.exit(app.exec_())
