import random

# Vous pouvez enrechir la base de donnee
# Sachant que chaque pas doit avoir le meme index que son capiatle dans les deux premieres liste
liste_option = ["a", "b", "c", "d"]

liste_pays_capitale = {
    'Paris': 'France',
    'Allemagne': 'Berlin',
    'Itali': 'Rome',
    'Royaume-Uni': 'Londre',
    'États-Unis': 'Washington D.C.',
    'Russie': 'Moscou',
    'Chine': 'Pekin',
    'Japon': 'tokyo',
    'Inde': 'New Delhi',
    'Brésil': 'Brasília'

}


def capitales_pays():

    # generer aleatoirement un pays et son capitale
    pays = random.choice(list(liste_pays_capitale))
    capitale = liste_pays_capitale[pays]

    # supprimer le pays et son capitales des listes
    del liste_pays_capitale[pays]

    # geneger une liste aleatoire de trois capitales
    liste_weights = [1 / len(liste_pays_capitale) for i in range(1, len(liste_pays_capitale) + 1)]
    liste_elements = random.choices(list(liste_pays_capitale.values()), weights=liste_weights, k=3)
    liste_elements.append(capitale)
    random.shuffle(liste_elements)

    # affichage
    print(f"Quelle est la capitale de : {pays}")
    for i in range(len(liste_elements)):
        print(f"{liste_option[i]}: {liste_elements[i]}")

    # recupere le choix
    option = ""
    while not (option in liste_option):
        option = input("---> ")

    # gagner ou perdre
    if liste_option.index(option) == liste_elements.index(capitale):
        print("bonne reponse")
        return True
    else:
        print("mouvaise reponse")
        return False


turn = 5
score = 0
while turn > 0:
    resultat = capitales_pays()
    turn -= 1
    if resultat:
        score += 1
print(f"Vous gagner {score} parti sur 5 \nfin du jeux")
