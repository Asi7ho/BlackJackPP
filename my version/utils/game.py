from .scores import *
from .constants import cardRank, cardFigure
from .card import Card
from random import shuffle


class Game:
    def __init__(self):

        self.deck = []
        self.pit = []

        # initialize the deck
        for figure in cardFigure:
            for rank in range(1, len(cardRank) + 1):
                self.deck.append(Card(rank, figure))

        shuffle(self.deck)

        self.scores = getScoresFromFile()

    def initializeGameScore(self):
        self.scores['player'] = 0
        self.scores['dealer'] = 0

    def getScores(self):
        return sortScores(self.scores)

    def updateScoreDealer(self):
        self.scores['dealer'] += 1

    def updateScorePlayer(self):
        self.scores['player'] += 1
