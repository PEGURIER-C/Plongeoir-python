Titre du projet : Plongeoir-python 
Auteur : Sacha et Clément


Fichier .geo : Ce fichier doit avoir une bonne syntaxe. Si la syntaxe est mauvaise, le programme vous renverra la ligne qui fait défaut. Enfin, la commande "extrude" est écrite par défaut pdans gmsh sur trois lignes, pour que le programme marche il vous suffit d'enlever les retour à la ligne, en laissant les espaces dans le script du fichier .geo.

Fichier .dgibi : Le fichier dgibi doit, à la fin du calcul, écrire la flèche maximale dans un fichier se nommant "resultat.txt".

Fichier Path.py : A l'intérieur de ce programme, écrire le chemin du fichier .dgibi ainsi que celui de son fichier .geo associé.

Mettre le fichier .geo et le .dgibi dans le même dossier que generate_positions.py, Analyse_Syntaxe.py, Main.py et Path.py. Exécuter le Main.py (./Main.py) dans mico24 vous permettra de réaliser une optimisation paramétrique de votre problème pour obtenir une valeur minimale de la flèche.
