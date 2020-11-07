import sys

from utils.game import Game
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

buttonStyle = """
                QPushButton {
                    font-size: 26px;
                    width: 100px;
                    border-radius: 10px;
                    border-style: outset;
                    background: white;
                    padding: 5px;
                }

                QPushButton:hover {
                    background: qradialgradient(
                        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
                        radius: 1.35, stop: 0 #fff, stop: 1 #bbb
                    );
                }
              """


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.game = Game()

        # window
        self.setWindowTitle("Black Jack ++")
        self.setFixedSize(1136, 850)

        # launch
        self.homePage()
        self.show()

    def homePage(self):
        # add buttons for home page
        rulesButton = QPushButton("Rules")
        rulesButton.setStyleSheet(buttonStyle)
        rulesButton.clicked.connect(self.rulesPage)

        scoreButton = QPushButton("Scores")
        scoreButton.setStyleSheet(buttonStyle)
        scoreButton.clicked.connect(self.scoresPage)

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox.addWidget(rulesButton)
        hbox.addWidget(scoreButton)

        widget = QWidget()

        # set the background image as the home page
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond_acceuil.png)")

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def rulesPage(self):
        # add buttons for rules page
        playButton = QPushButton("Play")
        playButton.setStyleSheet(buttonStyle)
        playButton.clicked.connect(self.gamePage)

        backButton = QPushButton("Back")
        backButton.setStyleSheet(buttonStyle)
        backButton.clicked.connect(self.homePage)

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox.addWidget(playButton)
        hbox.addWidget(backButton)

        widget = QWidget()

        # set the background image as the rules page
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond regle.PNG)")

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def scoresPage(self):
        # add buttons for scores page
        backButton = QPushButton("Back")
        backButton.setStyleSheet(buttonStyle)
        backButton.clicked.connect(self.homePage)

        # add scores data
        _, keys, values = self.game.getScores()
        numScoresToPlot = min(5, len(keys))
        for rank in range(numScoresToPlot):
            labelName = QLabel(keys[rank])
            labelName.setFont(QFont('Arial', 26))
            labelScore = QLabel(values[rank])
            labelScore.setFont(QFont('Arial', 26))

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox.addWidget(backButton)

        widget = QWidget()

        # set the background image as the scores page
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond score.PNG)")

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def gamePage(self):
        # set the background image as the game page
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond table.PNG)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)

        self.leaveButton.clicked.connect(self.leavePage)
        labelDealer = QLabel("Dealer")
        labelDealer.setFont(QFont('Arial', 26))
        labelPlayer = QLabel("You")
        labelPlayer.setFont(QFont('Arial', 26))

        self.hbox.addWidget(labelDealer, alignment=QtCore.Qt.AlignLeft)
        self.hbox.addWidget(labelPlayer, alignment=QtCore.Qt.AlignRight)

        self.hbox.addWidget(self.hitButton)
        self.hbox.addWidget(self.standButton)
        self.hbox.addWidget(self.splitButton)
        self.hbox.addWidget(self.leaveButton)

    def leavePage(self):
        # set the background image for leaving the game
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond au revoir.PNG)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)


def clearLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                clearLayout(item.layout())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
