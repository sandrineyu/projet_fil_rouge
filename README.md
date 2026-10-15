# Projet fil rouge : Groupe D (fraude à l'ouverture de compte)

## Source des données

Bank Account Fraud Dataset Suite (Feedzai, NeurIPS 2022), fichier `Base.csv`
- Source : https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips2022
- Documentation : https://github.com/feedzai/bank-account-fraud (datasheet : `documents/datasheet.pdf`)
- Licence : CC BY-NC-SA 4.0 (usage non commercial, attribution à Feedzai)
- Accès : `Base.csv` (213 Mo) a été téléchargé manuellement sur Kaggle, puis découpé en 3 parties (`data/dataset_part1.csv`, `dataset_part2.csv`, `dataset_part3.csv`) pour respecter la limite de 100 Mo de GitHub. Le notebook d'extraction vérifie par SHA-256 que les 3 parties, recollées, redonnent exactement le fichier d'origine.

**Granularité** : 1 ligne = 1 demande d'ouverture de compte (1 000 000 de demandes sur 8 mois, environ 1,1 % de fraude).

## Contenu du dépôt

```
projet_fil_rouge/
├── data_extraction.ipynb        # Module 1 : extraction, contrôle qualité, lineage
├── lineage.json                 # journal de traçabilité (généré par data_extraction.ipynb)
├── requirements.txt             # dépendances Python
├── data/
│   ├── dataset_part1-3.csv      # données brutes (Base.csv découpé en 3)
│   └── processed/               # dictionnaire des variables, rapport qualité
├── src/
│   ├── build_duckdb.py          # construit la base DuckDB à partir des 3 parties
│   ├── data_exploration.ipynb   # Module 2 : SQL (DuckDB)
│   └── EDA.ipynb                # Module 2 : EDA, hypothèses, pipeline, évaluation
├── models/                      # pipeline de référence (joblib) et seuil retenu
└── docs/                        # Data Canvas et slides (PDF)
```

## Installation

Python 3.12 ou plus récent.

```bash
git clone https://github.com/sandrineyu/projet_fil_rouge.git
cd projet_fil_rouge
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

Ouvrir le dossier `projet_fil_rouge` en entier dans VS Code ou Jupyter. Aucun téléchargement n'est nécessaire : les données sont déjà dans `data/`.

## Ordre d'exécution

1. **`data_extraction.ipynb`** (module 1) : `Kernel > Restart & Run All`. Produit `data/processed/base_clean.parquet` et `lineage.json`.
2. **`python src/build_duckdb.py`** : fusionne les 3 parties et construit `data/fraud.duckdb`.
3. **`src/data_exploration.ipynb`** (module 2, SQL) : requêtes DuckDB (qualité, agrégations, fonctions de fenêtre). Nécessite l'étape 2.
4. **`src/EDA.ipynb`** (module 2) : EDA, hypothèses, découpage temporel, pipeline, évaluation. Produit `models/pipeline_reference.joblib` et `models/seuil.json`.

Exemple de requête :
```python
import duckdb
con = duckdb.connect("data/fraud.duckdb", read_only=True)
con.sql("SELECT month, count(*) AS demandes, avg(fraud_bool) AS taux_fraude FROM applications GROUP BY month ORDER BY month").show()
```

## Fichiers générés (non versionnés)

`data/processed/base_clean.parquet`, `data/fraud.duckdb`, `data/dataset.csv`, `data/dataset_clean.csv`.
