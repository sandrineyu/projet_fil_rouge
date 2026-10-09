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
2. Installer les dépendances : `pip install pandas numpy pyarrow jupyter`
3. Ouvrir le dossier `projet_fil_rouge` en entier (Jupyter ou VS Code), puis ouvrir `groupeD_extraction.ipynb`.
4. Faire `Kernel > Restart & Run All`.

Aucune autre action manuelle n'est nécessaire : les données sont déjà dans `data/`.

## Sorties produites

- `data/processed/base_clean.parquet` : jeu nettoyé, avec la colonne `split` (train = mois 0 à 5, test = mois 6 et 7). Il n'est pas versionné (63 Mo) et se régénère à chaque exécution.
- `lineage.json` : source, URL, date de récupération, version, SHA-256, transformations.

## Livrables

Data Canvas et slides : dossier `docs/`. Usage de l'IA : annexe du Data Canvas.
