import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget


class CircleWindow(QMainWindow):
    def __init__(self):
        """Интерфейс примитивный, смысла в UI.ui нет"""
        super().__init__()
        self.setWindowTitle("Окружность")
        self.resize(674, 623)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.horizontalLayout = QHBoxLayout(central_widget)

        self.pushButton = QPushButton(self)
        self.pushButton.setMaximumSize(100, 16777215)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.setText('кнопочъка')
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for _ in range(1000):
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 100))
            painter.setBrush(color)
            pos = QPoint(randint(1, 2000), randint(1, 2000))
            radius = randint(1, 30)
            painter.drawEllipse(pos, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec_())