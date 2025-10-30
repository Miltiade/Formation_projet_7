import itertools
import csv
import time

def brute_force(actions, budget):
    meilleur_gain = 0
    meilleure_combinaison = None
    cout_optimal = 0

    # Passage en revue de toutes les combinaisons possibles
    for taille_combinaison in range(1, len(actions) + 1): # Déclaration de la variable "taille des combinaisons" ; sa valeur est : [1, nombre total d'actions]
        for combinaison in itertools.combinations(actions, taille_combinaison): # Pour chaque combinaison possible d'actions de taille "taille des combinaisons", on génère toutes les combinaisons possibles de tailles 1 à n, soit (2^n - 1) combinaisons
            # Calcul du gain et du coût pour chaque combinaison : proportionnel à la taille de la combinaison (car la variable "combinaison" est une liste)
            gain_combinaison = sum(action["cout"] * action["benefice"] / 100 for action in combinaison)
            cout_combinaison = sum(action["cout"] for action in combinaison) # Chaque sum parcourt les éléments de la combinaison : ce qui fait un travail O(k) par combinaison de taille k.
            # Vérification que le coût de la combinaison est dans le budget et que le gain est maximal ; ces opérations sont constantes en temps
            if cout_combinaison <= budget:            
                if gain_combinaison > meilleur_gain:
                    meilleur_gain = gain_combinaison
                    meilleure_combinaison = combinaison
                    cout_optimal = cout_combinaison

    return meilleure_combinaison, meilleur_gain, cout_optimal

# Fonction pour chronométrer l'exécution d'un algorithme
def chronometrer_algo(fonction, *args, **kwargs):
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    duree = fin - debut
    print(f"Temps d'exécution : {duree:.4f} secondes")
    return resultat

# Lecture du fichier CSV et remplissage de la liste actions
actions = []
with open('Liste+d\'actions+-+P7+Python+-+Feuille+2.csv', newline='') as csvfile:
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

# Définition de la variable : budget
budget = 500

# Appel de la fonction brute-force avec chronométrage
meilleure_combinaison, meilleur_gain, cout_optimal = chronometrer_algo(brute_force, actions, budget)

# Affichage des résultats
print("RESULTAT BRUTEFORCE. Actions examinées :", len(actions))
if meilleure_combinaison is None:
    print("Aucune combinaison trouvée qui soit conforme au budget du portefeuille client.")
else:
    print("Meilleure combinaison :", [action["nom"] for action in meilleure_combinaison])
    print("Gain total :", meilleur_gain, "EUR")
    print("Coût total :", cout_optimal, "EUR")