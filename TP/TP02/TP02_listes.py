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
#if __name__ == '__main__': testeur.fais_tests('01_acces')


# ***************************************************************************
# Fabrication d'une liste a partir d'une autre
# ***************************************************************************

liste_des_cubes = 'a completer...'


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_cubes')

# ***************************************************************************
# Ecriture d'une fonction permettant de determiner le prix total a payer
# ***************************************************************************

def prix_total(prix_au_kg,masse_voulue):
    ''' Ne pas oublier de remplir la docstring... '''
    return 



# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_prixtotal')


# ***************************************************************************
# Verification si un carre est magique ou non
# ***************************************************************************

def est_carre_magique(grille,N):
    ''' Le nombre magique est donne en argument de sorte que vous n'avez pas a 
    le caculer. Vous devez renvoyer une liste de trois booleens, le premier 
    etant False si au moins une ligne n'a pas pour somme N, le second est 
    False si au moins une colonne n'a pas pour somme N et le dernier est False 
    si une des deux diagonales n'a pas pour somme N. '''
    return
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_magic')


# *************************************************************************** 
# Definir ci-apres la fonction 'rabotage'
# ***************************************************************************

def rabotage(liste):
    ''' Docstring a remplir '''
    # Pas de return ici car la fonction n'est pas censee renvoyer quelque chose.




# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_pop')

# ***************************************************************************
# Mettre ci-apres les instruction pour 'slicer' la liste 'liste_a_slicer'
# ***************************************************************************

liste_slicee_01 = 'pas cela'
liste_slicee_02 = 'ni cela, a vous de modifier...'


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('06_slicing')

# *************************************************************************** 
# La fameuse course a trois jambes !
# *************************************************************************** 

def appariement(tirage):
    """ Docstring a completer. """
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_appariement')

# *************************************************************************** 
# Detection des resquilleurs au cinema
# ***************************************************************************

def detection_tricheur(numeros):
    """ Docstring a completer. """
    return 
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('08_cinema')

# *************************************************************************** 
# Gestion simple du stock sur tout le magasin
# ***************************************************************************

def etat_du_stock(stock,operations):
    """ Docstring a completer. """
    return 
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('09_stock')

# *************************************************************************** 
# Gestion du stock d'un objet a l'aide d'une file d'attente
# ***************************************************************************

def distribution_efficace(operations):
    """ Docstring a completer. """
    return 
    
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('10_pile')

# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
