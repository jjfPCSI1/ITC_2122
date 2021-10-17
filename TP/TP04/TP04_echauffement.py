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
if __name__ == '__main__': import test_TP04 as testeur 




# ***************************************************************************
# Project Euler numeros 1 et 48
# ***************************************************************************

def probleme_1():
    ''' (None) -> (int) '''
    return []

def probleme_48():
    ''' (None) -> (int) '''
    return []

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_PE1')
#if __name__ == '__main__': testeur.fais_tests('02_PE48')



# ***************************************************************************
# Le gros morceau: la conjecture de Collatz
# ***************************************************************************

def f(n):
    ''' (int) -> (int)'''
    return []


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_fonction_Collatz')

def orbite(a):
    ''' (int) -> list(int)'''
    return []


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_orbite_Collatz')

def temps_de_vol(a):
    ''' (int) -> (int) '''
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_tdv_Collatz')

def altitude(a):
    ''' (int) -> (int) '''
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('06_altitude_Collatz')


# Et pour la suite, vous avez compris le principe...


# Ligne suivante a decommenter pour tester le temps en altitude
#if __name__ == '__main__': testeur.fais_tests('07_ta_Collatz')

# Ligne suivante a decommenter pour tester le temps avant la chute
#if __name__ == '__main__': testeur.fais_tests('08_tac_Collatz')

## À présent, il reste à prévoir les fonctions de data-mining. 
## Attention, il y a une limite de temps.

def le_plus_haut(n):
    """ (int) -> [int, int] """
    return [0, 0]

# Ligne suivante a decommenter pour tester le plus haut
#if __name__ == '__main__': testeur.fais_tests('09_plus_haut_Collatz')

def le_plus_long(n):
    """ (int) -> [int, int] """
    return [0, 0]

# Ligne suivante a decommenter pour tester le plus long
#if __name__ == '__main__': testeur.fais_tests('10_plus_long_Collatz')

def le_plus_long_en_altitude(n):
    """ (int) -> [int, int] """
    return [0, 0]

# Ligne suivante a decommenter pour tester le plus haut en altitude
#if __name__ == '__main__': testeur.fais_tests('11_plus_long_en_altitude_Collatz')

def le_plus_long_avant_la_chute(n):
    """ (int) -> [int, int] """
    return [0, 0]

# Ligne suivante a decommenter pour tester le plus haut avant la chute
#if __name__ == '__main__': testeur.fais_tests('12_plus_long_avant_la_chute_Collatz')

## Reste à améliorer tout cela.
## Quelques conseils:
## * commencez par réécrire la fonction `orbite` en l'appellant `orbite2` par exemple
## de sorte qu'elle vous donne seulement l'orbite partielle jusqu'à passer sous `a`, 
## mais aussi la valeur du premier qui passe sous `a` ainsi que le maximum croisé de l'orbite
## * armé de cela, cherchez dans votre mémoire l'orbite (totale) du premier à être passé sous `a`
## et rajoutez-là à votre orbite partielle, vous aurez l'orbite totale.
## * Ne reste qu'à récupérer le temps de vol (facile), le temps de vol en altitude (facile grâce
## à l'orbite partielle) et le temps avant la chute (là je vous conseille d'écrire une fonction
## annexe `temps_de_vol_avant_la_chute2` qui prend à la fois `a` et l'orbite totale en argument 
## histoire de ne pas avoir à la recalculer). 
## Quant au plus haut, il s'obtient grâce aux maxima récoltés lors des calculs d'orbites.

def tout_en_un(n):
    """ (int) -> list([int, int])"""


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
