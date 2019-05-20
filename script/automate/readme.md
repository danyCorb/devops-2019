# Scripte automate
## Presentation
Ce dossier regroupe tout ce qui concerne les automates.
## Organisation

|Dossiers / Fichiers|Description|
|---|---|
|automate.json|Fichier json de configuration pour permettre au run.py de lancer plusieurs automates|
|AutomateRecording.py|Class AutomateRecording pour donner une forme objet aux enregistrements des automates.|
|Dockerfile|Fichier docker pour générer une image pour 1 automate|
|generator.py| Script d'entrée pour lancer un automate.|
|run.py|Script de lancement de plusieurs automates simultanément|

## Commandes
* Lancement d'automates défini par automate.json : `python run.py`
* Lancement d'un automate: `python generator.py [automateId] [serverPortNumber]`
