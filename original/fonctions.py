"""Ce fichier définit des fonctions utiles pour le programme blackjack.

On utilise les données du programme contenues dans donnees.py"""

import os
import pickle
from donnees import *
from tkinter import *
""" on creer l'objet carte. Nous avons ainsi son nom, son fivhier image associé
et la valeur de la carte"""


class Carte:
    def __init__(self, rang, figure):
        self.rang = rang
        self.figure = figure

    def dessin_carte(self):
        nom = "./original/cartes/" + \
            nom_carte[self.rang]+" de "+figure_carte[self.figure]+".PNG"
        return PhotoImage(file=nom)

    def __str__(self):
        return(nom_carte[self.rang]+" de "+figure_carte[self.figure])

    def getRang(self):
        return(self.rang)

    def getfigure(self):
        return(self.figure)

    def Valeur(self):
        if self.rang > 9:
            return(10)
        else:
            return(self.rang)
# fonction donnant la veleur de la main d'un joueur


def valeur_m(main):
    valeur_m = 0
    for carte in main:
        valeur_m += carte.Valeur()
    for carte in main:
        if carte.getRang() == 1 and valeur_m + 10 <= 21:
            valeur_m += 10
    return(valeur_m)


def recup_scores():
    """Cette fonction récupère les scores enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire, 
    soit l'objet dépicklé,
    soit un dictionnaire vide.

    On s'appuie sur nom_fichier_scores défini dans donnees.py"""

    if os.path.exists(nom_fichier_scores):  # Le fichier existe
        # On le récupère
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else:  # Le fichier n'existe pas
        scores = {}
    return scores


def enregistrer_scores(scores):
    """Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores. Elle reçoit en paramètre le dictionnaire des scores
    à enregistrer"""

    # On écrase les anciens scores
    fichier_scores = open(nom_fichier_scores, "wb")
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()
