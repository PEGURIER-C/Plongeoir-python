Titre du projet : Plongeoir-python 

Auteur : Sacha et Clément


Fichier .geo : Ce fichier doit avoir une bonne syntaxe. Si la syntaxe est mauvaise, le programme vous renverra la ligne qui fait défaut. Enfin, la commande "extrude" est écrite par défaut pdans gmsh sur trois lignes, pour que le programme marche il vous suffit d'enlever les retour à la ligne, en laissant les espaces dans le script du fichier .geo.

Fichier .dgibi : Le fichier dgibi doit, à la fin du calcul, écrire la flèche maximale dans un fichier se nommant "resultat.txt".

Fichier Path.py : A l'intérieur de ce programme, écrire le chemin du fichier .dgibi ainsi que celui de son fichier .geo associé.

Mettre le fichier .geo et le .dgibi dans le même dossier que generate_positions.py, Analyse_Syntaxe.py, Main.py et Path.py. 
Exécuter le generate_positions.py (./generate_positions.py) et définir les variables ainsi que leurs valeurs minimales et maximales. Les nombres à virgules se notent avec des points. Attention, le nombre d'essai évolu tel que nb_essais = 5**nb_variables. Vous pourrez vérifier le tableau avec toutes les valeurs des variables dans Val_positions.txt.
Exécuter ensuite le Main.py (./Main.py) dans mico24 vous permettra de réaliser une optimisation paramétrique de votre problème pour obtenir une valeur minimale de la flèche.
