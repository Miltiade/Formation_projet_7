

Vous venez de rejoindre AlgoInvest&Trade, une société financière spécialisée dans l'investissement. La société cherche à optimiser ses stratégies d'investissement à l'aide d'algorithmes, afin de dégager davantage de bénéfices pour ses clients.

Votre responsable technique, Robin, a expliqué que même si tous les membres de votre équipe connaissent les termes techniques, ils sont en revanche tous issus de l'économie et de la finance, plutôt que de l'informatique. Comme vous êtes un des seuls développeurs, votre rôle sera principalement de traduire leurs besoins commerciaux en solutions techniques.

 

Un matin, vous arrivez au travail et vous recevez le courriel suivant :

 

De : Robin

À : Moi

Sujet : Algorithme pour maximiser nos bénéfices

Bonjour,

 

J'espère que vous êtes prêt pour votre premier vrai projet ! 

 

Nous avons besoin d'aide pour rendre nos programmes d'investissement à court terme plus compétitifs. Vous concevrez un algorithme qui maximisera le profit réalisé par nos clients après deux ans d'investissement.

 

Votre algorithme doit suggérer une liste des actions les plus rentables que nous devrions acheter pour maximiser le profit d'un client au bout de deux ans.

 

Nous avons les contraintes suivantes :

    Chaque action ne peut être achetée qu'une seule fois.
    Nous ne pouvons pas acheter une fraction d'action.
    Nous pouvons dépenser au maximum 500 euros par client.

 

Je vous transfère une liste des actions en pièce jointe sur lesquelles nous travaillons après ce mail. La liste a trois colonne : ‘Actions’, ‘Coût par action (en euros)’ et ‘Bénéfice (après 2 ans)’.

 

Je sais que vous êtes nouveau dans le monde de la finance, alors voici un aperçu de la signification de chaque colonne :

 

    Actions – Chaque "Action-#" représente une action dans une entreprise différente. Si vous imaginez la valeur d'une entreprise comme étant une tarte entière, chaque action est comme une part de cette tarte.
    Coût par action (en euros) – Le coût d'une action de l'entreprise en euros.
    Bénéfice (après 2 ans) – Il s'agit du bénéfice réalisé par le titulaire de l'action après 2 ans d'investissement dans l'entreprise. Le bénéfice est un pourcentage du coût de l'action.

 

Pour être aussi transparent que possible pour nos clients, nous voulons que le programme essaie toutes les différentes combinaisons d'actions qui correspondent à nos contraintes, et choisisse le meilleur résultat. Le programme doit donc lire un fichier contenant des informations sur les actions, explorer toutes les combinaisons possibles et afficher le meilleur investissement.

 

Merci !

Robin Greene

Tech Lead, AlgoInvest&Trade

Pièce jointe : Liste d'actions - P7 Python

 

Après avoir lu les exigences, vous commencez à développer une solution de force brute et vous envoyez le code Python à Robin dans un fichier ("bruteforce.py").
