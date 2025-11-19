import os
import subprocess
import pandas as pd
import numpy as np
LARG=0.6
Valeurs=pd.DataFrame({})
val1=[]
val2=[]
val3=[]
with open("val_positions","r") as fichier :
    cpt=0
    for ligne in fichier: 
        cpt+=1
        if cpt==1: # il faut qu'il y ait 3 variables, il ne vérifie pas la forme du fichier (ce qui peut tout faire capoter)
            m=re.search('((.*)\\:){0,2}(.*)',ligne)
            var1 = m.group(0)
            var2 = m.group(1)
            var3 = m.group(2)
        else :
            m=re.search('((.*)\\:){0,2}(.*)',ligne)
            val1.append(m.group(0))
            val2.append(m.group(1))    
            val3.append(m.group(2))
Valeurs[var1]= val1
Valeurs[var2]= val2
Valeurs[var3]= val3

positions=np.array([0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95])
positions = positions*LARG
res_fleche = []
res_noeud = []
df = pd.DataFrame({})
for pos in positions:
    #Changement du fichier .geo
    with open("PlongTemp.geo", "w") as f_in, open("Plongeoir.geo", "r") as f_base:
        contenu = f_base.read().replace("%POS%", str(pos))
        f_in.write(contenu)
    E=0.01

    #Génération du maillage Gmsh
    commande_gmsh = ["gmsh", "-3", "PlongTemp.geo","-clmin", str(E),"-clmax", str(E),"-format" ,"unv" ,"-o", "plongeoir.unv"]
    subprocess.run(commande_gmsh, check=True)
    
    #Exécution de Cast3M
    subprocess.run([r"C:\Cast3M\PCW_25\bin\castem25.bat", "Plongeoir.dgibi"], check=True)
        
    #Lecture du résultat
    with open("resultat.txt", "r") as f_res:
        fleche, noeud = map(float, f_res.read().split())
        res_fleche.append(fleche)
        res_noeud.append(noeud)

# 3️⃣ Enregistrement dans Excel

df["fleche"]= res_fleche
df["position"]= positions
df.to_excel("resultats_castem_diff_pos.xlsx", index=False)

print("Calculs terminés et résultats enregistrés dans resultats_castem_diff_pos.xlsx")
