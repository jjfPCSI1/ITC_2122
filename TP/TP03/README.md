TP03 Petits exos entre amis
===========================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Introduction
------------

1. Simple fonction: Écrire une fonction `simple_fonction(x)` qui renvoie la valeur f(x) de la fonction affine f telle que f(0)=15 et f(10)=0.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2. Fonction conditionnelle: Programmer dans `fonction_conditionnelle(x)` la fonction f définie de la manière suivante:
  - f(x) = 1 si x<0
  - f(x) = x + 1 si x appartient à [0;2]
  - f(x) = -3x   si x > 2

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3. Tables de multiplication: Écrire une fonction `table_mul(n,m)` qui prend en argument deux entiers `n` et `m` et
renvoie en sortie une chaîne de caractères qui contient la table de
multiplication de m pour les n premiers entiers. Par exemple `table_mul(11,15)` doit
renvoyer (sans espace, ni en début, ni en fin de ligne) sous forme de
chaîne

```
1 fois 15 = 15
2 fois 15 = 30
3 fois 15 = 45
4 fois 15 = 60
5 fois 15 = 75
6 fois 15 = 90
7 fois 15 = 105
8 fois 15 = 120
9 fois 15 = 135
10 fois 15 = 150
11 fois 15 = 165
```

Il peut être utile de signaler que `\n` correspond au caractère indiquant un
passage à la ligne dans une chaîne de caractère.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4. Positivité: Construire une procédure booléenne `positif(L)` qui prend en entrée une liste de
nombres réels et qui renvoie `True` si tous les termes de la liste sont
positifs ou nuls et `False` dans le cas contraire.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


5. Chiffres à sommer:
    1.  Proposer une procédure `somme_chiffres(n)` qui renvoie la somme tous les chiffres de l’écriture décimale de l’entier `n`. Par exemple `somme_chiffres(139)` doit renvoyer 13 car 1+3+9=13.
    2.  Armé de cette procédure, écrivez-en deux autres: `probleme_16()` et `probleme_20()` qui, sans prendre aucun argument, renvoient les réponses respectives des problèmes 16 et 20 du projet Euler, voir http://projecteuler.net/problem=16 et http://projecteuler.net/problem=20

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Quelle heure est-il ?
---------------------

Un site de voyage permet de calculer les temps de parcours entre deux
villes sous forme d’une liste à 4 éléments représentant respectivement
les durées en jours, heures, minutes et secondes pour le voyage, le tout
de manière unique, c’est-à-dire que 27 heures vaut en fait 1 jour et
3 heures. Néanmoins, si vous faites plusieurs escales, vous voudriez
bien connaître la durée totale que vous aurez passée dans les
transports. On va décomposer ce problème en plusieurs sous-problèmes
plus simples à résoudre.

1.  Écrire une fonction `decomposition(duree)` qui prend en argument une durée exprimée en
    secondes et renvoie une liste composée de quatre entiers sous la
    forme `[jours,heures,minutes,secondes]`

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2.  Écrire la fonction inverse `secondes(L)` qui prend en argument une liste `L` composée de quatre entiers sous la forme `[jours,heures,minutes,secondes]` pour renvoyer la valeur correspondante en secondes.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  En utilisant les deux fonctions précédentes, écrire la fonction `addition(L1,L2)` qui va additionner correctement deux listes `L1` et `L2` à quatre éléments du type `[jours,heures,minutes,secondes]` et renvoyer la liste du même type correspondant à la durée totale du voyage.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4.  Écrire une fonction `affichage(L)` qui renvoie le temps total passé en transport de manière un peu plus lisible sous forme d'une chaîne de caractère. Par exemple `affichage([3,22,10,54])` doit répondre

        Vous allez voyager un total de 3 jours, 22 heures, 10 minutes et 54 secondes

    NB: Pour ne pas compliquer les choses, on ne s’occupera pas des «s» en
    trop dans le cas où l’on devrait écrire «1 heures» ou «0 secondes» ...

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


5.  Enfin, écrire une fonction `temps_total(liste_de_durees)` qui prend en argument une liste (de taille arbitraire) de durées sous la forme `[jours,heures,minutes,secondes]` et renvoie le temps total de parcours à l’aide de la fonction `affichage(L)` précédente.


**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
