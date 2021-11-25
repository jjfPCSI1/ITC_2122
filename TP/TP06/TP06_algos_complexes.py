# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des
# tests automatiquement et sans effort: il suffira de decommenter la ligne if
# if __name__ == '__main__': testeur.fais_tests('...')
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est
# ***absolument primordial*** de lancer l'execution dans le menu via
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)
# ***************************************************************************


# On importe la batterie de tests uniquement a l'execution du fichier et non
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP06 as testeur


# ***************************************************************************
# Algorithme de recherche dans une liste
# ***************************************************************************

def recherche(element,liste):
    """docstring a remplir...."""
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_recherche')



# ***************************************************************************
# Algorithme de recherche du maximum d'une liste
# (on demande une complexite lineaire...)
# ***************************************************************************

def maximum(liste):
    """docstring a remplir...."""
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_maximum')



# ***************************************************************************
# Calcul de la moyenne et de la variance d'une liste de nombres de maniere
# relativement efficace.
# ***************************************************************************

def moyenne(liste):
    return "Moyenne"

def moyenne_et_variance(liste):
    """docstring a remplir...."""
    return "Moyenne", "Variance"

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_moyenne_variance')



# ***************************************************************************
# Fonction binomiale et factoriel(n)
# ***************************************************************************

def factoriel(n):
    """docstring a remplir...."""
    return []


def bino(n,p):
    """docstring a remplir...."""
    return []

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_bino')


# ***************************************************************************
# Triangle de Pascal, version directe
# ***************************************************************************

def pascal(n):
    """docstring a remplir...."""
    return []



# Lignes suivantes commencant par '#if' a decommenter pour tester

# Les tests rapides d'abord.
#if __name__ == '__main__': testeur.fais_tests('05_pascal')

# Puis ceux qui prennent un peu plus de temps pour tester l'efficacite de l'algorithme choisi.
#if __name__ == '__main__': testeur.fais_tests('06_pascal_long')


# ***************************************************************************
# Triangle de Pascal, version récursive
# ***************************************************************************

def pascal_rec(n):
    return []

# Lignes suivantes commencant par '#if' a decommenter pour tester

# Les tests rapides d'abord.
#if __name__ == '__main__': testeur.fais_tests('07_pascal_rec')

# Puis ceux qui prennent un peu plus de temps pour tester l'efficacite de l'algorithme choisi.
#if __name__ == '__main__': testeur.fais_tests('08_pascal_rec_long')

# ***************************************************************************
# Triangle de Pascal, version "sioux"
# ***************************************************************************

def pascal2(n):
    """docstring a remplir...."""
    return 'pas ca !'



# Lignes suivantes commencant par '#if' a decommenter pour tester

# Les tests rapides d'abord.
#if __name__ == '__main__': testeur.fais_tests('09_pascal2')

# Puis ceux qui prennent un peu plus de temps pour tester l'efficacite de l'algorithme choisi.
#if __name__ == '__main__': testeur.fais_tests('10_pascal2_long')


# ***************************************************************************
# Project Euler, probleme 203: nombres "squarefree" dans un triangle de Pascal
# ***************************************************************************


def squarefree_pascal(n):
    """docstring a remplir...."""
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('11_squarefree')


# ***************************************************************************
# Project Euler, problemes 18 et 67: sommes maximales dans des triangles
# ***************************************************************************


# Les triangles suivants peuvent servir pour vos propres tests. Il faudra
# neanmoins penser a les convertir en liste de listes dans l'esprit de ce que
# renvoie la fonction 'pascal(n)' pour pouvoir etre utiliser dans la
# fonction a ecrire.

# L'exemple
mini = """3
7 4
2 4 6
8 5 9 3"""

# Le triangle du probleme 18
moyen = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Un troisieme triangle (plus grand, correspondant au probleme 67) est defini
# dans le fichier 'triangle.txt' que vous pouvez aussi lire et convertir dans
# un format bien compris par votre fonction.

def somme_maximale(triangle):
    """docstring a remplir...."""
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('12_triangle')


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
