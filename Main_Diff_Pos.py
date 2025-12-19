#!/usr/bin/python3

import subprocess
import re

from Analyse_Syntaxe import geo, condition
from Path import dgibiPath

E= 0.05
if condition : 
    with open("val_positions.txt","r") as fichier :
        cpt=0
        lignes = fichier.readlines()
        for ligne in lignes: 
            cpt+=1
            if cpt==1: 
                var= re.findall(r'[^:\\\n]+', ligne) # on récupère les variables dans une liste grace a findall.
                Valeurs=[]
                for i in range(len(var)):
                    Valeurs.append([]) # on initialise une liste de liste pour stocker les valeurs

            else :
                m=re.findall(r'[^:\\\n]+',ligne)
                for i in range(len(m)):
                    Valeurs[i].append(m[i]) # on remplit les listes de valeurs correspondantes

    res_fleche = []
    for j in range(len(Valeurs[0])):
        #Changement du fichier .geo
        with open("PlongTemp.geo", "w") as f_in :
            for i in geo:
                Trouvé = False
                for k in range(len(var)):
                    if re.search("^"+str(var[k]),i):# cherche si la ligne commence par la variable
                        contenu = str(var[k])+"="+str(Valeurs[k][j])+";\n"
                        f_in.write(contenu)
                        Trouvé = True
                if not Trouvé : 
                    f_in.write(i)    
        
    
        #Génération du maillage Gmsh
        commande_gmsh = ["gmsh", "-3", "PlongTemp.geo","-clmin", str(E),"-clmax", str(E),"-format" ,"unv" ,"-o", "plongeoir.unv"]
        subprocess.run(commande_gmsh, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Maillage Gmsh généré pour les positions : ", [Valeurs[i][j] for i in range(len(var))])
        
        #Préparation du fichier .dgibi
        with open("PlongTemp.dgibi", "w") as f_in:
            with open(dgibiPath, 'r') as file:
                lignes = file.readlines()
                for i in lignes:
                    Trouvé = False
                    for k in range(len(var)):
                        if re.search("^"+str(var[k]),i):# cherche si la ligne commence par la variable
                            contenu = str(var[k])+"="+str(Valeurs[k][j])+";\n"
                            f_in.write(contenu)
                            Trouvé = True
                    if not Trouvé : 
                        f_in.write(i)    
        #Exécution de Cast3M
        subprocess.run(["castem24", "PlongTemp.dgibi"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Calcul Cast3M effectué pour les positions : ", [Valeurs[i][j] for i in range(len(var))])

        #Lecture du résultat
        with open("resultat.txt", "r") as f_res:
            fleche= re.findall(r'[^ ]+',f_res.read())
            res_fleche.append(float(fleche[0]))
            print("Flèche maximale obtenue : ", fleche[0])

    #Affichage de la position optimale
    flechemin  = min(res_fleche)
    indice = 0
    for k in range (len(res_fleche)):
        if flechemin == res_fleche[k]:
            indice = k
            break
    print(flechemin)
    print("La flèche minimale est de ", flechemin, " pour les positions : ", [Valeurs[i][indice] for i in range(len(var))])
