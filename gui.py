import sys  # sys нужен для передачи argv в QApplication
import os
import numbersGUI # import my gui file

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QBrush, QPen, QPainter, QPolygon, QPixmap, QImage, QColor
from PyQt5.QtCore import QPoint, Qt

class NumbersApp(QtWidgets.QMainWindow, numbersGUI.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.learn)
        self.pushButton_3.clicked.connect(self.activate)

        self.horizontalSlider.setValue(0)
        self.horizontalSlider_2.setValue(0)
        self.horizontalSlider_3.setValue(0)
        self.horizontalSlider_4.setValue(0)
        self.horizontalSlider_5.setValue(0)
        self.horizontalSlider_6.setValue(0)
        self.horizontalSlider_7.setValue(0)
        self.horizontalSlider_8.setValue(0)
        self.horizontalSlider_9.setValue(0)
        self.horizontalSlider_10.setValue(0)

        self.scene = QGraphicsScene()
        view = QGraphicsView(self.scene, self)
        view.setGeometry(0,0,400,400)
        self.drawRect(0,0,400,400)

    def drawRect(self, x1, y1, x2, y2):
        redBrush = QBrush(Qt.red)
        blackPen = QPen(Qt.black)
        #ellipse = self.scene.addRect(x1, y1, x2, y2, blackPen, redBrush)

        width, height = 400, 400
        im = QImage(width, height, QImage.Format_ARGB32)

        for x in range(im.width()):
            for y in range(im.height()):
                im.setPixel(x, y, QColor(255, x/4 * 2.56, y/4 * 2.56, 255).rgb())

        self.scene.addPixmap(QPixmap.fromImage(im))


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