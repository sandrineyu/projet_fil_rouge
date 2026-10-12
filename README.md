# Projet fil rouge : Groupe D (fraude à l'ouverture de compte)

## Source des données

Bank Account Fraud Dataset Suite (Feedzai, NeurIPS 2022), fichier `Base.csv`
- Source : https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips2022
- Documentation : https://github.com/feedzai/bank-account-fraud
- Licence : CC BY-NC-SA 4.0 (usage non commercial, attribution à Feedzai)
- Accès : `Base.csv` (213 Mo) a été téléchargé manuellement sur Kaggle, puis découpé en 3 parties (`data/dataset_part1.csv`, `dataset_part2.csv`, `dataset_part3.csv`) pour respecter la limite de 100 Mo de GitHub. Le notebook vérifie par SHA-256 que les 3 parties, recollées, redonnent exactement le fichier d'origine.

**Granularité** : 1 ligne = 1 demande d'ouverture de compte (1 000 000 de demandes sur 8 mois, environ 1,1 % de fraude).

## Contenu du dépôt

```
projet_fil_rouge/
├── groupeD_extraction.ipynb   # notebook d'extraction et de contrôle qualité
├── lineage.json               # journal de traçabilité (généré par le notebook)
├── data/
│   ├── dataset_part1-3.csv    # données brutes (Base.csv découpé en 3)
│   └── processed/             # sorties du notebook
├── docs/                      # Data Canvas et slides (PDF)
└── src/                       # notebooks d'exploration (module 2)
```

## Lancer le notebook

1. Cloner le dépôt et se placer à la racine :
```bash
   git clone https://github.com/sandrineyu/projet_fil_rouge.git
   cd projet_fil_rouge
```
2. Installer les modules Python nécessaires (si besoin) :
```bash
   pip install pandas numpy pyarrow jupyter
```
3. Télécharger `Base.csv` (environ 213 Mo, trop volumineux pour GitHub) sur Kaggle :
   https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips2022
   puis le placer **à côté du notebook**, à la racine du dossier `projet_fil_rouge`
4. Ouvrir `groupeD_extraction.ipynb` depuis ce dossier (Jupyter ou VS Code)
5. Cliquer sur `Kernel > Restart & Run All`

Les fichiers générés sont écrits dans `data/processed/` et `lineage.json` à la racine.

## Base DuckDB

Le jeu de données brut est découpé en 3 fichiers (`data/dataset_part1.csv` à `part3.csv`).
Le script `src/build_duckdb.py` les fusionne et construit une base DuckDB interrogeable en SQL :

```bash
pip install duckdb
python src/build_duckdb.py
```

Sorties (non versionnées) :
- `data/dataset.csv` : les 3 parties fusionnées (1 000 000 lignes, 32 colonnes)
- `data/fraud.duckdb` : table `applications` (mêmes colonnes + `source_file`, le fichier d'origine)

Exemple de requête :
```python
import duckdb
con = duckdb.connect("data/fraud.duckdb", read_only=True)
con.sql("SELECT month, count(*) AS demandes, avg(fraud_bool) AS taux_fraude FROM applications GROUP BY month ORDER BY month").show()
```
