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

        self.username = "unknown"
        self.lineEdit = QLineEdit()

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

        self.game.initializeGameScore()

    def scoresPage(self):
        # add buttons for scores page
        backButton = QPushButton("Back")
        backButton.setStyleSheet(buttonStyle)
        backButton.clicked.connect(self.homePage)

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)

        # add widgets
        wrapperScoreV = QVBoxLayout()
        wrapperScoreV.setContentsMargins(20, 120, 0, 0)
        _, keys, values = self.game.getScores()
        numScoresToPlot = min(15, len(keys))
        for rank in range(numScoresToPlot):
            wrapperScoreH = QHBoxLayout()
            labelName = QLabel(keys[rank])
            labelName.setFont(QFont('Arial', 26))
            labelScore = QLabel(values[rank])
            labelScore.setFont(QFont('Arial', 26))
            wrapperScoreH.addWidget(labelName)
            wrapperScoreH.addWidget(labelScore)
            wrapperScoreH.addStretch(1)
            wrapperScoreV.addLayout(wrapperScoreH)

        vbox.addLayout(wrapperScoreV)
        vbox.addStretch()
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
        # add buttons for game page
        hitButton = QPushButton("Hit")
        hitButton.setStyleSheet(buttonStyle)
        hitButton.clicked.connect(self.hitEvent)

        standButton = QPushButton("Stand")
        standButton.setStyleSheet(buttonStyle)
        standButton.clicked.connect(self.standEvent)

        splitButton = QPushButton("Split")
        splitButton.setStyleSheet(buttonStyle)
        splitButton.clicked.connect(self.splitEvent)

        leaveButton = QPushButton("Leave")
        leaveButton.setStyleSheet(buttonStyle)
        leaveButton.clicked.connect(self.leavePage)

        # add players name
        labelDealer = QLabel("Dealer")
        labelDealer.setFont(QFont('Arial', 26))
        labelDealer.setStyleSheet(
            "padding:5px 20px; color: white; background-color:rgb(43, 43, 43); border-radius:20px")
        labelPlayer = QLabel("You")
        labelPlayer.setFont(QFont('Arial', 26))
        labelPlayer.setStyleSheet(
            "padding:5px 20px; color: white; background-color:rgb(43, 43, 43); border-radius:20px")

        # game
        self.game.dealerTurn()
        card = self.game.dealerHand.getLastCard()
        cardDrawing = QLabel()
        cardDrawing.setFixedSize(167, 225)
        cardDrawing.setStyleSheet(
            "border-image: url({})".format(card.getCardFile()))

        self.game.playerTurn()
        card = self.game.playerHand.getLastCard()
        cardDrawing2 = QLabel()
        cardDrawing2.setFixedSize(167, 225)
        cardDrawing2.setStyleSheet(
            "border-image: url({})".format(card.getCardFile()))

        self.game.playerTurn()
        card = self.game.playerHand.getLastCard()
        cardDrawing3 = QLabel()
        cardDrawing3.setFixedSize(167, 225)
        cardDrawing3.setStyleSheet(
            "border-image: url({})".format(card.getCardFile()))

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)

        # add widgets
        wrapperGameV = QVBoxLayout()
        wrapperGameDealer = QHBoxLayout()
        wrapperGamePlayer = QHBoxLayout()

        # label Dealer
        wrapperGameV.addWidget(labelDealer, alignment=Qt.AlignCenter)
        # cards Dealer
        wrapperGameDealer.addStretch()
        wrapperGameDealer.addWidget(cardDrawing)
        wrapperGameDealer.addStretch()
        wrapperGameV.addLayout(wrapperGameDealer)
        wrapperGameV.addStretch()

        # cards player
        wrapperGamePlayer.addStretch()
        wrapperGamePlayer.addWidget(cardDrawing2)
        wrapperGamePlayer.addWidget(cardDrawing3)
        wrapperGamePlayer.addStretch()
        wrapperGameV.addLayout(wrapperGamePlayer)
        # label player
        wrapperGameV.addWidget(labelPlayer, alignment=Qt.AlignCenter)

        vbox.addLayout(wrapperGameV)
        vbox.addLayout(hbox)

        hbox.addWidget(hitButton)
        hbox.addWidget(standButton)
        hbox.addWidget(splitButton)
        hbox.addWidget(leaveButton)

        widget = QWidget()

        # set the background image as the game page
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond table.PNG)")

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def updateGamePage(self):
        pass

    def hitEvent(self):
        pass

    def standEvent(self):
        pass

    def splitEvent(self):
        pass

    def winPage(self):
        # add buttons for win page
        continueButton = QPushButton("Continue")
        continueButton.setStyleSheet(buttonStyle)
        continueButton.clicked.connect(self.gamePage)

        leaveButton = QPushButton("Leave")
        leaveButton.setStyleSheet(buttonStyle)
        leaveButton.clicked.connect(self.leavePage)

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox.addWidget(continueButton)
        hbox.addWidget(leaveButton)

        widget = QWidget()

        # set the background image for leaving the game
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond gagne.PNG)")

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.game.updateScorePlayer()
        self.game.resetHands()

    def lostPage(self):
        # add buttons for win page
        continueButton = QPushButton("Continue")
        continueButton.setStyleSheet(buttonStyle)
        continueButton.clicked.connect(self.gamePage)

        leaveButton = QPushButton("Leave")
        leaveButton.setStyleSheet(buttonStyle)
        leaveButton.clicked.connect(self.leavePage)

        # layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        hbox.addWidget(continueButton)
        hbox.addWidget(leaveButton)

        widget = QWidget()

        # set the background image for leaving the game
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond perdu.PNG)")

        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.game.updateScoreDealer()
        self.game.resetHands()

    def leavePage(self):
        # add buttons for game page
        confirmButton = QPushButton("Confirm")
        confirmButton.setStyleSheet(buttonStyle)

        # add widgets
        label = QLabel("Enter your name:")
        label.setFont(QFont('Arial', 26))

        self.lineEdit.setStyleSheet(
            "padding:5px 10px")

        # layout
        wrapperLE = QVBoxLayout()
        wrapperLE.setContentsMargins(500, 50, 250, 650)
        wrapperLE.addStretch()
        wrapperLE.addWidget(label, alignment=Qt.AlignTop)
        wrapperLE.addWidget(self.lineEdit, alignment=Qt.AlignTop)
        wrapperLE.addWidget(confirmButton, alignment=Qt.AlignTop)

        widget = QWidget()

        # set the background image for leaving the game
        background = QLabel(widget)
        background.setFixedSize(1136, 850)
        background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond au revoir.PNG)")

        widget.setLayout(wrapperLE)
        self.setCentralWidget(widget)

        confirmButton.clicked.connect(self.registerUser)

    def registerUser(self):
        if self.lineEdit.text() != "":
            self.username = self.lineEdit.text()
        sys.exit()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
