# Scripte automate
## Présentation
Ce dossier regroupe tout ce qui concerne les Unitées (unit).
## Organisation

|Dossiers / Fichiers|Description|
|---|---|
|/datas|Dossier dans lequel seront stocker les fichier générés lors de l'aggrégation|
|aggregor.py| Script pour récupérer les données des automates et les enregistrer dans un fichier.|
|automate.json|Contient les informations pour aggréger les données des automates (ce fichier n'est pas obligatoire)|
|dbStorage.py|Script pour enregistrer les données des fichiers vers la base de donnée.|
|Dockerfile|Fichier de configuration docker pour générer l'image d'une unité|

## Commandes
* Lancement de l'aggregation avec fichier de configuration (automate.json) : `python aggregor.py [unitId]`
* Lancement de l'aggregation sans fichier de configuration : `python aggregor.py [unitId] [automate1Address] [automate1Port] [automat1Id] [automate2Address] [automate2Port] [automat2Id] ...`
* Lancement de l'enregistrement en base de données : `python dbStorage.py [dbAddress] [login] [password] [dbPort]`