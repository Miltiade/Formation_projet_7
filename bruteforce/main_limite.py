import csv
from algorithms_bruteforce import brute_force_limite

def lire_actions(fichier_csv):
    actions = []
    with open(fichier_csv, newline='') as csvfile:
        lecteur = csv.DictReader(csvfile, delimiter=',')
        for ligne in lecteur:
            benefice = float(ligne['Bénéfice (après 2 ans)'].strip().replace('%', ''))
            try:
                cout = float(ligne['Coût par action (en euros)'].strip())
                if cout <= 0:
                    print(f"Ignorée car coût nul ou négatif ({cout}) : {ligne}")
                    continue
            except ValueError:
                continue
            cout_centimes = int(cout * 100)
            actions.append({"nom": ligne['Actions #'], "cout": cout_centimes, "benefice": benefice})
    return actions

# MAIN
if __name__ == '__main__':
    actions = lire_actions('dataset1_Python+P7.csv')
    budget_en_centimes = int(500 * 100)
    duree_max = 134  # secondes

    (meilleure_combinaison,
     meilleur_gain,
     cout_optimal,
     combi_testees,
     duree,
     pic_mem) = brute_force_limite(actions, budget_en_centimes, duree_max)

    print(f"\nCalcul arrêté après {duree:.2f} s")
    print(f"Nombre de combinaisons testées : {combi_testees}")
    print(f"Actions dans la liste : {len(actions)}")
    print(f"Pic mémoire : {pic_mem / 1024 / 1024:.2f} Mo")
    if meilleure_combinaison is None:
        print("Aucune combinaison valide trouvée.")
    else:
        print("Meilleure combinaison :", [a['nom'] for a in meilleure_combinaison])
        print(f"Gain total : {meilleur_gain / 100:.2f} EUR")
        print(f"Coût total : {cout_optimal / 100:.2f} EUR")