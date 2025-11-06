import itertools
import tracemalloc
import time

def brute_force(actions, budget):
# Attention: cette fonction "travaille" en centimes et pas en euros (pour éviter les erreurs d'arrondi sur les floats)
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

def brute_force_limite(actions, budget, duree_max):
# Attention : cette fonction teste uniquement les combinaisons pendant une durée maximale donnée
    meilleur_gain = 0
    meilleure_combinaison = None
    cout_optimal = 0
    combi_testees = 0

    debut = time.time()
    tracemalloc.start()

    for taille_combinaison in range(1, len(actions) + 1):
        for combinaison in itertools.combinations(actions, taille_combinaison):
            combi_testees += 1
            gain_combinaison = sum(action["cout"] * action["benefice"] / 100 for action in combinaison)
            cout_combinaison = sum(action["cout"] for action in combinaison)
            if cout_combinaison <= budget:
                if gain_combinaison > meilleur_gain:
                    meilleur_gain = gain_combinaison
                    meilleure_combinaison = combinaison
                    cout_optimal = cout_combinaison

            # Vérification du temps écoulé
            if time.time() - debut >= duree_max:
                duree = time.time() - debut
                _, pic_mem = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                print(f"\nCalcul interrompu au bout de {duree_max} secondes.")
                print(f"Durée d'exécution effective : {duree:.2f} secondes")
                print(f"Nombre de combinaisons testées : {combi_testees}")
                print(f"Nombre d’actions traitées : {len(actions)}")
                print(f"Pic mémoire consommé : {pic_mem / 1024 / 1024:.2f} Mo")

                return meilleure_combinaison, meilleur_gain, cout_optimal

    duree = time.time() - debut
    _, pic_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\nCalcul terminé en {duree:.2f} secondes.")
    print(f"Nombre de combinaisons testées : {combi_testees}")
    print(f"Nombre d’actions traitées : {len(actions)}")
    print(f"Pic mémoire consommé : {pic_mem / 1024 / 1024:.2f} Mo")

    return meilleure_combinaison, meilleur_gain, cout_optimal
