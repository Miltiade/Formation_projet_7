import csv 
from algorithms_bruteforce import brute_force
import time
import tracemalloc

def lire_actions(fichier_csv):
    actions = []
    with open(fichier_csv, newline='') as csvfile:
        lecteur = csv.DictReader(csvfile, delimiter=',')
        for ligne in lecteur:
            # Retirer le % dans la colonne Bénéfice, convertir en float
            benefice_str = ligne['Bénéfice (après 2 ans)'].strip().replace('%', '')
            benefice = float(benefice_str)

            cout_str = ligne['Coût par action (en euros)'].strip()
            try:
                cout = float(cout_str)
                if cout <= 0:
                    print(f"Ignorée car coût nul ou négatif ({cout}) : {ligne}")
                    continue

            except ValueError:
                print(f"Valeur invalide pour le coût : '{cout_str}' dans la ligne {ligne}")
                continue
            
            cout_centimes = int(cout * 100)

            action = {
                "nom": ligne['Actions #'],
                "cout": cout_centimes,
                "benefice": benefice
            }
            actions.append(action)

    return actions

def mesure_performance(fonction, *args, **kwargs):
    tracemalloc.start()
    debut = time.time()

    resultat = fonction(*args, **kwargs)

    duree = time.time() - debut
    _, pic_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Durée : {duree:.2f} secondes")
    print(f"Pic mémoire : {pic_mem / 1024 / 1024:.2f} Mo")

    return resultat


# MAIN
if __name__ == '__main__':
    actions = lire_actions('Liste+d\'actions+-+P7+Python+-+Feuille+2.csv')
    budget_en_centimes = int(500 * 100)
    meilleure_combinaison, meilleur_gain, cout_optimal = mesure_performance(brute_force, actions, budget_en_centimes)

    print("RESULTAT BRUTEFORCE. Actions examinées :", len(actions))
    if meilleure_combinaison is None:
        print("Aucune combinaison trouvée qui soit conforme au budget du portefeuille client.")
    else:
        print("Meilleure combinaison :", [action["nom"] for action in meilleure_combinaison])
        print(f"Gain total : {meilleur_gain / 100:.2f} EUR")
        print(f"Coût total : {cout_optimal / 100:.2f} EUR")