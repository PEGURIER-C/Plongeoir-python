import os
import subprocess
import pandas as pd
import numpy as np
import re

from Analyse_Syntaxe import geo, condition

Valeurs=pd.DataFrame({})
val1=[]
val2=[]
val3=[]
E= 0.01
with open("val_positions","r") as fichier :
    cpt=0
    for ligne in fichier: 
        cpt+=1
        if cpt==1: # il faut qu'il y ait 3 variables, il ne vérifie pas la forme du fichier (ce qui peut tout faire capoter)
            m=re.search('(.*)\\:(.*)\\:(.*)',ligne)
            var1 = m.group(1)
            var2 = m.group(2)
            var3 = m.group(3)
        else :
            m=re.search('(.*)\\:(.*)\\:(.*)',ligne)
            val1.append(m.group(1))
            val2.append(m.group(2))    
            val3.append(m.group(3))
Valeurs[var1]= val1
Valeurs[var2]= val2
Valeurs[var3]= val3

res_fleche = []
res_noeud = []
df = pd.DataFrame({})
for val in Valeurs[var1]:
    #Changement du fichier .geo
    with open("PlongTemp.geo", "w") as f_in, open("Plongeoir.geo", "r") as f_base:
        for i in range(length(geo)):
            if re.search('^POS',geo(i)):
                contenu = "POS="+str(val)+";\n"
                f_in.write(contenu)
            else : 
                f_in.write(geo(i))

    #Génération du maillage Gmsh
    commande_gmsh = ["gmsh", "-3", "PlongTemp.geo","-clmin", str(E),"-clmax", str(E),"-format" ,"unv" ,"-o", "plongeoir.unv"]
    subprocess.run(commande_gmsh, check=True)
    
    #Exécution de Cast3M
    subprocess.run([r"C:\Cast3M\PCW_25\bin\castem25.bat", "Plongeoir.dgibi"], check=True)
        
    #Lecture du résultat
    with open("resultat.txt", "r") as f_res:
        fleche, noeud = map(float, f_res.read().split())
        res_fleche.append(fleche)

#Enregistrement dans Excel

df["fleche"]= res_fleche
df["position"]= positions
df.to_excel("resultats_castem_diff_pos.xlsx", index=False)

print("Calculs terminés et résultats enregistrés dans resultats_castem_diff_pos.xlsx")
