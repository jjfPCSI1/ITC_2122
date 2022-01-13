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
if __name__ == '__main__': import test_TP_note_sem1_2122 as testeur
from voulu import *

# ***************************************************************************
# Travail sur les listes
# ***************************************************************************

def au_moins_un_voulu(liste):

    return "Booleen" 

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_au_moins_un_voulu')

def compte_nombre_voulus(liste):

    return "Nombre"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_compte_nombre_voulus')


def rassemble_elements_voulus(liste):
    
    return "Liste d'elements voulus"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_rassemble_elements_voulus')


# ***************************************************************************
# Juste prix
# ***************************************************************************

def juste_prix(prix_max,N,public):
    prix = 7           # Vous pouvez bien sûr changer cette valeur.
    for i in range(N):
        indication = public(prix)
        # A vous de faire quelque chose d'intelligent de cette indication...


    return prix

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_juste_prix_simple')
#if __name__ == '__main__': testeur.fais_tests('05_juste_prix_dur')



# ***************************************************************************
# Arborescence
# ***************************************************************************

def recherche_fichier(chemin, extension):
    """ LISEZ l'énoncé en ENTIER: vous DEVEZ utiliser certaines fonctions """

    return "Liste de chemins de fichiers"

# Lignes suivantes a decommenter pour tester
if __name__ == '__main__': testeur.fais_tests('06_recherche_fichiers_simple')
#if __name__ == '__main__': testeur.fais_tests('07_recherche_fichiers_dur')

# ***************************************************************************
# Montagnes russes
# ***************************************************************************

def montagnes_russes(nb_places, nb_tours, groupes):

    return "Nombre de tickets vendus"

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('08_montagne_russe_simple')
#if __name__ == '__main__': testeur.fais_tests('09_montagne_russe_dur')


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
