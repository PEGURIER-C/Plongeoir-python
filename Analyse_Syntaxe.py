import re 

def LigneCorrecte(ligne) :
    global pt
    global line
    global circle
    global curve
    global surface
    if re.search(r'SetFactory\("OpenCASCADE"\);', ligne):
        return True
    if re.search(r'//\+', ligne):
        return True
    if re.search(r'([^()])+=[^{}()]+;', ligne):
        return True
    if re.search(r'^\s*Point\s*\([^)]+\)\s*=\s*\{[^,]+(?:\s*,\s*[^,]+){3}\}\s*;\s*$', ligne):
        m=re.search(r'^\s*Point\s*\(([^)]+)\)\s*=\s*\{([^,]+)(\s*,\s*[^,]+){3}\}\s*;\s*$', ligne)
        pt.append(m.group(1))
        return True
    
    if re.search(r'^\s*Circle\s*\([^)]+\)\s*=\s*\{[^,]+(?:\s*,\s*[^,]+){2}\}\s*;\s*$', ligne):
        m=re.search(r'^\s*Circle\s*\(([^)]+)\)\s*=\s*\{([^,]+),\s*([^,]+),\s*([^,]+)\}\s*;\s*$', ligne)
        circle.append(m.group(1))
        if (m.group(2) in pt) & (m.group(3) in pt) & (m.group(4) in pt) :
            return True      
	
    if re.search(r'^\s*Line\s*\([^)]+\)\s*=\s*\{[^,]+(?:\s*,\s*[^,]+){1}\}\s*;\s*$', ligne):
        m=re.search(r'^\s*Line\s*\(([^)]+)\)\s*=\s*\{([^,]+),\s*([^,]+)\}\s*;\s*$', ligne)
        line.append(m.group(1))
        if (m.group(2) in pt) & (m.group(3) in pt) :
            return True
	
    if re.search(r'^\s*Curve\sLoop\s*\([^)]+\)\s*=\s*\{[^,]+(?:\s*,\s*[^,]+)+\}\s*;\s*$', ligne):
        m=re.search(r'^\s*Curve\sLoop\s*\(([^)]+)\)\s*=\s*\{([^,]+(?:\s*,\s*[^,]+)+)\}\s*;\s*$', ligne)
        curve.append(m.group(1))
        liste = re.findall(r'[^,\s]+', m.group(2))
        for i in liste:
            if i not in line and i not in circle :
                return False
        return True

    if re.search(r'^\s*Plane\sSurface\s*\([^)]+\)\s*=\s*\{[^,}]+(?:\s*,\s*([^,])+)*\}\s*;\s*$', ligne):
        m=re.search(r'^\s*Plane\sSurface\s*\(([^)]+)\)\s*=\s*\{([^,}]+(?:\s*,\s*[^,]+)*)\}\s*;\s*$', ligne)
        surface.append(m.group(1))
        liste = re.findall(r'[^,\s]+', m.group(2))
        for i in liste:
            if i not in curve :
                return False
        return True
    
    if re.search(r'^\s*Ruled\sSurface\s*\([^)]+\)\s*=\s*\{[^,}]+(?:\s*,\s*([^,])+)*\}\s*;\s*$', ligne):
        m=re.search(r'^\s*Ruled\sSurface\s*\(([^)]+)\)\s*=\s*\{([^,}]+(?:\s*,\s*[^,]+)*)\}\s*;\s*$', ligne)
        surface.append(m.group(1))
        liste = re.findall(r'[^,\s]+', m.group(2))
        for i in liste:
            if i not in curve :
                return False
        return True

    if re.search(r'^\s*Physical\sLine\s*\("[^"]+"\s*,\s*[^\)]+\)\s*=\s*\{[^,\}]+(?:\s*,\s*[^,]+)*\}\s*;\s*$', ligne):
        return True	
    if re.search(r'^\s*Physical\sCurve\s*\("[^"]+"\s*,\s*[^\)]+\)\s*=\s*\{[^,\}]+(?:\s*,\s*[^,]+)*\}\s*;\s*$', ligne):
        return True
    if re.search(r'^\s*Physical\sSurface\s*\("[^"]+"\s*,\s*[^\)]+\)\s*=\s*\{[^,\}]+(?:\s*,\s*[^,]+)*\}\s*;\s*$', ligne):
        return True
    if re.search(r'^\s*Physical\sVolume\s*\("[^"]+"\s*,\s*[^\)]+\)\s*=\s*\{[^,\}]+(?:\s*,\s*[^,]+)*\}\s*;\s*$', ligne):
        return True

    if re.search(r'^\s*Cylinder\s*\([^)]+\)\s*=\s*\{[^,]+(?:\s*,\s*[^,]+){6,7}\}\s*;\s*$', ligne):
        return True

    if re.search(r'^\s*Box\s*\([^)]+\)\s*=\s*\{[^,]+(?:\s*,\s*[^,]+){5}\}\s*;\s*$', ligne):
        return True
       
    if re.search(r'Extrude\s*\{[^,]+(?:\s*,\s*[^,]+){2}\}\s*\{\s*Point\{[^}]+\};\s*\}', ligne):
        return True
    if re.search(r'Extrude\s*\{[^,]+(?:\s*,\s*[^,]+){2}\}\s*\{\s*Curve\{[^}]+\};\s*\}', ligne):
        return True
    if re.search(r'Extrude\s*\{[^,]+(?:\s*,\s*[^,]+){2}\}\s*\{\s*Surface\{[^}]+\};\s*\}', ligne):
        return True
    
    if re.search(r'^\s*BooleanUnion\s*\{\s*Volume\{[^}]+\};\s*Delete;\s*\}(?:\s*\{\s*Volume\{[^}]+\};\s*Delete;\s*\})+', ligne):
        return True
    if re.search(r'^\s*BooleanUnion\s*\{\s*Curve\{[^}]+\};\s*Delete;\s*\}(?:\s*\{\s*Curve\{[^}]+\};\s*Delete;\s*\})+', ligne):
        return True
    if re.search(r'^\s*BooleanUnion\s*\{\s*Surface\{[^}]+\};\s*Delete;\s*\}(?:\s*\{\s*Surface\{[^}]+\};\s*Delete;\s*\})+', ligne):
        return True

    if re.search(r'^\s*Fillet\s*\{[^}]+\}\s*\{[^}]+\}\s*\{[^}]+\}\s*$', ligne):
        return True
    return False

    
    
with open('plongeoir.geo', 'r') as file:
	lignes = file.readlines()
  

pt=[]
line=[]
circle=[]
curve=[]
surface=[]


cpt = 0
geo = []
condition = True
for ligne in lignes :
    cpt += 1
    if cpt!=1 : 
        if LigneCorrecte(ligne)==False : 
            print('la ligne numéro ' + str(cpt) + ' est fausse' )
            condition = False
            break
    geo.append(ligne)
