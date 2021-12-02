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
if __name__ == '__main__': import test_TP07 as testeur


# ***************************************************************************
# Tri bulle pour commencer
# ***************************************************************************

def emporte_max_local(liste):
    """(list) -> None
    Modifie la liste `liste` reçue en argument mais ne renvoie rien. Exemple:
    >>> L = [0, 10, 7, 5, 11, 13, 6]
    >>> L
    [0, 10, 7, 5, 11, 13, 6]
    >>> emporte_max_local(L)
    >>> L # Le 10 s'est déplacé jusqu'à croiser le 11, puis c'est le 13
    [0, 7, 5, 10, 11, 6, 13]
    >>> emporte_max_local(L)
    >>> L # Le 7 et le 11 ont l'occasion d'être emportés
    [0, 5, 7, 10, 6, 11, 13]
    >>> emporte_max_local(L)
    >>> L # Puis le 10 peut sauter au-dessus du 6
    [0, 5, 7, 6, 10, 11, 13]
    >>> emporte_max_local(L)
    >>> L # qui se fait alors rattraper par le 7
    [0, 5, 6, 7, 10, 11, 13]
    """

    return "Rien" # en fait None

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_emporte_max_local')

def bubble_sort(liste):
    """ (list) -> None
    Modifie la liste `liste` donnée en argument en appliquant emporte_max_local
    autant que nécessaire. Ne renvoie rien.
    >>> L = [0, 10, 7, 5, 11, 13, 6]
    >>> L
    [0, 10, 7, 5, 11, 13, 6]
    >>> bubble_sort(L)
    >>> L
    [0, 5, 6, 7, 10, 11, 13]
    """

    return "Rien" # en fait None

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_bubble_sort')

# ***************************************************************************
# Tri par insertion
# ***************************************************************************

def insertion(liste, i_depart):
    """(liste, int) -> None
    Procède à l'insertion de l'élément liste[i_depart] dans la partie gauche de
    la liste (soit dans liste[:i_depart]) en déplaçant l'élément visé vers la
    gauche tant que l'on trouve un élément plus grand que lui immédiatement
    à sa gauche.
    La fonction modifie la liste mais ne renvoie rien.
    Seul l'élément initialement en `i_depart` est susceptible de
    «faire son trou» jusqu'à trouver sa place dans la partie gauche.
    >>> L = [0, 10, 7, 5, 11, -13, 6]
    >>> L
    [0, 10, 7, 5, 11, -13, 6]
    >>> insertion(L, 3)
    >>> L # Le 5 coule jusqu'entre le 0 et le 10
    [0, 5, 10, 7, 11, -13, 6]
    >>> insertion(L, 5)
    >>> L # Le -13 va jusqu'au fond de la liste
    [-13, 0, 5, 10, 7, 11, 6]
    >>> insertion(L, 5)
    >>> L # Si on l'appelle n'importe comment, cela peut ne rien faire...
    [-13, 0, 5, 10, 7, 11, 6]
    """

    return "Rien" # en fait None

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_insertion')

def insertion_sort(liste):
    """ (list) -> None
    Implémentation du tri par insertion par application réfléchie et itérative
    de la fonction `insertion` précédente.
    La fonction modifie la liste donnée en argument et ne renvoie rien.
    """

    return "Rien" # en fait None

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('04_insertion_sort')

# ***************************************************************************
# Tri fusion
# ***************************************************************************

def fusion(L1, L2):
    """ (list, list) -> list
    Prend deux listes `L1` et `L2` supposée déjà triée et renvoie une liste
    triée constituée de la fusion de ces deux listes (réfléchissez à comment
    vous feriez si vous aviez deux tas de copies déjà triées par ordre
    alphabétique pour pouvoir en faire un seul tas lui aussi trié par ordre
    alphabétique en vous fatiguant le moins possible.
    Les listes de base ne doivent pas être modifiées.
    La fonction renvoie une nouvelle liste, créée pour l'occasion.
    >>> L1 = [1, 5, 8]
    >>> L2 = [2, 4, 6, 9]
    >>> fusion(L1, L2)
    [1, 2, 4, 5, 6, 8, 9]
    >>> L1
    [1, 5, 8]
    """

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_fusion')

def merge_sort(liste):
    """ (list) -> list
    Renvoie une nouvelle version (triée par tri fusion) de la liste donnée
    en argument.
    Contraintes: la fonction doit
    * n'avoir qu'une seule instruction conditionnelle
    * s'appeler elle-même par deux fois (caractère récursif)
    * appeler la fonction `fusion` définie plus haut
    """

    return "liste triée"

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('06_merge_sort')


# ***************************************************************************
# Tri par baquets
# ***************************************************************************

def buckets(liste, i):
    """(list(int), int) -> list(list)
    En partant d'une liste `liste` d'entiers, distribuer les nombres de la liste
    (dans l'ordre de la liste) dans des baquets suivant la valeur du chiffre
    devant 10**i dans le nombre à distribuer. Par exemple, si i=2, 987 ira dans
    baquets[9], mais si i=1, il ira dans baquets[8] (et dans baquets[7] si i=0)
    La liste d'entrée doit rester inchangée.
    >>> L = [0, 10, 7, 205, 11, 413, 6]
    >>> buckets(L, 0)
    [[0, 10], [11], [], [413], [], [205], [6], [7], [], []]
    >>> buckets(L, 1)
    [[0, 7, 205, 6], [10, 11, 413], [], [], [], [], [], [], [], []] 
    >>> buckets(L, 2) # seuls deux nombres ont un chiffre des centaines non nul
    [[0, 10, 7, 11, 6], [], [205], [], [413], [], [], [], [], []]
    >>> buckets(L, 3) # les chiffres devant 10**3 sont tous nuls
    [[0, 10, 7, 205, 11, 413, 6], [], [], [], [], [], [], [], [], []]
    """
    baquets = [[] for i in range(10)] #On fournit gracieusement l'initialisation


    return baquets

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('07_buckets')

def recupere_buckets(baquets):
    """(list(list)) -> list
    À partir de la liste de listes `baquets` par exemple  obtenue par
    application de la fonction précédente, renvoie une unique liste qui
    concatène (dans l'ordre) les listes qui correspondent à chaque baquet.
    Renvoie une nouvelle liste sans avoir touché `baquets`.
    Si on reprend les exemples précédents, cela donne
    >>> L = [0, 10, 7, 205, 11, 413, 6]
    >>> recupere_buckets(buckets(L, 0))
    [0, 10, 11, 413, 205, 6, 7]
    >>> recupere_buckets(buckets(L, 1))
    [0, 7, 205, 6, 10, 11, 413]
    >>> recupere_buckets(buckets(L, 2))
    [0, 10, 7, 11, 6, 205, 413]
    >>> recupere_buckets(buckets(L, 3))
    [0, 10, 7, 205, 11, 413, 6]
    """

    return "unique liste en ramassant tous les baquets"


# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('08_recupere_buckets')

def bucket_sort(liste):
    """ (list) -> list
    Renvoie une version triée de `liste` par applications successives des
    fonctions `buckets` et `recupere_buckets`.
    `liste` ne doit pas être modifiée.
    """

    return "liste triée"

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('09_bucket_sort')


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
