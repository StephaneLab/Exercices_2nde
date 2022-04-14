#!/usr/bin/python3.9
# Licence GPL3 (c) 2022 Stéphane Lassalvy
import numpy as np
import random as rd
def nb_simuleDeEquilibre(nbIndividus, nbFaces):
    # Exercice 11 page 324 MATHS 2nde Magnard Programme 2019 (Sésamaths)
    # ISBN 978-2-210-11165-3
    #
    # Simule le tirage d'un dé à nbFaces faces, nbIndividus fois
    # Le dé est supposé équilibré
    #
    # Entrée :
    # nbIndividus : nombre d'individus de l'échantillon
    # nbFaces : nombre de faces du dé
    #
    # Sortie :
    # effectifs : tableau des effectifs des observations réparties suivant les faces de 1 à nbFaces
    nbImpairs = 0
    nbPairs   = 0
    effectifs = [0] * nbFaces
    for i in range(1, nbIndividus + 1):
        observation = rd.random()
        for k in range(0, nbFaces):
            if observation >= k/12 and observation < (k+1)/12:
                effectifs[k] += 1
                if (k+1) % 2 == 1:
                    nbImpairs += 1
    print("nombre d'observations")
    print(nbIndividus)
    print("Nombre d'observations impaires :")
    print(nbImpairs)
    print("Nombre d'observations paires")
    nbPairs = nbIndividus - nbImpairs
    print(nbPairs)
    print("Effectifs des faces de 1 à 12 :")
    effectifs = np.array(effectifs)
    print(effectifs)
    frequences = np.round(np.array(effectifs) / nbIndividus, 4)
    print("Fréquences des faces de 1 à 12 :")
    print(frequences)
    return(effectifs)
# Exécution du programme
nb_simuleDeEquilibre(899, 12)
