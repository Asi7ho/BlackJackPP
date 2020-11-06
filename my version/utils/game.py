import sys
from .scores import *
from .constants import cardRank, cardFigure
from .card import Card
from random import randrange, shuffle
from collections import OrderedDict
from time import sleep

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap


class Game:
    def __init__(self):
        self.app = QApplication([])

        self.deck = []
        self.pit = []

        # initialize the deck
        for figure in cardFigure:
            for rank in range(1, len(cardRank) + 1):
                self.deck.append(Card(rank, figure))

        shuffle(self.deck)

        self.numPlayer = 2

        self.window = QWidget()
        self.window.setWindowTitle("Black Jack")
        self.window.setFixedSize(1136, 850)

    def startGame(self):
        self.window.show()
        self.homePage()
        sys.exit(self.app.exec())

    def homePage(self):
        # set the background image as the home page
        self.window.setStyleSheet(
            "background-image: url(./my version/assets/backgrounds/fond_acceuil.png)")

        playButton = QPushButton("Play")
        playButton.clicked.connect(self.rulesPage)

        scoreButton = QPushButton("Score")
        scoreButton.clicked.connect(self.scoresPage)

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(sys.exit)

        self.lay = QHBoxLayout(self.window)
        self.lay.addWidget(playButton)
        self.lay.addWidget(scoreButton)
        self.lay.addWidget(exitButton)

        # get the scores from local files
        self.scores = getScoresFromFile()

    def rulesPage(self):
        self.window.setStyleSheet(
            "QWidget {background-image: url(./my version/assets/backgrounds/fond regle.PNG) }")
        self.lay.removeWidget(self.lay)
        # self.canvas.delete(ALL)
        # self.scoreButton.destroy()
        # # set the background image as the rules page
        # self.backgroundImg = PhotoImage(
        #     file='./my version/assets/backgrounds/fond regle.PNG', master=self.app)
        # self.canvas.create_image(569, 380, image=self.backgroundImg)

        # # set buttons
        # self.playButton = Button(
        #     self.app, text='Play', width=15, command=self.game)
        # self.playButton .pack(side=LEFT)

        # # initialize the scores
        # for player in range(self.numPlayer):
        #     self.score[player] = 0

    def scoresPage(self):
        self.canvas.delete(ALL)
        self.scoreButton.destroy()

        self.backgroundImg = PhotoImage(
            file='./my version/assets/backgrounds/fond score.PNG', master=self.app)
        self.canvas.create_image(569, 380, image=self.backgroundImg)
        self.showScores()

        if len(self.keys) < 5:
            for i in range(len(self.keys)):
                classement = self.canvas.create_text(
                    300, 40*i+367, text=str(self.keys[i]), fill='white', font='Arial 28')
                classement = self.canvas.create_text(
                    500, 40*i+367, text=str(self.values[i]), fill='white', font='Arial 28')
        else:
            for i in range(5):
                classement = self.canvas.create_text(
                    300, 40*i+367, text=str(self.keys[i]), fill='white', font='Arial 28')
                classement = self.canvas.create_text(
                    500, 40*i+367, text=str(self.values[i]), fill='white', font='Arial 28')
        self.canvas.update()

    def showScores(self):
        sortedDict = OrderedDict(
            sorted(self.scores.items(), key=lambda t: t[1], reverse=True))

        self.keys = []
        for k in sortedDict.keys():
            self.keys.append(k)

        self.values = []
        for v in sortedDict.values():
            self.values.append(v)

    def game(self):
        self.canvas.delete(ALL)
        self.hitButton.destroy()
        self.standButton.destroy()
        self.splitButton.destroy()
        self.exitButton.destroy()
        self.playButton.destroy()
        self.backgroundImg = PhotoImage(
            file='./my version/assets/backgrounds/fond table.PNG', master=self.app)

        self.canvas.create_image(569, 380, image=self.backgroundImg)
        self.canvas.create_text(60, 30, text="Croupier",
                                fill='black', font='Arial 18')
        self.canvas.create_text(450, 800, text="Joueur",
                                fill='white', font='Arial 24')

        self.pit.extend(main['croupier'])
        self.pit.extend(main['humain'])
        main = {'croupier': [], 'humain': []}
        main_d = {'croupier': [], 'humain': []}
        self.canvas.update()

        # Check if there is enough cards in deck
        if len(self.deck) < 104:
            self.deck.extend(self.pit)
            for _ in range(5):
                self.pit.append(self.deck.pop(0))

        # shuffle deck
        shuffle(self.deck)
        sleep(1)

        # Croupier get one card and wait 1s
        self.drawCard(Croupier)

        # Player get two cards
        self.drawCard(Player)
        self.drawCard(Player)

        self.canvas.create_text(200, 30, text=str(
            self.scores['croupier']), fill='black', font='Arial 18')
        self.canvas.update()
        self.canvas.create_text(600, 800, text=str(
            self.scores['joueur']), fill='white', font='Arial 24')
        self.canvas.update()

        # remaining number of card in deck
        mini = len(self.deck) - randrange(15)
        maxi = randrange(15)+len(self.deck)
        self.canvas.create_text(820, 200, text=str("il reste entre"),
                                fill='black', font='Arial 18')
        self.canvas.create_text(920, 200, text=str(
            mini), fill='black', font='Arial 18')
        self.canvas.create_text(960, 200, text=str(
            "et"), fill='black', font='Arial 18')
        self.canvas.create_text(1000, 200, text=str(
            maxi), fill='black', font='Arial 18')
        self.canvas.create_text(950, 250, text=str("cartes dans le deck!"),
                                fill='black', font='Arial 18')

        # set buttons
        self.exitButton = Button(
            self.app, text='Exit', width=15, command=self.exit)
        self.exitButton.pack(side=RIGHT)
        self.hitButton = Button(self.app, text='Carte !',
                                width=15, command=self.hit)
        self.hitButton.pack(side=LEFT)
        self.standButton = Button(
            self.app, text='Stand', width=15, command=self.stand)
        self.standButton.pack(side=LEFT)
        self.splitButton = Button(
            self.app, text='Split', width=15, command=self.split)
        self.splitButton.pack(side=LEFT)

        # test if there is blackjack
        self.blackjack()

    def drawCard(self, hand):
        c = self.deck.pop(0)
        main_d['croupier'].append(c.getCardFile())
        self.canvas.create_image(150, 215, image=main_d['croupier'][0])
        sleep(1)
        main['croupier'].append(c)
        son_score = self.canvas.create_text(150, 30, text=str(
            valeur_m(main['croupier'])), fill='black', font='Arial 18')
        self.canvas.update()

    def blackjack():
        sleep(1)
        if valeur_m(main['humain']) == 21 and len(main['humain']) == 2:
            carte.destroy()
            rester.destroy()
            b_doubler.destroy()
            quitter_j.destroy()
            fond = PhotoImage(
                file='./original/fonds/fond gagné blackjack.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            scores['joueur'] += 3
            sleep(3)
            partie()
        elif valeur_m(main['croupier']) == 21 and len(main['croupier']) == 2:
            carte.destroy()
            rester.destroy()
            b_doubler.destroy()
            quitter_j.destroy()
            fond = PhotoImage(
                file='./original/fonds/fond perdu blackjack.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            scores['croupier'] += 3
            sleep(3)
            partie()
