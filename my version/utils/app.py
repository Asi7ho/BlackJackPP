import sys

from .game import Game
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton

buttonStyle = """
                QPushButton {
                    font-size: 26px;
                    width: 75px;
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


class App:
    def __init__(self):
        self.app = QApplication([])
        self.game = Game()

        # window
        self.window = QWidget()
        self.window.setWindowTitle("Black Jack")
        self.window.setFixedSize(1136, 850)

        # background
        self.background = QLabel(self.window)
        self.background.setFixedSize(1136, 850)

        # layout
        self.vbox = QVBoxLayout(self.window)
        self.hbox = QHBoxLayout(self.window)
        self.hbox.addStretch(1)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)
        self.window.setLayout(self.vbox)

        # buttons
        self.rulesButton = QPushButton("Rules")
        self.rulesButton.setStyleSheet(buttonStyle)

        self.playButton = QPushButton("Play")
        self.playButton.setStyleSheet(buttonStyle)

        self.scoreButton = QPushButton("Score")
        self.scoreButton.setStyleSheet(buttonStyle)

        self.backButton = QPushButton("Back")
        self.backButton.setStyleSheet(buttonStyle)

        self.hitButton = QPushButton("Hit")
        self.hitButton.setStyleSheet(buttonStyle)

        self.standButton = QPushButton("Stand")
        self.standButton.setStyleSheet(buttonStyle)

        self.splitButton = QPushButton("Split")
        self.splitButton.setStyleSheet(buttonStyle)

        self.leaveButton = QPushButton("Leave")
        self.leaveButton.setStyleSheet(buttonStyle)

    def startApp(self):
        self.window.show()
        self.homePage()
        sys.exit(self.app.exec())

    def homePage(self):
        # set the background image as the home page
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond_acceuil.png)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)

        self.rulesButton.clicked.connect(self.rulesPage)
        self.scoreButton.clicked.connect(self.scoresPage)

        self.hbox.addWidget(self.rulesButton)
        self.hbox.addWidget(self.scoreButton)

    def rulesPage(self):
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond regle.PNG)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)

        self.playButton.clicked.connect(self.gamePage)

        self.hbox.addWidget(self.playButton)

    def scoresPage(self):
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond score.PNG)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)

        self.backButton.clicked.connect(self.homePage)

        self.hbox.addWidget(self.backButton)

    def gamePage(self):
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond table.PNG)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)

        self.leaveButton.clicked.connect(self.leavePage)

        self.hbox.addWidget(self.hitButton)
        self.hbox.addWidget(self.standButton)
        self.hbox.addWidget(self.splitButton)
        self.hbox.addWidget(self.leaveButton)

    def leavePage(self):
        self.background.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond au revoir.PNG)")

        clearLayout(self.hbox)
        clearLayout(self.vbox)


def clearLayout(layout):
    for i in reversed(range(layout.count())):
        widgetToRemove = layout.itemAt(i).widget()
        if widgetToRemove is not None:
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)
