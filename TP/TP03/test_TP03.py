from test_TP03z import *

##################################
## Procédure d'exécution des tests
##################################

DICO = {'01_fonction': FonctionTest,
        '02_positivite': PositiviteTest,
        '03_condition': ConditionTest,
        '04_recursif_decollage': DecollageTest,
        '05_recursif_trihaut': TriangleHautTest,
        '06_recursif_tribas': TriangleBasTest,
        '07_recursif_regle': RegleTest,
        '08_somme': SommeTest,
        '09_duree_decomposition': DureeDecompositionTest,
        '10_duree_secondes': DureeSecondesTest,
        '11_duree_addition': DureeAdditionTest,
        '12_duree_affichage': DureeAffichageTest,
        '13_duree_temps_total': DureeTempsTotalTest,
            }


def fais_tests(choix):
    '''Fonction qui appelle les batteries de test selon le choix de
    l'utilisateur.'''
    dico = DICO
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(dico[choix])
    except:
        print('='*70)
        print('Le choix "%s" ne fait pas partie des possibilites suivantes:' % choix)
        s = '\n  * '
        print(s[1:] + s.join(sorted(list(dico.keys()))))
        print('='*70)
        exit()
    unittest.TextTestRunner(verbosity=2).run(suite)

##################################
# Calcul de la note du TP
##################################

def detaille_note():
    '''Pour calculer les notes à chaque sous-suite de tests.'''
    total_general  = 0
    success_general= 0
    for k in sorted(DICO.keys()):
        s = unittest.TestLoader().loadTestsFromTestCase(DICO[k])
        f = open('erreurs.txt','w')
        res = unittest.TextTestRunner(stream=f,verbosity=1).run(s)
        f.close()
        total = res.testsRun
        failed= len(res.failures)
        errors= len(res.errors)
        success = total - failed - errors
        print("{}/{}".format(success,total),k)
        total_general += total
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    print('Note indicative: {}/20'.format(round(success_general/total_general*20,2)))
