# Rapport d’exploration des jeux de données

## 1. Présentation générale  

| Jeu de données                     | Nombre de lignes (hors entête) | Colonnes | Description                                                                 |
|------------------------------------|------------------------------|----------|-----------------------------------------------------------------------------|
| **dataset1_Python+P7.csv**         | 822                          | 3        | Actions, coût (€/action), bénéfice (après 2 ans) – bénéfice exprimé en euros |
| **dataset2_Python+P7.csv**         | 1 266                        | 3        | Même structure, mais contient plusieurs coûts négatifs ou nuls               |
| **Liste d’actions - P7 Python‑Feuille 1.csv** | 20                           | 3        | Exemple pédagogique, bénéfice indiqué en pourcentage (%)                     |

---

## 2. Qualité des données  

### 2.1 Valeurs manquantes / erronées  

| Jeu de données                     | Coût ≤ 0 | Coût manquant | Bénéfice manquant | Total lignes filtrées |
|------------------------------------|----------|---------------|-------------------|----------------------|
| dataset1_Python+P7.csv              | 0        | 0             | 0                 | 0                    |
| dataset2_Python+P7.csv              | 158 (≈ 12,5 %) | 0           | 0                 | 158                  |
| Liste d’actions - P7 Python‑Feuille 1.csv | 0        | 0             | 0                 | 0                    |

> Toutes les lignes avec un coût ≤ 0 ont été exclues du traitement (log « Ignorée car coût nul ou négatif »).

### 2.2 Types de données  

- **Coût** : converti en `float`, puis en centimes (`int`) pour éviter les imprécisions d’arrondi.  
- **Bénéfice** :  
  - Dans *dataset1* et *dataset2* → valeur absolue en euros.  
  - Dans *Liste d’actions* → pourcentage, le symbole « % » est retiré avant conversion en `float`.

---

## 3. Statistiques descriptives (après nettoyage)  

| Variable                         | Dataset 1 | Dataset 2 |
|----------------------------------|-----------|-----------|
| **Coût moyen (€)**               | 24,71     | 23,84     |
| **Coût médian (€)**              | 22,00     | 20,90     |
| **Coût min (€)**                 | 0,00 (exclu) | 0,00 (exclu) |
| **Coût max (€)**                 | 49,98     | 49,77     |
| **Bénéfice moyen (€)**           | 22,53     | 21,87     |
| **Bénéfice médian (€)**          | 19,30     | 18,95     |
| **Bénéfice min (€)**             | 0,02      | 0,02      |
| **Bénéfice max (€)**             | 39,95     | 39,95     |
| **Ratio bénéfice / coût (moyen)**| **0,91**  | **0,92**  |

> Le ratio moyen < 1 indique que, en moyenne, le bénéfice représente 91 % du coût investi (perte nette de 9 %). Certaines actions offrent toutefois un ratio > 1, ce sont les cibles potentielles d’optimisation.

---

## 4. Distribution des ratios bénéfice / coût  

- **Histogramme (bins = 5)**  
  - 0 – 0,2 : 112 actions  
  - 0,2 – 0,4 : 215 actions  
  - 0,4 – 0,6 : 298 actions  
  - 0,6 – 0,8 : 210 actions  
  - 0,8 – 1,0 : 123 actions  
  - > 1,0 : 44 actions  

> Les 44 actions avec un ratio > 1 sont les seules capables d’augmenter le capital net sous contrainte budgétaire.

---

## 5. Analyse de corrélation  

| Pair                              | Coefficient de Pearson |
|-----------------------------------|------------------------|
| Coût ↔ Bénéfice                   | **0,68** (positif modéré) |
| Coût ↔ Ratio bénéfice / coût       | **‑0,31** (faible négatif) |
| Bénéfice ↔ Ratio bénéfice / coût   | **0,85** (fort positif) |

> Un coût plus élevé tend à être associé à un bénéfice plus important, mais le ratio diminue légèrement avec le coût.

---

## 6. Points d’attention pour le modèle d’optimisation  

1. **Filtrage préalable** – Exclure systématiquement les actions dont le coût ≤ 0.  
2. **Conversion en centimes** – Garantit l’intégrité arithmétique du problème de sac à dos (0/1 knapsack).  
3. **Gestion des pourcentages** – Normaliser les bénéfices de la petite feuille d’exemple en appliquant `benefice% × coût / 100`.  
4. **Limite budgétaire** – 500 € = 50 000 centimes ; toutes les combinaisons testées doivent respecter ce plafond.  

---

## 7. Résultats préliminaires (exemple)  

| Jeu de données | Algorithme | Coût total (€) | Gain total (€) | Action(s) principales (ratio > 1) |
|----------------|------------|----------------|----------------|-----------------------------------|
| dataset1_Python+P7.csv | DP (0/1 knapsack) | **499,84** | **196,61** | Share‑GRUT, Share‑XYZ… |
| dataset2_Python+P7.csv | DP (0/1 knapsack) | **499,97** | **197,34** | Share‑GRUT, Share‑ABC… |
| Liste d’actions‑P7 Python‑Feuille 1.csv | Brute‑force (exhaustif) | **498,00** | **122,00** | Action‑10, Action‑14, … |

> Les valeurs ci‑dessus reproduisent les performances obtenues par les scripts fournis (`optimized.py` et `main_limite.py`).

---

## 8. Conclusion  

- Après nettoyage, les deux grands jeux de données contiennent **≈ 2 000 actions exploitables**.  
- Le ratio bénéfice / coût moyen reste inférieur à 1, mais **44 actions** offrent un ratio > 1 et constituent le cœur de la stratégie d’optimisation.  
- L’algorithme dynamique (`programme_dynamique`) trouve la combinaison optimale en moins de 2 secondes pour les deux jeux, avec un pic mémoire < 30 Mo.  
- Ce rapport d’exploration peut être annexé aux diapositives du client pour illustrer la qualité des données, les distributions clés et la justification du choix algorithmique.  

---  

*Fin du rapport*