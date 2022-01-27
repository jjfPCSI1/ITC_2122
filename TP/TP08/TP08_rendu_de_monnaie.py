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
if __name__ == '__main__': import test_TP08 as testeur


# ***************************************************************************
# Mise en jambe
# ***************************************************************************

def deux_maxima(L):
    """(list(?)) -> (?, ?)
    Étant donnée une liste `L` de taille au moins 2
    d'objets comparables et ordonnables (donc qui répondent correctement
    quand on demande `a > b` par exemple), il s'agit de renvoyer
    le maximum `M` ainsi que le second maximum `m` de sorte que
    `M >= m`.
    """
    M = "Vrai maximum de la liste"
    m = "Second maximum de la liste, inférieur ou égal au premier"

    return M, m

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_deux_maxima')

# ***************************************************************************
# Fonctions de conversion
# ***************************************************************************

def euros2cents(valeur_en_euros):
    """
    (float) -> (int)
    Converti une valeur en euros (par exemple `valeur_en_euros = 2.77`)
    en centimes d'euros (ici 277 cents).
    Attention à bien renvoyer un entier à l'aide de la fonction `int`.
    """

    return "Un entier"

def cents2euros(valeur_en_cents):
    """
    (int) -> (float)
    Converti une valeur en cents (par exemple `valeur_en_cents = 277`)
    en euros (ici 2.77 euros).
    """

    return "Un flottant"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_conversions')

# ***************************************************************************
# Récupération des pièces
# ***************************************************************************

def pieces2cents(pieces):
    """(list(int)) -> int
    Étant donnée la liste `pieces` des pièces qui correspondent aux valeurs
    faciales de la variable globale `VALEURS`, la fonction revoie le nombre
    de cents correspondant sous forme d'un entier
    """

    return "Un entier"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_pieces2cents')

def pieces2euros(pieces):
    """(list(int)) -> float
    Étant donnée la liste `pieces` des pièces qui correspondent aux valeurs
    faciales de la variable globale `VALEURS`, la fonction revoie la valeur totale en euros sous forme d'un flottant.
    NB: on vous demande d'utiliser les fonctions précédentes.
    """

    return "Un flottant"


# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_pieces2euros')

# ***************************************************************************
# Algorithme glouton
# ***************************************************************************

def cents2pieces(valeur_en_cents):
    """ (int) -> list(int)
    À partir d'un entier `valeur_en_cents` représentant le nombre de cents
    à distribuer, il faut renvoyer la décomposition en pièces de monnaies
    dont les valeurs faciales sont dans la liste VALEURS correspondante
    (c'est une variable globale, vous ne devez PAS la définir vous même)
    en suivant le principe d'un algorithme glouton:
    * la liste `VALEURS` est supposée triée par ordre décroissant
    * on commence par chercher le nombre maximal de grosses pièces
    (c'est-à-dire de plus haute valeur faciale) qu'on peut rendre pour
    cette `valeur_en_cents`, puis la suivante plus grande, puis la suivante
    jusqu'à épuisement.
    La fonction renvoie une liste de même taille que `VALEURS` avec le nombre
    de pièce de chaque type.
    """

    return "Une liste de pièces"



# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_cents2pieces')

def cents2pieces_limitee(valeur_en_cents):
    """ (int) -> list(int)
    Même principe que la fonction précédente, sauf qu'on ne dispose pas d'un
    stock infini de pièce: il faut donc faire avec les moyens du bord, notés
    dans la variable globale `TIROIR_CAISSE`, et mettre à jour ladite variable
    avant de renvoyer la liste demandée, mais uniquement s'il est possible de
    rendre les pièces sans faire un trou dans la caisse.
    """
    global TIROIR_CAISSE # Pour avoir le droit de modifier le tiroir-caisse

    return "Une liste de pièces"

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('06_cents2pieces_limitee')

# ***************************************************************************
# Bottom up !
# ***************************************************************************

def bottom_up(valeur_en_cents):
    """(int) -> list(int)
    De même que précédemment (sans TIROIR_CAISSE néanmoins) mais on doit
    être sûr de rendre le nombre minimal de pièces, même si la structure
    des valeurs faciales n'est pas adaptée à l'algorithme glouton.
    Par exemple, on doit avoir, pour
    >>> VALEURS = [4, 3, 1]
    >>> bottom_up(6)
    [0, 2, 0]
    et non pas [1, 0, 2] qui serait la réponse de l'algorithme glouton
    """

    return "Une liste de pièces"


# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('07_bottom_up')
#if __name__ == '__main__': testeur.fais_tests('08_bottom_up_long')


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
