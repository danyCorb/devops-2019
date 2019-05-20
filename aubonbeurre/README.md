# Brique logiciel Docker-web
## Présentation
Cette partie du projet permet de gérer le coté web. Elle regroupe le serveur API, le projet vuejs et le docker (+configuration) nginx.

## Organisation

|Dossier / Fichiers|Description|
|---|---|
|aubonbeurre-api|Projet express js pour accéder aux données de la base de données et les envoyer vers le vue|
|aubonbreurre-dataviz|Projet vuejs pour l'interface web client|
|nginx| Fichier docker de nginx et fichiers de configurations|
|docker-compose.yml| script de déploiement des docker pour le fonctionnement du service web|

## Docker compose
* Lance aubonbeurre-api inaccessible autrement que par un docker.
* Lance le serveur vue sur le port 8080.
* Lance le nginx-reverse proxy sur le 80 et redirige les flux http:80 sur http:8080 (le vuejs)

