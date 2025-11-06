# CAVEAT: on suppose que le coût de chaque action est un entier

import csv
import time

def programme_dynamique(actions, budget):
    n = len(actions)  

    # Initialiser la table DP : (n+1) lignes, (budget+1) colonnes, valeurs initialement fixées à 0
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

def chronometrer_algo(fonction, *args, **kwargs):
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    duree = fin - debut
    print(f"Temps d'exécution : {duree:.4f} secondes")
    return resultat

# Lecture du fichier CSV et préparation de la liste actions
actions = []

with open('dataset1_Python+P7.csv', newline='') as csvfile:
    lecteur = csv.DictReader(csvfile, delimiter=',')
    for ligne in lecteur:
        benefice_str = ligne['Bénéfice (après 2 ans)'].strip().replace('%', '')
        benefice = float(benefice_str)

        cout_str = ligne['Coût par action (en euros)'].strip()
        
        try:
            cout = float(cout_str)
            # Vérifier que le coût est positif (strictement supérieur à 0)
            if cout <= 0:
                print(f"Attention : coût négatif détecté ({cout}) dans la ligne : {ligne}")
                continue  # Ignorer cette action 

        except ValueError:
            print(f"Valeur invalide pour le coût : '{cout_str}' dans la ligne {ligne}")
            # Ignorer cette action
            continue

        # Conversion en centimes (entier) pour conserver la précision
        cout_centimes = int(cout * 100)

        action = {
            "nom": ligne['Actions #'],
            "cout": cout_centimes,
            "benefice": benefice
        }

        actions.append(action)

budget_en_euros = 500
budget_en_centimes = int(budget_en_euros * 100)  # Convertir en centimes pour la logique

# Appel de la fonction optimisée avec chronométrage
meilleure_combinaison, meilleur_gain = chronometrer_algo(programme_dynamique, actions, budget_en_centimes)
cout_total = sum(action["cout"] for action in meilleure_combinaison)

# Affichage des résultats
print("RESULTAT OPTIMIZED. Actions examinées :", len(actions))
if not meilleure_combinaison:
    print("Aucune combinaison trouvée conforme au budget.")
else:
    print("Meilleure combinaison :", [action["nom"] for action in meilleure_combinaison])
    print(f"Gain total : {meilleur_gain / 100:.2f} EUR")  # Convertir en euros avec 2 décimales
    print(f"Coût total : {cout_total / 100:.2f} EUR")
