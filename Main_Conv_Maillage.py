import os
import subprocess
import pandas as pd
import numpy as np

df = pd.DataFrame({})
ancien = 0
eps = 5
err = 100
E= 0.03
res_fleche = []
res_noeud = []
#  Boucle maillage
while err>eps:
    
    # Génération du maillage Gmsh
    commande_gmsh = ["gmsh","-3","plongeoirMaill.geo","-clmin",str(E),"-clmax",str(E),
    "-format","unv","-o","plongeoir.unv"]
    subprocess.run(commande_gmsh, check=True)
    
    #Exécution de Cast3M
    subprocess.run([r"C:\Cast3M\PCW_25\bin\castem25.bat", "Plongeoir.dgibi"], check=True)
            
    #Lecture du résultat ---
    with open("resultat.txt", "r") as f_res:
        fleche, noeud = map(float, f_res.read().split())
        res_fleche.append(fleche)
        res_noeud.append(noeud)
    nouveau = fleche
    err = (abs(ancien-nouveau)/nouveau)*100 
    ancien = nouveau 
    E=E/1.2
    
#Enregistrement dans Excel

df["noeud"]= res_noeud
df["fleche"]= res_fleche
df.to_excel("resultats_castem_convergence_a_maillage.xlsx", index=False)

print("Calculs terminés et résultats enregistrés dans resultats_castem_convergence_a_maillage.xlsx")

