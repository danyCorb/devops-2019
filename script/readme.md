# Brique système Docker-factory
## Présentation
Cette partie de projet permet de gérer la partie création des données, aggrégation des données et sauvegarde des données en base de données.
## Organisation

| Dossier / Fichier | Description |
| --- | --- |
| docker-compose.yml | Lance 5 automates sur les ports 8001, 8002, 8003, 8004 et 8005. Lance une unité d'aggregation et une unité dbStorage |
| automate | Créer un serveur et envoi les données aléatoire d'un automate a chaque connexion |
| unit | Récupère les données des automates et les aggrèges en 1 fichier chaque minute. Envoi les données des fichiers en base de données |

## Docker compose
* Lance 5 automates sur les ports 8001, 8002, 8003, 8004,8005
* Lance 1 unit d'aggregation connecté au 5 automates avec un volume bind sur le dossier datas
* Lance 1 unit de dbStorage avec un volume bind sur le dossier datas. La base de données ce trouve sur dany-corbineau.ddns.net:8001 
