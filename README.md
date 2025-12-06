README – Data Formats & Python Data Structures Assignment
📌 Description

Ce projet démontre la compréhension de plusieurs concepts fondamentaux en Python, incluant :

Différents formats de données : JSON, CSV, YAML, XML

Structures Python : TypedDict, namedtuple, dataclass, Pydantic

Différences entre Python lists et NumPy arrays

Mesure du temps d’exécution via un decorator

Comparaison de performances : multiplication scalaire → Python list vs NumPy

Chargement d’un fichier CSV avec Pandas

Travail structuré avec un repository Git

Ce projet répond aux exigences de l’assignment demandé.

📁 Structure du Projet
project/
│
├── data/
│   ├── user.json
│   ├── user.csv
│   ├── user.yaml
│   └── user.xml
│
├── src/
│   └── assignment.py
│
├── README.md
│
└── requirements.txt

📦 Installation et Dépendances

Créer un environnement virtuel (OPTIONNEL mais recommandé) :

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# OU
.\.venv\Scripts\activate    # Windows


Installer les dépendances :

pip install -r requirements.txt


Fichier requirements.txt recommandé :

pandas
numpy
pydantic
pyyaml

📂 1. Example Data Files

Les fichiers se trouvent dans le dossier /data :

user.json

user.csv

user.yaml

user.xml

Chaque fichier contient les mêmes données utilisateurs dans différents formats.

🧱 2. Python Data Structures

Le fichier src/assignment.py contient l’implémentation de :

TypedDict

namedtuple

dataclass

Pydantic model

⚡ 3. NumPy vs Python Lists

Le script compare :

une multiplication scalaire × liste Python

une multiplication scalaire × tableau NumPy

Avec un decorator @timer qui mesure le temps d’exécution.

📊 4. CSV Loaded in Pandas

Le fichier user.csv est chargé dans un DataFrame :

df = pd.read_csv("data/user.csv")
print(df)

▶️ Exécution du script

Depuis la racine du projet :

python src/assignment.py

📤 5. Git Workflow (commands)

Voici les commandes utilisées pour ce projet :

Initialisation du repo
git init

Ajouter les fichiers
git add .

Commit
git commit -m "Initial commit – data formats and Python structures assignment"

Ajouter un remote GitHub
git remote add origin https://github.com/<username>/<repo-name>.git

Push vers GitHub
git push -u origin main

🧪 Test Rapide

Pour vérifier que NumPy et Pandas sont bien installés :

python -c "import numpy; import pandas; print('OK')"

✔️ Résultats Attendus
⏱ Mesure du temps

NumPy est beaucoup plus rapide que les listes Python

Le decorator affiche quelque chose comme :

multiply_python_list took 0.250431 seconds
multiply_numpy_array took 0.004182 seconds

📄 Pandas DataFrame affiché :
   id   name               email  age         roles
0   1  Alice  alice@example.com   25  admin;editor
1   2    Bob    bob@example.com   30        viewer
