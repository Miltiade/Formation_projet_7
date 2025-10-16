# CAVEAT: on suppose que le coût de chaque action est un entier

import csv

def programme_dynamique(actions, budget):
    n = len(actions)    
    # Initialiser la table DP : (n+1) lignes, (budget+1) colonnes, valeurs à 0
    DP = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Remplissage de la table
    for i in range(1, n + 1):
        action = actions[i - 1]
        cout = int(action["cout"])
        gain = int(action["cout"] * action["benefice"] / 100)
        
        for b in range(budget + 1):
            if cout > b:
                DP[i][b] = DP[i - 1][b]
            else:
                DP[i][b] = max(DP[i - 1][b], gain + DP[i - 1][b - cout])
    
    # Backtracking pour retrouver les actions sélectionnées
    b = budget
    actions_choisies = []
    
    for i in range(n, 0, -1):
        if DP[i][b] != DP[i - 1][b]:
            action = actions[i - 1]
            actions_choisies.append(action)
            b -= int(action["cout"])
    
    actions_choisies.reverse()  # pour garder l’ordre initial
    
    return actions_choisies, DP[n][budget]

# Lecture du fichier CSV et préparation de la liste actions
actions = []

with open('Liste+d\'actions+-+P7+Python+-+Feuille+1.csv', newline='') as csvfile:
    lecteur = csv.DictReader(csvfile, delimiter=',')
    for ligne in lecteur:
        benefice_str = ligne['Bénéfice (après 2 ans)'].strip().replace('%', '')
        benefice = float(benefice_str)

        action = {
            "nom": ligne['Actions #'],
            "cout": int(float(ligne['Coût par action (en euros)'])),  # conversion en entier (par précaution)
            "benefice": benefice
        }
        actions.append(action)

budget = 500

# Appel de la fonction optimisée
meilleure_combinaison, meilleur_gain = programme_dynamique(actions, budget)
cout_total = sum(action["cout"] for action in meilleure_combinaison)

# Affichage des résultats
if not meilleure_combinaison:
    print("Aucune combinaison trouvée conforme au budget.")
else:
    print("Meilleure combinaison :", [action["nom"] for action in meilleure_combinaison])
    print(f"Coût total : {cout_total} EUR")
    print(f"Gain total : {meilleur_gain} EUR")
