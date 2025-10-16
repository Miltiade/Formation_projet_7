import itertools
import csv


# Définition des variables (chargées depuis le fichier CSV) : action et actions
actions = []

# Lecture du fichier CSV et remplissage de la liste actions
with open('Liste+d\'actions+-+P7+Python+-+Feuille+1.csv', newline='') as csvfile:
    lecteur = csv.DictReader(csvfile, delimiter=',')
    for ligne in lecteur:
        # Retirer le % dans la colonne Bénéfice, convertir en float
        benefice_str = ligne['Bénéfice (après 2 ans)'].strip().replace('%', '')
        benefice = float(benefice_str)

        action = {
            "nom": ligne['Actions #'],
            "cout": float(ligne['Coût par action (en euros)']),
            "benefice": benefice
        }
        actions.append(action)

# Définition des variables : budget, meilleur_gain, meilleure_combinaison
budget = 500
meilleur_gain = 0
cout_optimal = 0
meilleure_combinaison = None

# algorithme de force brute : recherche de la meilleure combinaison
## Passage en revue de toutes les combinaisons possibles
for taille_combinaison in range(1, len(actions) + 1):
    for combinaison in itertools.combinations(actions, taille_combinaison):
        gain_combinaison = sum(action["cout"] * action["benefice"] / 100 for action in combinaison)
        cout_combinaison = sum(action["cout"] for action in combinaison)
## Vérification que le coût de la combinaison est dans le budget et que le gain est maximal
        if cout_combinaison <= budget:            
            if gain_combinaison > meilleur_gain:
                meilleur_gain = gain_combinaison
                meilleure_combinaison = combinaison
                cout_optimal = cout_combinaison

# Affichage des résultats
if meilleure_combinaison is None:
    print("Aucune combinaison trouvée qui soit conforme au budget du portefeuille client.")
else:
    print("Meilleure combinaison :", [action["nom"] for action in meilleure_combinaison])
    print("Gain total :", meilleur_gain)
    print("Coût total :", cout_optimal)   