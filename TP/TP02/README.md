TP02 Approfondissement du langage: les listes
=============================================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.


Accès à un élément donné via sa position
----------------------------------------

1.  Une liste `L` a été définie dans le module fourni. Stocker dans la
    variable `quinzieme_element_de_L` le quinzième élément de la liste `L`.

2.  Stockez dans la variable `liste_des_cubes` la liste qui contient les cubes des éléments de la liste de l’exercice précédent.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  Les stocks des ingrédients nécessaires à la réalisation d’un onguent
    très utiles commencent à se vider et les savants vous chargent
    d’aller en ville acheter une certaine quantité de chaque ingrédient,
    afin de pouvoir continuer la production pendant le prochain mois.

    Le comptable étant particulièrement pointilleux, il vous donnera
    exactement la quantité d’argent dont vous avez besoin, pas une pièce
    de plus. Heureusement vous savez à l’avance le prix de chaque
    ingrédient et la quantité dont vous avez besoin.

    Écrivez une fonction `prix_total` qui prend en argument deux listes (`prix_au_kilo` et `masse_voulue`) qui
    représentent respectivement les prix au kilogramme de chaque
    ingrédient et la masse (en kg) nécessaire à la fabrication de
    l’onguent. Il doit renvoyer la quantité totale d’argent à demander
    au comptable.

Remarque: quand une liste contient des autres listes, alors les éléments `L[i]`
(pour `i` dans `range(len(L))`) sont eux-aussi des listes, donc peuvent accepter la syntaxe
des crochets de telle sorte que `L[i][j]` (pour `j` dans `range(len(L[i]))`) est le `j`-ième  élément de la `i`-ième liste contenue dans `L`.


**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4.  Un carré magique est une grille carrée (liste de listes) dans
    laquelle des nombres sont placés de telle sorte que la somme des
    nombres de chaque colonne, chaque ligne et de chacune des deux
    diagonales soit la même. De plus, le carré doit contenir une fois
    chaque nombre, de 1 au nombre de cases de la grille.

    Écrivez une fonction `est_carre_magique` qui vérifie si la grille de nombres
    fournie en argument est un carré magique. On vous donne aussi le nombre
    magique N auxquelles les sommes doivent être égales. On vous assure que tous
    les nombres sont différents, il n’est donc pas nécessaire de le vérifier.
    Votre fonction doit renvoyer une liste de trois booléens (`True` ou `False`)
    qui représentent respectivement les propriétés « Toutes les lignes ont leur
    somme qui vaut N », « Toutes les colonnes ont leur somme qui vaut N » et «
    Toutes les diagonales ont leur somme qui vaut N ».

**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Méthode : récupération et effacement d’un élément
-------------------------------------------------

5.  Écrivez une fonction `rabotage` qui prend une liste en argument, ne renvoie
    rien, mais modifie la liste donnée en argument de sorte à supprimer
    les sixième, cinquième et premier éléments de la liste initiale, tout en remettant le
    cinquième élément supprimé précédemment tout à la fin de la liste.

**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Slicing
-------

6.  Stocker dans la variable `liste_slicee_01` la copie de la liste `liste_a_slicer` comprenant tous ses
    éléments sauf de le premier.

7.  Stocker dans la variable `liste_slicee_02` la copie de la liste `liste_a_slicer` comprenant tous ses
    éléments sauf les 10 derniers.

**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

remove, min, max, index
-----------------------

8.  En parallèle du grand marché de la ville, auquel vous accompagnez
    vos amis marchands, un ensemble de jeux sont organisés pour les
    habitants, en particulier la fameuse : cette course se déroule par
    équipes de deux personnes dont deux des jambes sont attachées par
    une corde.

    Afin de constituer les équipes au hasard, une sorte de tirage au
    sort est organisé mais cela prend beaucoup de temps à faire
    manuellement, vous décidez d’aider les organisateurs en écrivant une
    fonction qui prend en argument une liste d’entiers différents que
    chaque participant a librement choisi.

    Les équipes sont constituées ainsi : la personne ayant choisi le
    plus petit entier est avec celle ayant choisi le plus grand, celle
    ayant choisi le deuxième plus petit est avec celle ayant choisi le
    deuxième plus grand, et ainsi de suite.

    Vous devrez renvoyer la liste des compositions de chacune des
    équipes (chaque personne est identifiée de manière unique par la
    position de son vote dans la liste donnée en argument), dans l’ordre
    : d’abord celle dont le plus petit numéro fait partie, puis celle
    dont le second plus petit numéro fait partie, et ainsi de suite. Au
    sein de chaque équipe on affichera d’abord le plus petit numéro puis
    le plus grand. On vous garantit que tous les numéros sont
    différents. Voici un exemple

```Python
>>> tirage = [10, 32, 29, 45, 72, 2]
>>> appariement(tirage)
[[5, 4], [0, 3], [2, 1]]
```

**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Tableau de booléen annexe pour détecter les tricheurs
-----------------------------------------------------

Hint: un indice est caché dans le titre de la section

9.  Vous êtes employé dans un cinéma et votre patron décide de lancer
    une offre spéciale. Toute personne possédant une carte de fidélité a
    le droit, pendant un mois, de voir un film gratuit par jour. Bien
    entendu certaines personnes vont essayer de tricher en venant
    plusieurs fois au cinéma dans la même journée et votre travail
    consiste à détecter ces tricheurs. Si vous trouvez un tricheur, vous
    devez laisser votre caisse à un collègue, et emmener le tricheur
    chez votre patron qui lui confisquera sa carte.

    Votre fonction `detection_tricheur` prend en entrée la liste des numéros de carte
    utilisés dans la journée et doit renvoyer le numéro du premier
    tricheur (s’il y en a au moins un) ou `None` (sinon). On garantit que les
    numéros sont tous des entiers positifs (de sorte à pouvoir
    facilement être utilisés comme indices d’une liste).

**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Gestion de stock
----------------

10. Gérard, votre ami gérant d’un supermarché, s’est débarrassé des
    vieilles caisses enregistreuses et dispose maintenant de tout un
    système moderne, avec lecteurs de code-barres. Un passage rapide
    d’un produit devant le lecteur et le nom du produit s’affiche
    instantanément à l’écran à côté de son prix.

    Votre ami souhaite utiliser ce système pour maintenir un état
    complet de son stock de produits et préparer ses commandes en
    évitant d’avoir à faire l’inventaire toutes les semaines. Lors de
    chaque achat ou vente d’un produit, l’opération est stockée dans un
    fichier, accompagnée du numéro du produit. Vous devez écrire un
    programme (`etat_du_stock`) qui analyse le contenu de ce fichier et détermine la
    quantité restante de chacun des produits du magasin.

    Les données du fichier sont transmises à votre programme sous forme
    de deux listes:
    -   le nombre de produits de chaque type disponibles dans le
        magasin, dans l’ordre du type, *avant* que les achats et ventes
        décrits dans le fichier n’aient été effectués.
    -   La liste des opérations effectuées sous forme de liste de listes
        de deux entiers : le numéro du type de produit qui a été acheté
        ou vendu, et la quantité de produits concernée. Cette quantité
        est un entier positif lorsqu’il s’agit d’un achat par Gérard, et
        négatif lorsqu’il s’agit d’une vente.

    Votre programme doit renvoyer une liste contenant le nombre de
    produits de chaque type disponible dans le magasin, dans l’ordre du
    type, *après* que les achats et ventes décrits dans le fichier aient
    été effectués.

**STOP GITLAB: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Append et pop(0): gestion de stock à l’aide d’une file
------------------------------------------------------

11. Gérard est fatigué d’avoir à réordonner certaines piles de produits
    périssables assez rapidement et a donc décidé d’investir dans un
    système de distribution plus efficace. Avec ce système, dans lequel
    il place ses produits, les clients se servent automatiquement en bas
    de la pile et Gérard peut insérer les nouveaux produits tout en
    haut. Les clients prennent donc les produits dans l’ordre où Gérard
    les a placés. Ce système réduit les chances qu’il reste des produits
    périmés, mais ne les supprime pas totalement. Il faut de temps en
    temps jeter quelques produits lorsqu’il est trop tard pour les
    vendre. Gérard vous fournit la liste des opérations effectuées et
    vous demande d’écrire un programme capable de détecter la date
    d’expiration la plus ancienne parmi les produits restants.

    La liste reçue en paramètre est une liste de doublets où
    -   Le premier entier est la quantité de produits concernés par
        l’opération. Cette quantité est un entier positif lorsqu’il
        s’agit d’un achat par Gérard (ajout) et négatif lorsqu’il s’agit
        d’une vente (retrait).
    -   Le deuxième entier vaut 0 si l’opération est une vente
        (retrait). S’il s’agit d’un achat, cet entier représente la date
        de péremption du produit. L’entier correspond à la concaténation
        de l’année sur quatre chiffres, du mois sur deux chiffres et du
        jour sur deux chiffres.

EXEMPLE entrée :
```Python
operations = [( 3, 20040810),
              (-1, 0),
              (-1, 0),
              ( 4, 20040920),
              (-1, 0),
              ( 3, 20040916),
              (-3, 0),
              (-2, 0)]
```

Sortie attendue: `20040916`
