To create the virtual environment:
sudo apt install python3(si necessaire)
sudo apt install python3.12-venv
python3 -m venv .venv
pip install -r requirements.txt

-----------------------------------------------------
-----------------------------------------------------




# 📄 Documentation — **Simulateur de Budget Étudiant**

## 📌 Présentation

Le **Simulateur de Budget Étudiant** est un outil en Python permettant d’analyser un budget mensuel à partir d’un fichier CSV, de visualiser la répartition des dépenses et d’obtenir des recommandations simples pour améliorer sa gestion financière.

Ce projet a été réalisé **en autonomie** afin de :

* Mettre en pratique mes compétences en **Python**, **analyse de données**, et **visualisation**.
* Structurer un projet comme en entreprise (modules séparés, réutilisables).
* Valoriser mon profil sur **mon CV** et **LinkedIn** par un projet concret.

---

##  Fonctionnalités

* **Lecture et analyse** des revenus et dépenses à partir d’un fichier CSV.
* **Calculs automatiques** : totaux, reste disponible, taux d’épargne et de dépenses.
* **Recommandations personnalisées** en fonction des données.
* **Génération de graphique** (camembert) de la répartition des dépenses.
* **Organisation modulaire** en plusieurs fichiers Python.


---

## 📂 Structure du projet

```
budget_simulator/
├── main.py                  # Point d’entrée principal
├── budget.py                # Calculs et logique métier
├── utils.py                 # Fonctions utilitaires
├── data/
│   └── example_budget.csv   # Exemple de budget utilisateur
├── outputs/                 # Rapports PDF générés (option)
├── graphs/                  # Graphiques générés
├── requirements.txt         # Dépendances Python
└── README.md                # Documentation
```

---

## 🗂 Format du fichier CSV attendu

Le fichier CSV doit comporter **exactement** trois colonnes :
`Type`, `Nom`, `Montant`

* `Type` : `"Revenu"` ou `"Dépense"`
* `Nom` : nom de la catégorie ou source (ex. `"Loyer"`, `"Bourse"`)
* `Montant` : montant numérique

**Exemple :**

```csv
Type,Nom,Montant
Revenu,Bourse,450
Revenu,Job étudiant,300
Dépense,Loyer,400
Dépense,Nourriture,180
Dépense,Netflix,15
Dépense,Transports,50
```

---

##  Installation

1. **Cloner le dépôt**

```
git clone .....
cd budget_simulator
```

2. **Créer un environnement virtuel**

```
python -m venv venv
source venv/bin/activate  # sous macOS/Linux
venv\Scripts\activate     # sous Windows
```

3. **Installer les dépendances**

```
pip install -r requirements.txt
```

---

## ▶️ Utilisation

### 1. Préparer un fichier CSV

Placez-le dans le dossier `data/`.

### 2. Lancer le script

```
python main.py --input data/exemple_budget.csv
```

### 3. Résultat attendu (exemple console)

```
--- Résumé du budget ---
Total revenus  : 750,00 €
Total dépenses : 645,00 €
Reste mensuel  : 105,00 €
Taux d’épargne : 14 %

--- Recommandations ---
✅ Très bon équilibre entre dépenses et revenus.

Graphique sauvegardé dans: graphs/budget_graphic.XXXX-XX-XX.png
```

---

##  Graphique généré

* Un **camembert** représentant la répartition des dépenses.
* Enregistré automatiquement dans `/graphs/` avec date dans le nom.

---

## Compétences mises en œuvre

* Lecture et traitement de données (`pandas`)
* Visualisation (`matplotlib`)
* Programmation modulaire en Python
* Automatisation avec scripts CLI (`argparse`)
* Génération dynamique de fichiers
* Bonnes pratiques de structuration de projet

---

## 🚀 Améliorations possibles

* Ajout d’une interface web (`Streamlit` ou `Flask`).
* Connexion avec exports bancaires.
* Personnalisation des recommandations.
* Comparaison multi-mois.

---

## 📄 Licence

Projet personnel, open-source, sous  CC0-1.0 license.


