import os
import subprocess
import pandas as pd
import numpy as np
import re 

def LigneCorrecte(ligne) :
    global VAR
    if re.search('SetFactory\\("OpenCASCADE"\\);', ligne):
        return True
    if re.search('//+', ligne):
        return True
    if re.search('.*=.*;', ligne):
        VAR.append(re.search('(.*)=.*', ligne)) 
        return True
    if re.search('Point *\\(.*\\) *= *\\{(.*, ){3} 1.0\\};', ligne):
        return True
    
    if re.search('Circle *\\(.*\\) *= *\\{(.*, ){2}.*\\};', ligne):
        return True
	
    if re.search('Line *\\(.*\\) *= *\\{.*, .*\\};', ligne):
        return True
	
    if re.search('Curve Loop *\\(.*\\) *= *\\{(.*, )+ .*\\};', ligne):
        return True

    if re.search('Plane Surface *\\(.*\\) *= *\\{(.*, )* .*\\};', ligne):
        return True
	
    if re.search('Ruled Surface *\\(.*\\) *= *\\{(.*, )* .*\\};', ligne):
        return True
		
    if re.search('Physical Curve *\\(.*\\) *= *\\{(.*, )* .*\\};', ligne):
        return True

    if re.search('Physical Surface *\\(.*\\) *= *\\{(.*, )* .*\\};', ligne):
        return True
		
    if re.search('Cylinder *\\(.*\\) *= *\\{(.*, ){6,7} .*\\};', ligne):
        return True

    if re.search('Box *\\(.*\\) *= *\\{(.*, ){5} .*\\};', ligne):
        return True

    if re.search('Physical Volume *\\(.*\\) *= *\\{(.*, )* .*\\};', ligne):
        return True

    if re.search('Extrude *\\{(.*, ){2}.*\\} *\\{ *Surface\\{.*\\}; *\\}', ligne):
        return True
	if re.search('Extrude *\\{(.*, ){2}.*\\} *\\{ *Point\\{.*\\}; *\\}', ligne):
        return True
    if re.search('Extrude *\\{(.*, ){2}.*\\} *\\{ *Curve\\{.*\\}; *\\}', ligne):
        return True

    if re.search('BooleanUnion *( *\\{Volume\\{.*\\}; *Delete; *\\}){2,}', ligne):
        return True
    if re.search('BooleanUnion *( *\\{Curve\\{.*\\}; *Delete; *\\}){2,}', ligne):
        return True
    if re.search('BooleanUnion *( *\\{Surface\\{.*\\}; *Delete; *\\}){2,}', ligne):
        return True
    return False


with open('plongeoir.geo', 'r') as file:
	lignes = file.readlines()
  
cpt = 0
VAR=[]
d = []
for ligne in lignes :
    cpt += 1
    if LigneCorrecte(ligne)==False : 
        print('la ligne numéro ' + str(cpt) + ' est fausse' )
		break
	d[cpt] = ligne
print(d)
