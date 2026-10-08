# Projet fil rouge : Groupe D

MBA 2 Data & BI, Epitech. Module 1 : fraude à l'ouverture de compte.

## Contenu du dépôt

- `groupeD_extraction.ipynb` : notebook d'extraction et de contrôle qualité
- `lineage.json` : journal de traçabilité des données (généré par le notebook)
- `docs/` : Data Canvas et slides en PDF
- `data/processed/` : fichiers produits par le notebook (dictionnaire des variables, rapport qualité)

## Lancer le notebook

1. Cloner le dépôt :
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
