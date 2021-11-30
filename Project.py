import sys
import random
import urllib.request

from PyQt5.QtCore import  QCoreApplication
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget,
                             QTextEdit,QApplication)
from PyQt5.QtGui import QPixmap
from datetime import datetime

from gamedb import GameDB


class AimGame(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title = QLabel('AIM GAME', self)
        self.target = QLabel('Target', self)
        self.startBtn = QPushButton(self)
        self.startBtn.setText("start")
        self.targetEdit = QLineEdit(self)

        url = "https://animrefdotcom.files.wordpress.com/2019/04/capture.jpg?w=400&h=200&crop=1"
        img = urllib.request.urlopen(url).read()
        self.img_lab = QLabel(self)
        self.img_lab.resize(400, 200)

        pixmap = QPixmap()
        pixmap.loadFromData(img)
        self.img_lab.setPixmap(pixmap)
        self.img_lab.move(50, 270)

        titleFont = self.title.font()
        titleFont.setPointSize(40)
        self.title.setFont(titleFont)
        self.title.move(120, 100)
        self.target.move(150, 200)
        self.startBtn.move(220, 230)
        self.targetEdit.move(200, 200)
        self.startBtn.clicked.connect(self.buttonClicked)

        self.setGeometry(600, 400, 500, 500)
        self.setWindowTitle('AIM-GAME')
        self.center()
        self.show()

        self.num = 1

    def buttonClicked(self):
        try:
            self.num_count = int(self.targetEdit.text())
            self.start_time = datetime.now()
            self.title.hide()
            self.targetEdit.hide()
            self.target.hide()
            self.startBtn.hide()
            self.img_lab.hide()

            self.aimBtn = QPushButton(self)
            self.aimBtn.setText("AIM")
            self.aimBtn.resize(50, 50)
            self.aimBtn.setStyleSheet("color: red;"
                                      "border-style: solid;"
                                      "border-width: 2px;"
                                      "border-color: #FA8072;"
                                      "border-radius: 3px")
            self.aimBtn.move(random.randrange(1, 450), random.randrange(1, 450))
            self.aimBtn.show()
            self.aimBtn.clicked.connect(aim.game)
        except:
            QMessageBox.about(self, 'Message', '숫자를 입력하세요.')

    def game(self):
        self.aimBtn.move(random.randrange(1, 450), random.randrange(1, 450))
        self.aimBtn.show()

        if (self.num < self.num_count):
            self.num += 1
        else:
            self.aimBtn.hide()
            fin_time = datetime.now()
            self.total_time = round((fin_time - self.start_time).total_seconds(), 3)

            self.clear = QLabel('', self)
            self.clear.setStyleSheet("color: green;"
                                     "background-color: #7FFFD4")
            self.clear.setText("Clear Time : " + str(self.total_time))
            targetFont = self.clear.font()
            targetFont.setPointSize(30)
            self.clear.setFont(targetFont)
            self.clear.move(100, 200)
            self.clear.show()
            aim.exercise()

    def exercise(self):
        self.tryBtn = QPushButton(self)
        self.quitBtn = QPushButton(self)
        self.textedit = QTextEdit(self)

        self.textedit.move(50, 300)
        self.textedit.resize(400, 150)

        self.tryBtn.setText("Again")
        self.tryBtn.move(150, 250)
        self.tryBtn.show()
        self.quitBtn.setText("Quit")
        self.quitBtn.move(300, 250)
        self.quitBtn.show()
        aim.record()

        self.textedit.show()

        self.tryBtn.clicked.connect(self.again)
        self.quitBtn.clicked.connect(QCoreApplication.instance().quit)

    def again(self):
        self.tryBtn.clicked.connect(QCoreApplication.instance().quit)
        aim.__init__()

    def record(self):
        game = GameDB()
        scdb = game.readGameDB()
        record = {'TargetNumber': str(self.num_count), 'clearTime': str(self.total_time)}
        scdb += [record]
        game.writeGameDB(scdb)
        aim.showGameDB(scdb)

    def showGameDB(self, scdb):  # all student information print
        for p in scdb:
            self.textedit.append("Target Number: " + str(p.get('TargetNumber')) + " Clear Time: " + p.get('clearTime'))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aim = AimGame()
    sys.exit(app.exec_())
