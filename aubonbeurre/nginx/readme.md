# Nginx
## Présentation
Ce dossier regroupe ce qui concerne le serveur nginx.
## Organisation

|Fichiers|Description|
|-|-|
|Dockerfile|Fichier docker pour la génération de l'image|
|nginx.conf|Fichier de configuration utiliser par nginx|
|proxy.conf|Fichier pour le proxy. Permet de spécifier les headers|

## Notes
* Connnexions max : 4096
* Port 80 redirigé vers vue-server:8080
* Port 3009 redirigé vers au_bon_beurre_api:3009