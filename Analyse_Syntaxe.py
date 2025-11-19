import os
import subprocess
import pandas as pd
import numpy as np
import re 

def LigneCorrecte(ligne) :
  global VAR
  if re.search('SetFactory("OpenCASCADE");', ligne):
    return True
  if re.search('//+', ligne):
    return True
  if re.search('.*=.*;', ligne):
    VAR.append(re.search('(.*)=.*', ligne)) 
    return True
  if re.search('Point\(.*\) = \{ .*, .*, .*, 1.0\};', ligne):
    m = re.search('Point\(.*\) = \{ (.*), (.*), (.*), 1.0\};', ligne)
    for i in range(2):
      if m.group(i) in VAR :
        
    
    return True

  p = re.search('Point',ligne)
  l = re.search('Line', ligne)
    

with open('Plongeoir.geo', 'r') as file:
	lignes = file.readlines()
  
cpt = 0
VAR=[]

for ligne in lignes :
  cpt += 1
  if LigneCorrecte==False : 
    print('la ligne numéro ' + str(cpt) + ' est fausse' )

