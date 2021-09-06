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
if __name__ == '__main__': import test_TP01 as testeur
# NE PAS COMMENTER la ligne precedente...



# ***************************************************************************
# Premier travail: ecrire print('Hello World !') a la ligne 29 ci-dessous.
# ***************************************************************************



# ***************************************************************************
# La fonction qui salue le monde vivant
# ***************************************************************************

def hello_world():
    '''Normalement, cela doit renvoyer Hello World !'''
    return 'Mais il va falloir changer des choses...'

# Ligne suivante a decommenter pour tester la fonction hello_world()
#if __name__ == '__main__': testeur.fais_tests('00_hello')

# *************************************************************************** 
# Mettre ici (enfin ci-apres... l'idee est de garder les lignes de 
# commentaires qui definissent ce qui va suivre et non de les effacer...) les 
# assignations demandees dans la premiere section 
# ***************************************************************************






# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('01_assignations')

# ***************************************************************************
# Mettre ci-apres les instructions conditionnelles de la seconde section
# ***************************************************************************






# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('02_conditionnelles')

# ***************************************************************************
# Definir ci-apres la fonction de verification de surcharge
# ***************************************************************************

def verification_surcharge(poids_bagage):
    # A vous de remplir ! Et n'oubliez pas de commenter !
    return 



# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('03_fonction')


# ***************************************************************************
# Faire ci-apres vos calculs de sommes en utilisant des boucles
# ***************************************************************************




    

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('04_boucles')


# ***************************************************************************
# Definir ici la fonction permettant de determiner le prix d'une nuit a l'auberge
# ***************************************************************************

def prix_auberge(heure_arrivee):
    """ La presente 'docstring' entre guillemets triples permet de documenter 
    les fonctions que l'on ecrit. Il faudra penser a toujours en mettre une et 
    modifier celles qui seront indiquees par defauts dans les fichiers de TP. 
    """
    return

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('05_auberge')

# ***************************************************************************
# Definir ici la fonction donnant le prix du peage
# ***************************************************************************

def prix_peage(de1,de2):
    """ Docstring a completer. """
    return 



# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('06_peage')

# *************************************************************************** 
# Recherche d'une personne dans un registre
# *************************************************************************** 

def recherche(numero,registre):
    """ Docstring a completer. """
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('07_recherche')

# *************************************************************************** 
# Enfin, la recherche de l'espion dans la ville. Cette fois, il y a deux 
# fonctions a completer.
# ***************************************************************************

def est_espion(infos):
    """ Docstring a completer. """
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('08_espion')

    
def verification_ville(infos_habitants):
    """ Docstring a completer """
    return 

# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('09_ville')

# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
