import os
import subprocess
import pandas as pd
import numpy as np
import re 

def LigneCorrecte(ligne) :
  global VAR
	global point
  if re.search('SetFactory("OpenCASCADE");', ligne):
    return True
  if re.search('//+', ligne):
    return True
  if re.search('.*=.*;', ligne):
    VAR.append(re.search('(.*)=.*', ligne)) 
    return True
 
	if re.search('Point *\(.*\) *= *\{(.*, ){3} 1.0\};', ligne):
		return True
	
	if re.search('Circle *\(.*\) *= *\{(.*, ){2}.*\};', ligne):
		return True
	
	if re.search('Line *\(.*\) *= *\{.*, .*\};', ligne):
		return True
	
	if re.search('Curve Loop *\(.*\) *= *\{(.*, )+ .*\};', ligne):
		return True

  if re.search('Plane Surface *\(.*\) *= *\{(.*, )* .*\};', ligne):
		return True
		
  if re.search('Ruled Surface *\(.*\) *= *\{(.*, )* .*\};', ligne):
		return True
		
  if re.search('Physical Curve *\(.*\) *= *\{(.*, )* .*\};', ligne):
		return True

	if re.search('Physical Surface *\(.*\) *= *\{(.*, )* .*\};', ligne):
		return True
		
  if re.search('Cylinder *\(.*\) *= *\{(.*, ){6,7} .*\};', ligne):
		return True
				
  if re.search('Box *\(.*\) *= *\{(.*, ){5} .*\};', ligne):
		return True
				
  if re.search('Physical Volume *\(.*\) *= *\{(.*, )* .*\};', ligne):
		return True
				
  if re.search('Extrude *\{(.*, ){2}.*\} *\{Surface\{.*\};\}', ligne):
		return True
					
  if re.search('BooleanUnion *(\{.*\{.*\}; .*; /}){2,}', ligne):
		return True



with open('Plongeoir.geo', 'r') as file:
	lignes = file.readlines()
  
cpt = 0
VAR=[]
point=[]

for ligne in lignes :
  cpt += 1
  if LigneCorrecte==False : 
    print('la ligne numéro ' + str(cpt) + ' est fausse' )

