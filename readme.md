# Projet devops Au Bon Beurre
## Présentation
Le projet a pour objectif de fournir une solution fonctionnelle à l'enteprise Au Bon Beurre pour la détection efficace de problèmes liés à la sécurité sanitaire.  
## Architecture logiciel
Le projet est composé de 5 briques logiciel développées pour répondre au besoin.

|Nom|Localisation|Description|
|---|---|---|
|aubonbeurre-api|`/aubonbeurre/aubonbeurre-api`| Api pour récupérer les données de la base de donnée et les envoyer vers le Front|
|aubonbeurre-dataviz|`/aubonbeurre/aubonbeurre-dataviz`|Application *vue* pour accèder à l'interface graphique et consulter les données.|
|Automate-Generation|`script/automate`| Créer un serveur interne et communique les données de l'automate à chaque connexion|
|Unit-Agregation|`script/unit/aggregor.py`| Récupère les données des automates et créer un fichier chaque minute|
|Unit-Storage|`script/unit/dbStorage.py`| Récupère les données généré par *arggregor* et les envoies en base de données.
## Architecture Système
Le projet utilise 3 briques système qui peuvent êtres utilisé sur des OS différents.

|Nom|Localisation|Description|
|---|---|---|
|Docker-web| `/aubonbeurre/docker-compose.yml`| Composée des brique logiciels aubonbeurre-api, aubonbeurre-dataviz et d'un serveur web nginx.|
|Docker-factory|`script/docker-compose.yml`|Composée des briques pour simuler des automates et des unitées|
|Docker-MariaDB|`database/docker-compose.yml`|Utilisé pour créer un container MariaDB avec en login corentin.dupont et mot de passe XXX (pour le mod dev)
## Licence
Creative Common CC
Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 3.0 France (CC BY-NC-SA 3.0 FR) 

Toute reproduction ou utilisation sans l'accord des créateurs ci-dessous nommée est interdite.
Dany CORBINEAU dany.corbineau@ynov.com
Corentin DUPONT corentin.dupont@ynov.com