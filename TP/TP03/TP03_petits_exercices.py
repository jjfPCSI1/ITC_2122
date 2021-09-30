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
if __name__ == '__main__': import test_TP03 as testeur


# ***************************************************************************
# Une petite fonction simple
# ***************************************************************************
    
def simple_fonction(x):
    '''Prend x et doit renvoyer une fonction f affine telle que f(0)=15 et f(10)=0'''
    return 3*x+2  # NB: ce n'est pas la bonne...

# Ligne suivante a decommenter pour tester la fonction simple
#if __name__ == '__main__':  testeur.fais_tests('01_fonction')


# ***************************************************************************
# Verifier qu'une liste ne contient que des elements positifs
# ***************************************************************************

def positif(L):
    '''docstring a remplir....'''
    return "Un booleen"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_positivite')


# ***************************************************************************
# Une fonction conditionnelle pour tester la dexterite dans le maniement des 'if'
# ***************************************************************************

def fonction_conditionnelle(x):
    '''docstring a remplir....'''
    return "Une valeur"


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_condition')


# ***************************************************************************
# Un premier contact avec la récursivité
# ***************************************************************************

def compte_a_rebours(n):
    """ Depuis la console, l'appel devrait donner
    >>> compte_a_rebours(5)
    5
    4
    3
    2
    1
    Décollage !
    >>> 
    """
    return


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_recursif_decollage')


def triangle_haut(n):
    """ Depuis la console, l'appel devrait donner
    >>> triangle_haut(5)
    .....
    ....
    ...
    ..
    .
    >>> 
    """
    return

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_recursif_trihaut')


def triangle_bas(n):
    """ Depuis la console, l'appel devrait donner
    >>> triangle_bas(5)
    .
    ..
    ...
    ....
    .....
    >>> 
    """
    return

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('06_recursif_tribas')


def regle(n):
    """ Depuis la console, l'appel devrait donner
    >>> regle(3)
    -
    --
    -
    ---
    -
    --
    -
    >>> 
    """
    return

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('07_recursif_regle')




# ***************************************************************************
# Sommer les chiffres d'un nombre en ecriture decimale
# ***************************************************************************

def somme_chiffres(n):
    '''(int) -> (int)'''
    return "Un nombre"


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('08_somme')



# *************************************************************************** 
# Le site de voyage. La, on vous laisse ecrire le nom des fonctions, vous avez 
# compris le principe a present... 
# ***************************************************************************



# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('09_duree_decomposition')
#if __name__ == '__main__': testeur.fais_tests('10_duree_secondes')
#if __name__ == '__main__': testeur.fais_tests('11_duree_addition')
#if __name__ == '__main__': testeur.fais_tests('12_duree_affichage')
#if __name__ == '__main__': testeur.fais_tests('13_duree_temps_total')

# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
