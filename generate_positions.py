#!/usr/bin/python3

import itertools
import sys
from numpy import *
from math import *
import collections

def liste_variables(nb_pos=5):
    """ 
    Génère l'ensemble des valeurs des varibales à tester et les écrit dans un fichier.
    La première ligne contient les variables GMSH dont les valeurs varient : 
    POS:LH:LB:,...
    Chacune des lignes suivantes contient les valeurs à tester. 
    exemple : 0.3:1:12.4:...
    """
    #
    cpt = 0
    var=[]
    min=[]
    max=[]
    while True : 
        cpt+=1 
        var.append(str(input("Veuillez rentrer le nom de la variable. si la viariable est \"end\" le programme s'arrete : ")))
        if var[cpt-1] == "end":
            var.pop()
            break
        else :
            min.append(float(input("Veuillez rentrer la valeur minimale de la variable " + var[cpt-1] + " : ")))
            max.append(float(input("Veuillez rentrer la valeur maximale de la variable " + var[cpt-1] + " : ")))
    # structure de données pour stocker les substitutions
    subs = collections.OrderedDict()
    print(var)
    for i in range(len(var)):
        subs[var[i]] = list()
    
    
    # Génération des plages de valeurs pour chaque variable
    ranges = []
    for i in range(len(var)):
        ranges.append(linspace(min[i], max[i], nb_pos))

    # Générer toutes les combinaisons et les ajouter à subs
    for values in itertools.product(*ranges):
        for i, key in enumerate(subs.keys()):
            subs[key].append(round(values[i], 6))  # arrondir pour éviter les problèmes de précision flottante
    
    return subs
    
def printFile(subs,file):
    with open(file, "w") as file:
        keys = list(subs.keys())
        key = keys.pop(0)
        file.write(key)
        for key in keys:
            file.write(':' + key)
        file.write('\n')
        while len(subs[list(subs.keys())[0]])>0:
            keys = list(subs.keys())
            key = keys.pop(0)
            file.write(str(subs[key].pop(0)))                
            for key in keys:
                file.write(':' + str(subs[key].pop(0)))
            file.write('\n')

def main():
    subs = liste_variables()
    printFile(subs,"val_positions.txt")

main()

