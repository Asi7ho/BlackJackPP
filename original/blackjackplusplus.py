# on apporte ici toutes les bibliothèques nécessaires

# fonction apportée pour ordonner les dictionnaires
from collections import OrderedDict
from fonctions import *
from donnees import *
from random import *  # bibliothèque destinée au hasard

""" bibliothèques dédiée aux graphiques
et plus particulièrement à la création de fenetre """
from tkinter import *
from tkinter import messagebox
import tkinter

from time import sleep  # bibliothèque servant à manipuler les durées

""" 2 fichiers pythons contenant les différentes données variables
et les fonctions nécessaires"""


# on définie la fonction présentant la page d'accueil
def accueil():
    global can, jouer, quitter_j, v_score, scores, fond

    """on insere ici l'image de fond de l'écran d'accueil"""
    fond = PhotoImage(file='./original/fonds/fond_acceuil.png', master=fenetre)
    can.create_image(569, 380, image=fond)

    """on raffraichit le canvas"""
    can.update()

    """on définit les différents boutons"""
    quitter_j = Button(fenetre, text='Quitter',
                       width=15, command=fenetre.destroy)
    quitter_j.pack(side=RIGHT)
    jouer = Button(fenetre, text='jouer', width=15, command=regle)
    jouer.pack(side=LEFT)
    v_score = Button(fenetre, text='score', width=15, command=score)
    v_score.pack(side=LEFT)

    """on récupère les scores stockés dans le fichier scores"""
    scores = recup_scores()


def regle():  # ici la fonction présentant les règles
    global can, jouer, v_score, fond, carte, rester, b_doubler, scores

    """on supprime tout ce qui était dans le canvas de la fonction précédentes ainsi que les boutons"""
    can.delete(ALL)
    jouer.destroy()
    v_score.destroy()
    """on insère un nouveau fond"""
    fond = PhotoImage(file='./original/fonds/fond regle.PNG', master=fenetre)
    can.create_image(569, 380, image=fond)

    """ on affiche les boutons pour montrer à quoi le jeu ressemble"""
    jouer = Button(fenetre, text='jouer', width=15, command=partie)
    jouer.pack(side=LEFT)
    carte = Button(fenetre, text='carte', width=15)
    carte.pack(side=LEFT)
    rester = Button(fenetre, text='rester', width=15)
    rester.pack(side=LEFT)
    b_doubler = Button(fenetre, text='doubler', width=15)
    b_doubler.pack(side=LEFT)

    """on initialise les scores"""
    scores["joueur"] = 0
    scores["croupier"] = 0
# fonction servant à décomposer le dictionnaire des scores afin de le manipuler


def dicordonne():
    global clés, valeurs
    dicoordre = OrderedDict(
        sorted(scores.items(), key=lambda t: t[1], reverse=True))
    valeurs = []
    for v in dicoordre.values():
        valeurs.append(v)
    clés = []
    for c in dicoordre.keys():
        clés.append(c)
# fonction servant à montrer les scores


def score():
    global can, fond, jouer, v_score
    can.delete(ALL)
    v_score.destroy()
    fond = PhotoImage(file='./original/fonds/fond score.PNG', master=fenetre)
    can.create_image(569, 380, image=fond)
    dicordonne()  # on utilise la fonction pour décomposre le dictionnaire
    """et on boucle sur le dictionnaire décomposé afin d'afficher dans l'ordre les scores"""
    if len(clés) < 5:
        for i in range(len(clés)):
            classement = can.create_text(
                300, 40*i+367, text=str(clés[i]), fill='white', font='Arial 28')
            classement = can.create_text(
                500, 40*i+367, text=str(valeurs[i]), fill='white', font='Arial 28')
    else:
        for i in range(5):
            classement = can.create_text(
                300, 40*i+367, text=str(clés[i]), fill='white', font='Arial 28')
            classement = can.create_text(
                500, 40*i+367, text=str(valeurs[i]), fill='white', font='Arial 28')
    can.update()
# programme principal du jeu


def partie():
    global deck, can, main, main_d, fosse, son_score, mon_score, fond, carte, rester, b_doubler, quitter_j, jouer
    """ on commence par tout initialiser """
    can.delete(ALL)
    carte.destroy()
    rester.destroy()
    b_doubler.destroy()
    quitter_j.destroy()
    jouer.destroy()
    fond = PhotoImage(file='./original/fonds/fond table.PNG', master=fenetre)
    can.create_image(569, 380, image=fond)
    can.create_text(60, 30, text="Croupier", fill='black', font='Arial 18')
    can.create_text(450, 800, text="Joueur", fill='white', font='Arial 24')
    fosse_carte.extend(main['croupier'])
    fosse_carte.extend(main['humain'])
    main = {'croupier': [], 'humain': []}
    main_d = {'croupier': [], 'humain': []}
    can.update()
    """on s'assure que le deck a assez de cartes sinon on le réinitialise en récupérant les cartes jetées """
    if len(deck) < 104:
        deck.extend(fosse_carte)
        for i in range(5):
            fosse_carte.append(deck.pop(0))
    """on mélange le cartes et on attend une seconde"""
    shuffle(deck)
    sleep(1)

    """on pioche la première carte, on l'ajoute à la main du croupier, on l'affiche avec le score de sa main et on fait une pause de 1 seconde"""
    c = deck.pop(0)
    main_d['croupier'].append(c.dessin_carte())
    can.create_image(150, 215, image=main_d['croupier'][0])
    main['croupier'].append(c)
    son_score = can.create_text(150, 30, text=str(
        valeur_m(main['croupier'])), fill='black', font='Arial 18')
    can.update()
    sleep(1)

    """on affectue l'opération 2 fois pour le joueur"""
    c = deck.pop(0)
    main_d['humain'].append(c.dessin_carte())
    can.create_image(450, 567, image=main_d['humain'][0])
    can.update()
    sleep(1)
    main['humain'].append(c)
    c = deck.pop(0)
    main_d['humain'].append(c.dessin_carte())
    can.create_image(500, 567, image=main_d['humain'][1])
    can.update()
    sleep(1)
    main['humain'].append(c)
    mon_score = can.create_text(550, 800, text=str(
        valeur_m(main['humain'])), fill='white', font='Arial 24')
    can.update()
    can.create_text(200, 30, text=str(
        scores['croupier']), fill='black', font='Arial 18')
    can.update()
    can.create_text(600, 800, text=str(
        scores['joueur']), fill='white', font='Arial 24')
    can.update()

    """on affiche le nombre approximatif de cartes restants dans le deck"""
    mini = len(deck) - randrange(15)
    maxi = randrange(15)+len(deck)
    can.create_text(820, 200, text=str("il reste entre"),
                    fill='black', font='Arial 18')
    can.create_text(920, 200, text=str(mini), fill='black', font='Arial 18')
    can.create_text(960, 200, text=str("et"), fill='black', font='Arial 18')
    can.create_text(1000, 200, text=str(maxi), fill='black', font='Arial 18')
    can.create_text(950, 250, text=str("cartes dans le deck!"),
                    fill='black', font='Arial 18')

    """puis on affiche les différents choix possibles pour le joueur"""
    quitter_j = Button(fenetre, text='Quitter', width=15, command=quitter)
    quitter_j.pack(side=RIGHT)
    carte = Button(fenetre, text='Carte !', width=15, command=hit)
    carte.pack(side=LEFT)
    rester = Button(fenetre, text='Je reste', width=15, command=stay)
    rester.pack(side=LEFT)
    b_doubler = Button(fenetre, text='Doubler', width=15, command=doubler)
    b_doubler.pack(side=LEFT)

    """on test si le joueur à un blackjack"""
    blackjack()
# fonction testant le blackjack


def blackjack():
    global fond, carte, rester, b_doubler, quitter_j
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


""" fonction servant à tirer une carte.
Le procédé est le meme que précédemment dans la fonction partie"""


def hit():
    global main, main_d, deck, can, son_score, mon_score, fond, scores, carte, rester, b_doubler, quitter_j
    c = deck.pop(0)
    main_d['humain'].append(c.dessin_carte())
    main['humain'].append(c)
    n = len(main['humain'])
    can.create_image(500+50*(n-2), 567, image=main_d['humain'][n-1])
    can.delete(mon_score)
    mon_score = can.create_text(550, 800, text=str(
        valeur_m(main['humain'])), fill='white', font='Arial 24')
    can.update()
    if valeur_m(main['humain']) > 21:
        can.delete(ALL)
        carte.destroy()
        rester.destroy()
        b_doubler.destroy()
        quitter_j.destroy()
        sleep(1)
        fond = PhotoImage(
            file='./original/fonds/fond perdu.PNG', master=fenetre)
        can.create_image(569, 380, image=fond)
        can.update()
        scores['croupier'] += 1
        sleep(3)
        partie()

# fonction faisant piocher le croupier jusqu'à arriver à un nombre entre 17 et 21


def stay():
    global deck, can, main, main_d, son_score, mon_score, fond, scores, carte, rester, b_doubler, quitter_j
    carte.destroy()
    rester.destroy()
    b_doubler.destroy()
    quitter_j.destroy()
    c = deck.pop(0)
    main_d['croupier'].append(c.dessin_carte())
    main['croupier'].append(c)
    n = len(main['croupier'])
    can.create_image(150+50*(n-1), 215, image=main_d['croupier'][n-1])
    can.delete(son_score)
    son_score = can.create_text(150, 30, text=str(
        valeur_m(main['croupier'])), fill='black', font='Arial 18')
    can.update()
    blackjack()
    if valeur_m(main['croupier']) > 21:
        sleep(1)
        fond = PhotoImage(
            file='./original/fonds/fond gagné.PNG', master=fenetre)
        can.create_image(569, 380, image=fond)
        can.update()
        scores['joueur'] += 1
        sleep(3)
        partie()
    elif valeur_m(main['croupier']) < 17:
        sleep(2)
        stay()
    else:
        if valeur_m(main['humain']) > valeur_m(main['croupier']):
            sleep(1)
            fond = PhotoImage(
                file='./original/fonds/fond gagné.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            scores['joueur'] += 1
        elif valeur_m(main['croupier']) > valeur_m(main['humain']):
            sleep(1)
            fond = PhotoImage(
                file='./original/fonds/fond perdu.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            scores['croupier'] += 1
        can.update()
        sleep(3)
        partie()


"""fonction servant à doubler.
elle fait appelle à la fonction hite pour tirer une carte
puis réplique la fonction stay avec des valeurs de gains différents"""


def doubler():
    global deck, can, main, main_d, son_score, mon_score, fond, carte, rester, b_doubler, quitter_j
    carte.destroy()
    rester.destroy()
    b_doubler.destroy()
    quitter_j.destroy()
    hit()
    sleep(1)
    c = deck.pop(0)
    main_d['croupier'].append(c.dessin_carte())
    main['croupier'].append(c)
    n = len(main['croupier'])
    can.create_image(150+50*(n-1), 215, image=main_d['croupier'][n-1])
    can.delete(son_score)
    son_score = can.create_text(150, 30, text=str(
        valeur_m(main['croupier'])), fill='black', font='Arial 18')
    can.update()
    blackjack()
    if valeur_m(main['croupier']) > 21:
        sleep(1)
        fond = PhotoImage(
            file='./original/fonds/fond gagné.PNG', master=fenetre)
        can.create_image(569, 380, image=fond)
        can.update()
        scores['joueur'] += 2
        sleep(3)
        partie()
    elif valeur_m(main['croupier']) < 17:
        sleep(2)
        stay()
    else:
        if valeur_m(main['humain']) > valeur_m(main['croupier']):
            sleep(1)
            fond = PhotoImage(
                file='./original/fonds/fond gagné.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            scores['joueur'] += 2
        elif valeur_m(main['croupier']) > valeur_m(main['humain']):
            sleep(1)
            fond = PhotoImage(
                file='./original/fonds/fond perdu.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            scores['croupier'] += 2
        can.update()
        sleep(3)
        partie()
# fonction servant à demander ou non de s'enregistrer


def quitter():
    global entree, deck, can, fond, scores, carte, rester, b_doubler, quitter_j
    del (scores['croupier'])
    dicordonne()
    can.delete(ALL)
    carte.destroy()
    rester.destroy()
    b_doubler.destroy()
    quitter_j.destroy()
    if len(valeurs) >= 6:
        if scores['joueur'] >= valeurs[-2]:
            fond = PhotoImage(
                file='./original/fonds/fond score.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            value = StringVar()
            value.set("Entrez votre pseudo")
            entree = Entry(fenetre, textvariable=value, width=30)
            entree.pack()
            valider = Button(fenetre, text="Valider", command=recupere)
            valider.pack(side=RIGHT)
        else:
            fond = PhotoImage(
                file='./original/fonds/fond au revoir.PNG', master=fenetre)
            can.create_image(569, 380, image=fond)
            can.update()
            sleep(2)
            fenetre.destroy()
    else:
        fond = PhotoImage(
            file='./original/fonds/fond score.PNG', master=fenetre)
        can.create_image(569, 380, image=fond)
        can.update()
        value = StringVar()
        value.set("Entrez votre pseudo")
        entree = Entry(fenetre, textvariable=value, width=30)
        entree.pack()
        valider = Button(fenetre, text="Valider", command=recupere)
        valider.pack(side=RIGHT)
# fonction servant à récupérer le score et le pseudo donné


def recupere():
    scores[entree.get()] = scores['joueur']
    del (scores['joueur'])
    dicordonne()
    if len(valeurs) >= 6:
        if scores[clés[-1]] == scores[entree.get()]:
            del (scores[clés[-2]])
        else:
            del (scores[clés[-1]])
    enregistrer_scores(scores)
    messagebox.showinfo("Alerte", "votre score a bien été enregistré")
    fenetre.destroy()


# fenetre graphique
fenetre = Tk()
fenetre.title("Blackjack")
can = Canvas(fenetre, width=1100, height=800, bg='white')
can.pack(side=TOP, padx=5, pady=5)

#  on initialise le deck
for i in range(6):
    for figure in figures:
        for rang in range(1, 14):
            deck.append(Carte(rang, figure))
for i in range(randrange(5, 101)):
    fosse_carte.append(deck.pop(0))

# on fait appelle à la première fenetre
accueil()

# demarrage :
fenetre.mainloop()
