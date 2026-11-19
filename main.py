tache = []


def ajouter_une_tache():
    titre = input("donner le titre ").strip()
    if len(titre) == 0:
        print("titre invalide")
        return False
    tache.append(titre)
    print("tache ajoutee avec succes ")


def afficher_les_tache():
    if len(tache) == 0:
        print("la liste est vide")
    else:
        for n, l in enumerate(tache):
            print("tache numero ", n + 1, ":", l)


def rechercher_une_tache():
    mt = input("donner un mot-clé").lower()
    trouve = False
    for l in tache:
        if mt in l.lower():
            print(l)
            trouve = True
    if trouve == False:
        print("non trouvée")


choix = -1
while choix != 0:
    print("== Gestion des taches ==")
    print("1 - ajouter une tache")
    print("2 - afficher les taches")
    print("3 - rechercher une tache ")
    print("0 - quitter")
    choix = int(input("votre choix : "))
    if choix == 1:
        ajouter_une_tache()
    elif choix == 2:
        afficher_les_tache()
    elif choix == 3:
        rechercher_une_tache()
    elif choix == 0:
        print("fermeture du programme")
    else:
        print("choix invalide")
print("programme finaliser merci pour avoir utiliser mon programme")
