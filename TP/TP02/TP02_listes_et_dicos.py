# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent 
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des 
# tests automatiquement et sans effort: il suffira de decommenter la ligne #if 
# #if __name__ == '__main__': testeur.fais_tests('...') 
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est 
# ***absolument primordial*** de lancer l'execution dans le menu via 
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon 
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)
# ***************************************************************************

from vm import *

# On importe la batterie de tests uniquement a l'execution du fichier et non 
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP02 as testeur
# NE PAS COMMENTER la ligne precedente...

# ***************************************************************************
# Determination du quinzieme element d'une liste L deja connue par Python
# ***************************************************************************

quinzieme_element_de_L = 'a completer en modifiant cette chaine'


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_liste')

# ***************************************************************************
# Determination de la note de la QDC04 à partir du dictionnaire notes_sur_5
# ***************************************************************************

note_QDC04 = 'note de la QDC04'

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_dico')


# ***************************************************************************
# Fabrication d'une liste a partir d'une autre
# ***************************************************************************

liste_des_cubes = 'a completer...'


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_cubes')

# ***************************************************************************
# Fabrication d'un dictionnaire à partir d'un autre
# ***************************************************************************

notes_sur_20 = 'a completer'

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_sur_20')

# ***************************************************************************
# Ecriture d'une fonction permettant de determiner le prix total a payer
# ***************************************************************************

def prix_total(prix_au_kg,masse_voulue):
    ''' (list, list) -> int '''
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_prixtotal')


def prix_total_avec_dico(prix_au_kg,masse_voulue):
    ''' (dict, dict) -> int '''
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('06_prixtotal_dico')


# ***************************************************************************
# Verification si un carre est magique ou non
# ***************************************************************************

def est_carre_magique(grille, N):
    ''' 
    (list(list), int) -> list(bool)
    Le nombre magique est donne en argument de sorte que vous n'avez pas a 
    le caculer. Vous devez renvoyer une liste de trois booleens, le premier 
    etant False si au moins une ligne n'a pas pour somme N, le second est 
    False si au moins une colonne n'a pas pour somme N et le dernier est False 
    si une des deux diagonales n'a pas pour somme N. '''
    return
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_magic')


# *************************************************************************** 
# Inversion d'une liste par pop() successifs
# ***************************************************************************

def inversion(liste):
    ''' (list) -> (list) '''
    return


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('08_pop')

# ***************************************************************************
# Mettre ci-apres les instruction pour 'slicer' la liste 'liste_a_slicer'
# ***************************************************************************

liste_slicee_01 = 'pas cela'
liste_slicee_02 = 'ni cela, a vous de modifier...'


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('09_slicing')


# *************************************************************************** 
# Detection des resquilleurs au cinema
# ***************************************************************************

def detection_tricheur(numeros):
    """ (list) -> int 
    À partir d'une liste de numéros d'identification, renvoyer le premier qui se répète.
    """
    return 
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('10_cinema')

# *************************************************************************** 
# Gestion simple du stock sur tout le magasin
# ***************************************************************************

def etat_du_stock(stock,operations):
    """
    (dict, list(list(str, int))) -> dict 
    """
    return 
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('11_stock')

# *************************************************************************** 
# Gestion du stock d'un objet a l'aide d'une file d'attente
# ***************************************************************************

def distribution_efficace(operations):
    """ list(list(int, int)) -> int """
    return
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('12_pile')

# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
