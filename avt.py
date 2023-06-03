

from PySide2 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit

from ui_pro import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # установить event filter для кнопок
        self.ui.HelpBtn.installEventFilter(self)
        self.ui.HomeBtn.installEventFilter(self)
        self.ui.InformationBtn.installEventFilter(self)
        self.ui.NewTaskBtn.installEventFilter(self)
        self.ui.OkBtn.installEventFilter(self)
        # self.ui.HumansPerHour.




        # Создаем QWidget для отображения
        self.help_widget = QWidget()
        self.home_widget = QWidget()
        self.information_widget = QWidget()
        self.new_task_widget = QWidget()
        self.new_task2_widget = QWidget()





        # Добавляем QWidget в QStackedWidget
        self.ui.stackedWidget.addWidget(self.help_widget)
        self.ui.stackedWidget.addWidget(self.home_widget)
        self.ui.stackedWidget.addWidget(self.information_widget)
        self.ui.stackedWidget.addWidget(self.new_task_widget)
        self.ui.stackedWidget.addWidget(self.new_task2_widget)



        self.show()


    def eventFilter(self, source, event):
        if source == self.ui.HelpBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.ui.stackedWidget.setCurrentIndex(1)
            print("HelpBtn event filter")

        if source == self.ui.NewTaskBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.ui.stackedWidget.setCurrentIndex(3)
            print("NewTaskBtn event filter")

        if source == self.ui.InformationBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.ui.stackedWidget.setCurrentIndex(2)
            print("InformationBtn event filter")

        if source == self.ui.HomeBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.ui.stackedWidget.setCurrentIndex(0)
            print("HomeBtn event filter")

        if source == self.ui.OkBtn and event.type() == QtCore.QEvent.MouseButtonPress:
            self.ui.stackedWidget.setCurrentIndex(4)
            print("OkBtn event filter")



        return super().eventFilter(source, event)


    def show_help(self):
        # Переключаемся на нужный QWidget при нажатии на кнопку HelpBtn
        self.ui.stackedWidget.setCurrentWidget(self.help_widget)

    def show_home(self):
        # Переключаемся на нужный QWidget при нажатии на кнопку
        self.ui.stackedWidget.setCurrentWidget(self.home_widget)

    def show_informstion(self):
        # Переключаемся на нужный QWidget при нажатии на кнопку
        self.ui.stackedWidget.setCurrentWidget(self.information_widget)

    def show_new_task(self):
        # Переключаемся на нужный QWidget при нажатии на кнопку
        self.ui.stackedWidget.setCurrentWidget(self.new_task_widget)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
