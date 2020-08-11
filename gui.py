import sys
import os
import numbersGUI # import my gui file
import random
import settings
from numbersNetwork import Network

from datetime import datetime
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QBrush, QPen, QPainter, QPolygon, QPixmap, QImage, QColor
from PyQt5.QtCore import QPoint, Qt

class NumbersApp(QtWidgets.QMainWindow, numbersGUI.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле gui
        super().__init__()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setMouseTracking(True)

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
        self.textEdit.setText('1')

        #draw field
        self.scene = QGraphicsScene()
        view = QGraphicsView(self.scene, self)
        view.viewport().installEventFilter(self)
        width, height = settings.fieldWidth, settings.fieldWidth
        view.setGeometry(0, 0, width, height)
        self.initImage(width-5, height-5)

        settings.pixelWidth = 20
        settings.pixelHeight = 20

        #init field
        self.field = [[0] * settings.pixelWidth for i in range(settings.pixelHeight)]
        self.draw()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove and (event.buttons() == QtCore.Qt.LeftButton or event.buttons() == QtCore.Qt.RightButton):
            pos = event.pos()
            x = pos.x() / settings.pixelWidth
            y = pos.y() / settings.pixelHeight

        if event.type() == QtCore.QEvent.MouseMove:
            if event.buttons() == QtCore.Qt.NoButton:
                pass
                #print("Simple mouse motion")
            elif event.buttons() == QtCore.Qt.LeftButton:
                try:
                    self.field[int(y)][int(x)] = 1
                    self.field[int(y) + 1][int(x)+1] = 1
                    self.field[int(y)][int(x) + 1] = 1
                    self.field[int(y) + 1][int(x)] = 1

                    self.putPixel(int(x), int(y))
                    self.putPixel(int(x) + 1, int(y) + 1)
                    self.putPixel(int(x), int(y) + 1)
                    self.putPixel(int(x) + 1, int(y))
                except Exception:
                    pass

            elif event.buttons() == QtCore.Qt.RightButton:
                try:
                    self.field[int(y)][int(x)] = 0
                    self.field[int(y) + 1][int(x)+1] = 0
                    self.field[int(y)][int(x) + 1] = 0
                    self.field[int(y) + 1][int(x)] = 0

                    self.putPixel(int(x), int(y), 0)
                    self.putPixel(int(x) + 1, int(y) + 1, 0)
                    self.putPixel(int(x), int(y) + 1, 0)
                    self.putPixel(int(x) + 1, int(y), 0)
                except Exception:
                    pass

        elif event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                pass
                #print("Press!")
        return super(NumbersApp, self).eventFilter(source, event)


    def draw(self):
        pixelInRow = int(settings.fieldWidth / settings.pixelWidth)
        pixelInColumn = int(settings.fieldHeight / settings.pixelHeight)
        for i in range(pixelInRow):
            for j in range(pixelInColumn):
                if self.field[i][j] == 1:
                    self.putPixel(i, j)
                if self.field[i][j] == 0:
                    self.putPixel(i, j, 0)

    def putPixel(self, x, y, color=1):
        for i in range(x * settings.pixelWidth, x * settings.pixelWidth + settings.pixelWidth):
            for j in range(y * settings.pixelHeight, y * settings.pixelHeight + settings.pixelHeight):
                if i <= 394 and j <= 394:
                    if color == 1:
                        self.image.setPixel(i, j, QColor(0, 0, 0, 0).rgb())
                    elif color == 0:
                        self.image.setPixel(i, j, QColor(255, 255, 255, 255).rgb())
                    else:
                        self.image.setPixel(i, j, QColor(255, 255, 255, 255).rgb())

        self.scene.addPixmap(QPixmap.fromImage(self.image))

    def initImage(self, width, height):
        self.image = QImage(width, height, QImage.Format_ARGB32)

        red = 255
        green = 255
        blue = 255

        for x in range(self.image.width()):
            for y in range(self.image.height()):
                self.image.setPixel(x, y, QColor(red, green, blue, 255).rgb())

        self.scene.addPixmap(QPixmap.fromImage(self.image))



    def click(self):
        self.textEdit.setText('CLICK')
    def clear(self):
        for i in range(20):
            for j in range(20):
                self.field[i][j] = 0
        self.draw()

    def learn(self):
        #self.image_save()
        number = self.textEdit.toPlainText()
        Network.addSample(self.field, number)

    def activate(self):
        Network.activate(self.field)

    def image_save(self):
        now = datetime.now()
        nowFormatted = now.strftime("%d_%m_%Y")
        number = self.textEdit.toPlainText()
        self.image.save('samples/' + number + '/' +
                        number + '_' +
                        str(datetime.timestamp(now)) + '_' +
                        str(nowFormatted) + '.jpg','JPG'
                        )

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = NumbersApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()