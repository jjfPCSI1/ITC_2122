# TP01: Découverte de Pyzo et de GitHub

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Quelques exercices d’entraînement
=================================

Le fichier `TP01_decouverte.py` est déjà préécrit pour contenir des
tests pour les objets qu’il vous faut définir et les fonctions qu’il
vous faut écrire. Pour lancer les tests concernant un exercice
particulier, il vous suffit de décommenter (c'est-à-dire supprimer le dièze) la ligne correspondante afin
de vérifier votre avancée. Continuez à écrire dans le même fichier
`TP01_decouverte.py` et suivez le guide... On n’oubliera pas de
commenter abondamment toutes les fonctions créées.

Assignation
-----------

1.  Stocker la valeur `42` dans la variable `ma_variable`.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

2.  Stocker dans la variable `reponse_grande_question_de_l_univers` le résultat de la suite d’opérations
    suivante:
    -   Élever `ma_variable` à la puissance 5 ;
    -   Diviser le résultat par le carré de {l’année du début de la
        révolution française auquel on a soustrait le carré de 5}.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

3.  Faire de même dans la variable `encore_une_reponse` avec la suite d’opérations:
    -   Prendre l’année de début de la révolution française ;
    -   La multiplier par 10 ;
    -   Ajouter 2 ;
    -   Prendre le résultat modulo 50.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Instructions conditionnelles
----------------------------

4.  Stocker dans la variable `x` la valeur préalablement stockée dans la
    variable `valeur_mystere` que Python connaît déjà (attention, comme il se doit, il n’y a pas d’accent dans le nom de la variable).

5.  Si `x` est un multiple de 5, stockez dans la variable `resultat_if` la chaîne de caractères `"x est un multiple de 5."` (attention à la ponctuation: ne pas oublier le point final). Sinon, si est un multiple de 3, stockez dans la même variable la
    chaîne `"x est un multiple de 3."`. Sinon stockez la chaîne `"Pas de chance..."`

Notez que, dans l’exercice précédent, si `x` est à la fois multiple de 5 et
multiple de 3, il ne sera estampillé que « multiple de 5 ».

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Définir une fonction
--------------------

6.  Définir une fonction qui prenne un seul argument `poids_bagage` (exprimé en kg) et
    qui vérifie s’il y a ou non surcharge avant d’embarquer un bagage
    dans la soute d’un avion. La fonction doit renvoyer
    -   `"Surcharge !"` si le poids excède strictement 100 kg ;
    -   `"Surtaxe..."` si le poids appartient à l'intervalle (ouvert-fermé) ]20 kg ; 100 kg] ;
    -   `"Tout va bien."` si le poids appartient à l'intervalle (fermé-fermé) [0; 20 kg] ;
    -   `"What the hell !?!"` sinon.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Faire des boucles
-----------------

7.  Calculer à l’aide d’une boucle la somme des entiers de 1 à 100
    et stocker le résultat dans la variables `somme_entiers_1_a_100`  .

8.  Calculer de même la somme des carrés des entiers de 1 à 100 et
    stocker le résultat dans la variable `somme_des_carres_1_a_100`.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


9.  Stocker dans la variable `somme_divisibles_par_333_et_813` la somme des entiers entre 1 et 1 000 000 qui soient à la fois divisibles par 333 et 813.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

Quelques mélanges
-----------------

10.  L’auberge dans laquelle vous avez prévu de passer la nuit ce soir
    propose des tarifs très intéressants, pour peu que l’on n’arrive pas
    trop tard. En effet, plus on arrive tôt moins on devra payer. Vous
    devez construire une fonction (nommée `prix_auberge` ) vous donnant directement le
    prix à payer en fonction de votre heure d’arrivée (entier entre 7 et
    24 [l’auberge ferme passé minuit]). Le prix de base est de 10 euros
    plus 5 euros pour toute heure après midi. Il ne peut cependant pas
    dépasser 53 euros. Votre fonction doit renvoyer un entier qui est le
    prix à payer (en euros) correspondant à l’heure d’arrivée donnée.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


11.  Vous arrivez devant un pont que vous devez absolument emprunter pour
    arriver avant la nuit au village situé de l’autre côté de la
    rivière. Cependant, la traversée du pont n’est pas gratuite et le
    tarif dépend de votre chance au jeu. En effet, le gardien vous
    demande de lancer deux dés et le prix dépendra des valeurs que vous
    obtiendrez. Vous devez écrire une fonction `prix_peage` pour vérifier qu’il
    applique bien le bon tarif. Celle-ci reçoit deux entiers compris
    entre 1 et 6 en arguments: la valeur de chaque dé. Si la somme est
    supérieure ou égale à 10 alors vous devez payer une taxe spéciale
    (36 euros), sinon vous payez deux fois la somme des valeurs des deux
    dés. Votre fonction doit non seulement renvoyer le prix à payer,
    mais aussi une chaîne de caractère contenant soit `"Special tax"`, soit `"Regular tax"` selon le
    cas qui se présente.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


12.  Un personnage important de la cité n’est pas rentré chez lui hier
    soir et tout le monde est à sa recherche. Or tout habitant de la
    ville a un numéro unique (type numéro de sécurité sociale) qui lui est associé et doit signer une
    sorte de registre avec ce numéro quand il sort de la ville. Vous souhaitez savoir
    si le registre a été signé, auquel cas il faudra étendre les
    recherches à l’extérieur de la ville.
    Vous devez écrire une fonction `recherche` qui prend deux paramètres en entrée:
    un entier (`numero`), le numéro d’une personne recherchée, puis une
    liste (`registre`) qui correspond aux signatures du registre des sorties.
    Si le numéro est présent dans la liste (il peut l’être plusieurs
    fois) vous devez renvoyer le texte `"Sorti de la ville"` sinon `"Encore dans la ville"`.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


13.  Grâce à un certain nombre d’informateurs plus ou moins fiables, le
    chef de la police a recueilli des indications qui devraient lui
    permettre enfin de démasquer cet espion qui lui échappe depuis des
    semaines. La population de la ville étant relativement importante,
    il vous demande votre aide afin d’automatiser un peu les choses. On
    va commencer par écrire une fonction `est_espion` qui estime la probabilité
    qu’une personne soit un espion, on verra plus tard comment étendre
    cela à toute la ville.
    La fonction reçoit un seul argument `infos` qui est un dictionnaire.
    Un dictionnaire est une structure de données qui, comme une liste, vise à
    stocker de multiples éléments. Sauf qu'au contraire d'une liste dont on peut
    accéder aux éléments via leurs numéros, les éléments d'un dictionnaire peuvent
    être accédés via une «clef», en général une chaîne de caractère. Le
    dictionnaire fourni en argument dispose de 5 clefs: `'taille'`,
    `'age'`, `'poids'`, `'cheval'` et `'brun'` qui donnent
    respectivement accès à la taille en
    cm de la personne (données par `infos['taille']`), l'âge en année
    (`infos['age']`), le poids en kg (`infos['poids']`), un booléen (`True`
    ou `False`) qui dit si la personne possède un cheval (`infos['cheval']`) et un dernier
    booléen qui dit si la personne a des cheveux bruns (`infos['brun']`).
    
    On veut
    déterminer à quel point la personne concernée correspond aux 5
    critères suivants caractéristiques de l’espion:
    -   il aurait une taille supérieure ou égale à 178 cm et inférieure
        ou égale à 182 cm,
    -   il aurait au moins 34 ans,
    -   il pèserait strictement moins de 70 kg,
    -   il n’a pas de cheval,
    -   il a les cheveux bruns.
    Lorsque cela n’est pas précisé explicitement, les inégalités sont au
    sens large.
    La fonction doit tester tous les critères et s’ils sont vérifiés
    tous les 5, elle doit renvoyer `"Tres probable"`. Si seulement 3 ou 4 sont vérifiés,
    elle doit renvoyer `"Probable"`. Si aucun n’est vérifié elle doit renvoyer `"Impossible"` et
    dans les autres cas, elle doit renvoyer `"Peu probable"`.

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


14.  Maintenant que votre fonction de vérification d’espion est
    opérationnelle, le chef de la police voudrait étendre les
    vérifications à l’ensemble des habitants de la ville. Il vous
    demande d’écrire une fonction `verification_ville` qui prend une liste `infos_habitants` en arguments qui,
    pour chaque habitant, donne le dictionnaire contenant les cinq informations nécessaires à
    l’usage de votre fonction `est_espion`. En utilisant la fonction précédente,
    étendre vos recherches à la ville entière en renvoyant une
    liste contenant pour chaque habitant la mention `"Très probable"`, `"Probable"`, `"Peu probable"` ou `"Impossible"`
    correspondante. NB: On peut construire une liste avec la méthode `.append`.
    L’exemple suivant (à adapter selon vos besoins) construit une liste
    qui contient les 10 premiers entiers pairs en partant d’une liste
    vide `[]` et en rajoutant un élément à la fin à chaque tour de boucle à
    l’aide de `append`:

```Python
L = [] # Initialisation de la variable L à une liste vide
for i in range(10): # On itère sur 10 entiers de 0 à 9
    L.append(2*i)   # et on stocke à chaque fois le double dans la liste L
```

**STOP GITLAB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
