"""
    This file handle the save/recover the scores state. 
"""

import os
import pickle

from .constants import localScoresFile


def getScoresFromFile():
    """
      Recover scores from the scores file defined in constants.py
      The function returns a dictionnary if there if the file exists otherwise it returns an empty dictionary
    """

    if os.path.exists(localScoresFile):
        scoresFile = open(localScoresFile, "rb")
        scoresFile = pickle.Unpickler(scoresFile)
        scores = scoresFile.load()
        scoresFile.close()
    else:
        scores = {}
    return scores


def saveScores(scores):
    """
      Save the scores dictionnary in a local file
    """

    # The previous data are erased
    scoresFile = open(localScoresFile, "wb")
    scoresFile = pickle.Pickler(scoresFile)
    scoresFile.dump(scores)
    scoresFile.close()
