L = [i**(((j+1)**i)%11) for j in range(10) for i in range(10)]

liste_a_slicer = L[40:80]

def lecture_dico(fichier):
    DICO  = {}
    with open(fichier) as f:
        for line in f:
            k, v = line.strip().split()
            DICO[k] = float(v)
    return DICO

notes_sur_5 = lecture_dico('notes5.txt')
