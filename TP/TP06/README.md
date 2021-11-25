TP06 Algorithmes plus complexes
===============================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.


Applications directes du cours
------------------------------

1. Recherche dans une liste: Implémentez la fonction `recherche(element,liste)` qui, si `element` appartient à `liste`, renvoie l’indice où l’on
peut trouver cette élément. Renvoie `None` sinon. Copie directe du cours à
proscrire...

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2. Recherche d’un maximum: Implémentez la fonction `maximum(liste)` qui renvoie le maximum d’une liste en complexité linéaire. Copie directe du cours à proscrire...

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3. Calcul de la moyenne et de la variance: Implémentez la fonction `moyenne_et_variance(liste)` qui, à partir d’une liste de nombre, renvoie la
moyenne et la variance (moyenne du carré des écarts à la moyenne)
de la liste. Copie directe du cours à proscrire...

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Triangle de Pascal
------------------

1.  Implémenter une procédure `bino(n,p)` permettant de calculer le coefficient
    binomial de p parmi n défini par

        / n \         n!
        |   |  =  ---------  si p est entier entre 0 et n, et 0 sinon
        \ p /     p! (n-p)!

    On pourra définir une fonction annexe qui renvoie la factorielle de
    l’entier .


**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

2.  Écrire une procédure `pascal(n)` qui renvoie le
    triangle  de Pascal (sous forme d’une liste de listes de longueurs variables)
    jusqu’à la valeur fournie. Par exemple `pascal(3)` doit renvoyer `[[1],[1,1],[1,2,1],[1,3,3,1]]`.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  En utilisant la formule de Pascal, implémentez une fonction `pascal2(n)` qui
    renvoie le triangle de Pascal sans utiliser d’appel à la fonction `bino(n,p)`.
    Comparez la vitesse d’exécution des deux fonctions et pour
    $n=1,10,50,100,200,300,400$.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4.  À présent que l’on sait construire les éléments du triangle de
    Pascal facilement, on peut résoudre le problème 203 du projet Euler.
    Les 8 premières lignes (n=7) du triangle de Pascal s’écrivent

          1
          1    1
          1    2    1
          1    3    3    1
          1    4    6    4    1
          1    5   10   10    5    1
          1    6   15   20   15    6    1
          1    7   21   35   35   21    7    1

    On peut voir que ces huit premières lignes du triangle contiennent
    douze nombres distincts: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 et 35. Un entier positif n est dit « squarefree » si aucun
    carré d’un nombre premier n’est parmi les diviseurs de n. Des
    douze nombres distincts de ces huit premières lignes du triangle de
    Pascal, tous sont squarefree mis à part 4 et 20. La somme de tous ces
    nombres des huit premières lignes vaut alors 105. Écrivez un
    programme qui calcule la somme des nombres squarefree distincts présents dans  les premières lignes du triangle de Pascal. On pourra utiliser un
    ensemble (`set`) pour s’assurer que chaque nombre n’est compté qu’une
    seule fois (voir `help(set)` pour plus de détails).

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Pour réfléchir un peu (Projet Euler 18 et 67)
---------------------------------------------

Considérons le triangle suivant:

            3
           7 4
          2 4 6
         8 5 9 3

En partant du sommet et en descendant uniquement selon les chiffres
adjacents sur la ligne du dessous, la somme maximale que l’on peut
obtenir est 3+7+4+9=23. Écrivez une fonction `somme_maximale(triangle)` qui, étant donné un
triangle proposé comme une liste de liste comme ceux de la section
précédente, calcule la somme maximale sur un des chemins qui mène du
sommet à la base.

Une petite mise en garde néanmoins: pour un triangle de N lignes, il
existe 2 puissance N moins 1 chemins différents du sommet à la base. S’il est
plausible de tous les explorer par une méthode pour de faibles valeurs
de N (disons jusqu’à 20 environ), cela n’est plus possible pour un
triangle de 100 lignes. La méthode se doit d’être un peu plus réfléchie.
;-)

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
