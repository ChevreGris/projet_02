Projet 02 du cursus Python d'OpenClassrooms, 2021.

# BookScraper

Ce script récupére les données du site [Books to Scrape](https://books.toscrape.com/) dans un fichier csv.
Chaques catégories du site a son dossier, dans lequel ce trouve le fichier csv, ainsi que toutes les images jpeg de chaques livres.

## Utilisation
Python3 doit être installé correctement.
Depuis la racine du projet, créer un environement virtuel et lancer le script:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scrapper/__main__.py
```

Les données se retrouve dans le dossier `Script_results` du répertoire courant.
