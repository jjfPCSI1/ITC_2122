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
if __name__ == '__main__': import test_TP05 as testeur



# ***************************************************************************
# Rentree des classes
# ***************************************************************************

def corrige_score(premiere_manche,final_errone):
    '''docstring a remplir....'''
    pass

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_rentree')


# ***************************************************************************
# Liberation de prisonnier a la prison de Sikania
# ***************************************************************************

def sikinia(n):
    '''Reçoit un nombre n de cellules,
    doit renvoyer la liste des numéros de cellules pour les prisonniers libérés'''
    pass

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_prison_sikinia')

# ***************************************************************************
# Version plus difficile, car non mathématiquement prévisible
# ***************************************************************************
def sikinia_difficile(cellules, i_depart):
    """ (dict, int) -> (list(int))
    * `cellules` est un dictionnaire contenant l'état initial des portes de chaque cellule
    (True pour ouvert, False pour fermé)
    * `i_depart` est le numéro de la cellule à partir de laquelle on commence à appuyer
    sur les interrupteurs (c'est comme si on oubliait les étapes qu'on aurait dû faire
    avant de démarrer à la cellule `i_depart`)
    """
    return "liste des prisonniers libérés"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_prison_sikinia_difficile')

# ***************************************************************************
# Version plus difficile, car non mathématiquement prévisible
# ***************************************************************************
def sikinia_recursif(cellules, i_depart, final):
    """ (dict, int, bool) -> (list(int))
    * `cellules` est un dictionnaire contenant l'état initial des portes de chaque cellule
    (True pour ouvert, False pour fermé)
    * `i_depart` est le numéro de la cellule à partir de laquelle on commence à appuyer
    sur les interrupteurs (c'est comme si on oubliait les étapes qu'on aurait dû faire
    avant de démarrer à la cellule `i_depart`)
    * `final` est un booléen:
    s'il est à True, on renvoie la liste des prisonniers libérés,
    sinon il n'y a pas besoin de calculer cette liste.
    Attention, la fonction doit être récursive (donc s'appeler elle-même),
    ne doit pas comporter de boucles imbriquées et pas trop (<5) d'instructions conditionnelles.
    Vous êtes explicitement autorisés à modifier le dictionnaire `cellules` au vol
    """
    # Mettez là tout ce qui fait le corps de la fonction

    if final:
        # Mettez le calcul de la liste des prisonniers libérés dans ce bloc

        return "liste des prisonniers libérés"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_prison_sikinia_recursif')


# ***************************************************************************
# Feux de foret
# ***************************************************************************

def feux_de_foret(altitudes,impacts):
    '''docstring a remplir....'''
    pass


# Lignes suivantes commencant par '#if' a decommenter pour tester

# Les tests rapides d'abord.
#if __name__ == '__main__': testeur.fais_tests('04_foret_rapide')

# Puis ceux qui prennent un peu plus de temps pour tester l'efficacite de l'algorithme choisi.
#if __name__ == '__main__': testeur.fais_tests('05_foret_long')

# Enfin ceux qui prennent *vraiment* longtemps, qui impose une efficacite optimale.
#if __name__ == '__main__': testeur.fais_tests('06_foret_tres_long')


# ***************************************************************************
# Les petits pois a ranger...
# ***************************************************************************


def range_petits_pois(nb_petits_pois):
    '''docstring a remplir....'''
    pass


# Lignes suivantes (commencant par '#if' a decommenter pour tester

# Tests pour petites valeurs de nb_petits_pois:
#if __name__ == '__main__': testeur.fais_tests('07_petits_pois_rapide')

# Tests pour valeurs moyennes de nb_petits_pois:
#if __name__ == '__main__': testeur.fais_tests('08_petits_pois_moyen')

# Tests pour grandes valeurs de nb_petits_pois:
#if __name__ == '__main__': testeur.fais_tests('09_petits_pois_long')

# Tests pour tres grandes valeurs de nb_petits_pois:
#if __name__ == '__main__': testeur.fais_tests('10_petits_pois_tres_long')

# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
