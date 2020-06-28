import sys  # sys нужен для передачи argv в QApplication
import os
import numbersGUI # import my gui file
from PyQt5 import QtWidgets

class NumbersApp(QtWidgets.QMainWindow, numbersGUI.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.learn)
        self.pushButton_3.clicked.connect(self.activate)

    def clear(self):
        self.textEdit.setText('clear')

    def learn(self):
        self.textEdit.setText('learn')

    def activate(self):
        self.textEdit.setText('Activate')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = NumbersApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()