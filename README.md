# Projet fil rouge : Groupe D — Détection de la fraude à l'ouverture de compte

**Module 1 : Data Canvas, extraction et traçabilité des données**

## Contenu du dépôt

- **Data Canvas & cadrage** : cadrage du projet et description du besoin (PDF)
- **Notebook d'extraction** : code d'extraction et de contrôle qualité des données
- **Slides de présentation** : support de présentation du module (PDF)
- **Traçabilité** : lignage des données (`lineage.json`), généré par le notebook

## Structure du dépôt

```
projet_fil_rouge/
├── README.md
├── notebooks/
│   └── groupeD_extraction.ipynb
├── docs/
│   ├── Data Canvas (groupe D).pdf
│   └── Slides (groupe D).pdf
└── outputs/
    ├── Base.csv                  (non versionné, voir « Données »)
    ├── lineage.json
    ├── rapport_qualite.json
    └── dictionnaire_variables.csv
```

| Dossier | Rôle |
|---|---|
| `notebooks/` | Code source : le notebook qui produit les résultats |
| `docs/` | Livrables rédigés : Data Canvas et slides |
| `outputs/` | Fichiers de données et résultats : base, lignage, rapport qualité, dictionnaire des variables |

## Données

Le fichier `Base.csv` (environ 203 Mo) n'est **pas inclus dans le dépôt** : il dépasse la limite de taille de GitHub (100 Mo par fichier).

1. Télécharger le jeu de données sur Kaggle : **[lien du dataset à compléter]**
2. Vérifier que le fichier s'appelle exactement `Base.csv` (renommer si besoin)
3. Le placer dans le dossier `outputs/`

## Instructions pour lancer le code

1. Cloner le dépôt :
```bash
   git clone https://github.com/sandrineyu/projet_fil_rouge.git
   cd projet_fil_rouge
```
2. Placer `Base.csv` dans `outputs/` (voir la section « Données »)
3. Ouvrir `notebooks/groupeD_extraction.ipynb`
4. Exécuter `Kernel > Restart & Run All`

Les fichiers générés (`lineage.json`, `rapport_qualite.json`, `dictionnaire_variables.csv`) sont écrits dans `outputs/`.

## Équipe

Groupe D : **[noms des membres à compléter]**
