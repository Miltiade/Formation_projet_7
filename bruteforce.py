import itertools
import csv


# Définition des variables (chargées depuis le fichier CSV) : action et actions
actions = []

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
meilleure_combinaison = None

# algorithme de force brute : recherche de la meilleure combinaison
for taille_combinaison in range(1, len(actions) + 1):
    for combinaison in itertools.combinations(actions, taille_combinaison):
        gain_total = sum(action["cout"] * action["benefice"] / 100 for action in combinaison)
        cout_total = sum(action["cout"] for action in combinaison)

        if cout_total <= budget:            
            if gain_total > meilleur_gain:
                meilleur_gain = gain_total
                meilleure_combinaison = combinaison

# Affichage des résultats
if meilleure_combinaison is None:
    print("Aucune combinaison trouvée qui soit conforme au budget du portefeuille client.")
else:
    print("Meilleure combinaison :", [action["nom"] for action in meilleure_combinaison])
    print("Gain total :", meilleur_gain)