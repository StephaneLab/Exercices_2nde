#!/usr/bin/python3.9
# Licence GPL3 (c) 2022 Stéphane Lassalvy
import numpy as np
import random as rd
def my_simuleNbFemmes(nbIndividus, proportion):
    # Exercice 10 page 324 MATHS 2nde Magnard Programme 2019 (Sésamaths)
    # ISBN 978-2-210-11165-3
    #
    # Simule le nombre de femmes dans une population où
    # la proportion de femmes est connue
    # Entrée :
    # nbIndividus : nombre d'individus de l'échantillon
    # proportion  : proportion de femmes dans la population
    #
    # Sortie :
    # nbFemmes : nombre de femmes dans l'échantillon simulé
    nbFemmes = 0
    for i in range(1, nbIndividus + 1):
        if rd.random() <= proportion:
            nbFemmes += 1
    proportionEstimee = round(nbFemmes * 100 / nbIndividus, 2)
    print(f"Proportion théorique de femmes : {proportion *100} %")
    print(f"Nombre de femmes : {nbFemmes}, sur {nbIndividus} individus,")
    print(f"Qui représentent une fréquence de {proportionEstimee} % de l'échantillon")
    return(nbFemmes)

# Exécution de la fonction
# Taille de l'échantillon : 400
# Proportion de femmes p = 49.6% = 0.496
my_simuleNbFemmes(400, 0.496)


