# Base de donnée
## Présentation
Ce dossier permet de gérer tout ce qui touche à la base de donnée.
## Organisation

|Fichiers / Dossier| Description|
|---|---|
|create_aubonbeurre_db.sql|Script de création / reset de la base de donnée|
|docker-composer.yml|Script docker compose de lancement du serveur de base de donnée.|
|insert_data_au_bon_beurre.sql|Script d'insertion des données de base (unités, automates, niveaux critiques)|

## Commande
* Lancement de la base de donnée : `docker-compose up`