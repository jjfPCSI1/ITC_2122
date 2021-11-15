TP05 Conception d'algorithmes simples
=====================================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Mise en jambe
-------------

1. Rentrée des classes (ou beaucoup de bruit pour rien...)
Un instituteur peu attentif a noté les scores de la seconde manche à l'envers (la dernière équipe en premier, l'avant-dernière en 2ième, etc.)
Écrivez un programme `corrige_score(premiere_manche, final_errone)` qui, étant données la liste des scores de la
première manche et la liste erronée du score total, donne la liste
correcte du score total.

Exemple:


         0   1   2   3   4   5   (scores de la première manche, fournis)
       + 1   4   1   3   2   0   (scores inversés de la 2ème manche, non fournis)
        --- --- --- --- --- ---
         1   5   3   6   6   5   (résultats obtenus par l'instituteur, fournis)

alors qu’il aurait du calculer :

          0   1   2   3   4   5
        + 0   2   3   1   4   1   (scores dans le bon sens)
         --- --- --- --- --- ---
          0   3   5   4   8   6   (résultats corrects, à renvoyer par votre programme)


**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Prison de Sikinia.  
-----------------

2. Version historique. Pour fêter le vingtième anniversaire de la république de Sikinia, le président décide d’une amnistie. Il donne au directeur de la prison les ordres suivants: « Tournez successivement d'un demi-tour les boutons
    - de toutes les portes ;
    - puis d'une porte sur deux à partir de la deuxième ;
    - puis d'une porte sur trois à partir de la troisième ;
    - puis d'une porte sur quatre à partir de la quatrième ;
    - puis ... »
Pour des raisons de sécurité, le directeur de la prison aimerait
connaître à l’avance quels seront les prisonniers libérés. Pouvez-vous
l’aider ? Vous écrirez un programme plus général `liberation_prisonniers(n)` qui prend en argument
le nombre `n` de cellules de la prison (numérotées de 1 à n) et qui doit
renvoyer la liste des numéros des cellules ouvertes. (Problème tiré de
*Elements of mathematics*, 1975, St-Louis (Missouri))

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

3. Version moins prévisible. Les plus mathématiciens d'entre vous auront vu qu'en fait les cellules ainsi ouvertes suivent toujours un même motif (il peut même être intéressant de réfléchir au pourquoi mathématique de la chose, mais je vous laisse en discuter avec vos profs de maths respectifs ou essayer de le démontrer par vous-même). On va donc corser un tout petit peu les choses: à présent, la procédure de rotation des boutons est toujours la même, mais on ne part pas de l'état «toutes les cellules sont fermées», mais d'un état intermédiaire où certaines sont ouvertes et certaines sont fermées. Pour stocker cet état, on vous fournit un dictionnaire (une liste aurait pu marcher aussi, en prenant pour position le numéro de la cellule et en rajoutant une cellule numérotée $0$, mais c'est pour s'entraîner dans la manipulation des dictionnaires) `cellules` qui a pour clefs les numéros de cellule (ces numéros sont bien des entiers qui sont des clefs valides de dictionnaires, au même titre que des chaînes de caractères) et pour valeur `True` si la cellule commence ouverte et `False` si la cellule commence fermée.

En outre, on ne va pas forcément démarrer à la toute première porte, mais on donne un second argument `i_depart` qui dit qu'on démarre à cette porte `i_depart` pour tourner les boutons à toutes les cellules multiples de `i_depart` en allant jusqu'à la dernière cellule accessible (pour trouver le nombre de cellules total jusqu'auquel on va devoir aller, vous pouvez utiliser la fonction `len` qui donne le nombre de clefs présentes dans le dictionnaire. Les clefs en question étant les entiers de 1 à n, il y en a bien n au total). On continue ainsi de suite jusqu'à atteindre le(s) multiple(s) du numéro de la dernière cellule.

En résumé, il faut ici compléter la fonction `sikinia_difficile(cellules, i_depart)` qui prend en argument le dictionnaire `cellules` donnant l'état actuel des cellules et le numéro `i_depart` de la cellule à partir de laquelle on réapplique le protocole de la section précédente.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

4. Version récursive. La structure d'appel adoptée à la section précédente facilite grandement la mise en place d'une implémentation récursive `sikinia_recursif(cellules, i_depart)` qui doit de la même manière renvoyer la liste des cellules desquelles on libèrera les prisonniers après application de la procédure complète. Pour passer les tests, votre fonction devra forcément:
  * s'appeler elle-même (c'est le principe même d'une fonction récursive: elle fait appel à elle-même en changeant juste les paramètres d'appel);
  * comporter une unique instruction conditionnelle, donc un unique `if` accompagné ou non de son `else`, à votre convenance (réfléchissez bien à la condition d'arrêt qu'il faut implémenter);
  * comporter une unique boucle (`for` ou `while`, à votre convenance, même si la boucle `for` sera plus sûre) au lieu des deux dont vous avez eu besoin dans les deux sections précédentes.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Feux de forêt
-------------

La foudre se déchaîne sur les Vosges. Les éclairs déchirent le ciel,
offrant un spectacle à la fois sublime et effrayant. Néanmoins, les
habitants du coin savent que la menace principale provient des feux de
forêt: chaque éclair s’abattant sur la forêt engendre un départ de feu.
Vous décidez d’aider les pompiers à s’organiser dans leur combat contre
les flammes.

La forêt, qui s’étend tout le long de la crête de la montagne, peut
être représentée par une suite de cases, chacune à une altitude donnée.
Lorsque la foudre s’abat sur une case, celle-ci s’enflamme, puis se
propage ensuite aux cases voisines, toujours en montant. Autrement dit,
le feu se propage d’une case aux cases voisines de même altitude ou
d’altitude supérieure.

Écrivez un programme `feux_de_foret(alitudes,impacts)` qui détermine le nombre de cases de forêt qui risquent de brûler connaissant la liste `altitudes` des altitudes des cases successives le long de la crête et la liste `impacts` des _positions_ (variant de 0 à `len(altitudes)-1`) où frappent les éclairs (ces positions étant données dans un ordre a priori quelconque).

Votre programme doit renvoyer un unique entier : le nombre de cases de
forêt menacées par les flammes.

Pour passer tous les tests, votre programme doit être aussi efficace que
possible (limitations en temps à 1 s sachant que le nombre de cases
et le nombres d’éclairs peuvent varier de 1 à 40000).

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Des histoires de petits pois
----------------------------

Un marchand de légumes très maniaque souhaite ranger ses petits pois en
les regroupant en boîtes de telle sorte que chaque boîte contienne un
nombre factoriel de petits pois. Il souhaite également utiliser le plus petit nombre de boîtes possible. Ainsi, s’il a 17 petits pois, il utilisera :
  -   2 boîtes de 3! = 6 petits pois, soit 12 petits pois rangés;
  -   2 boîtes de 2! = 2 petits pois, soit 4 petits pois rangés;
  -   1 boîte  de 1! = 1 petit pois, soit 1 petit pois rangé.

ce qui donne bien 2x3! + 2x2! + 1x1! = 12 + 4 + 1 = 17.

Votre programme `range_petits_pois(nb_petits_pois)` doit renvoyer la liste (unique) qui permettra à
l’assistant du marchand de préparer les boîtes avant d’y ranger ses
petits pois. Bien entendu, tout comme les factoriels, le nombre de
petits pois à ranger peut vite devenir astronomique et il ne faut
pas que le programme prenne plus de 1 s pour donner sa réponse.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
