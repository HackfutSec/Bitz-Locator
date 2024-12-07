Bitz Pro 2.0: Localisation de Numéros de Téléphone
Bitz Pro 2.0 est un programme Python qui permet de localiser un numéro de téléphone et de fournir des informations détaillées sur sa localisation, y compris la latitude, la longitude, le pays, la ville, et le fournisseur de service. Il utilise plusieurs bibliothèques Python et services d'API tels que phonenumbers, OpenCage Geocode, et Folium pour effectuer les différentes étapes de l'analyse.

Fonctionnalités :
Localisation du numéro de téléphone : Analyse le numéro de téléphone pour déterminer sa localisation géographique (pays, ville, fournisseur).
Fournisseur de service : Identifie le fournisseur du numéro de téléphone à partir de sa signature.
Génération d'une carte interactive : Utilise Folium pour créer une carte interactive à partir des coordonnées géographiques et sauvegarde la carte sous forme de fichier HTML.
Lien Google Maps : Fournit un lien direct vers la localisation sur Google Maps.
Utilisation de l'API OpenCage : Permet de récupérer des informations géographiques détaillées sur la localisation à partir de l'API OpenCage Geocoder.
Prérequis :
Avant de lancer le programme, vous devez installer les dépendances suivantes :

phonenumbers
folium
requests
opencage
Pour installer les dépendances, vous pouvez utiliser la commande suivante :

bash
Copier le code
pip install phonenumbers folium requests opencage
Utilisation :
Lancez le script.
Entrez le numéro de téléphone que vous souhaitez localiser. Assurez-vous qu'il soit au format international, par exemple : +33XXXX.
Entrez votre clé API OpenCage pour obtenir des informations géographiques détaillées. Si vous n'en avez pas, vous pouvez en obtenir une gratuitement en vous inscrivant sur le site d'OpenCage.
Le programme vous affichera :
La localisation géographique du numéro.
Le fournisseur de service associé au numéro.
Une carte interactive avec le marquage de la localisation.
Un lien vers la localisation sur Google Maps.
Le programme génère un fichier cartefound.html contenant la carte interactive que vous pouvez visualiser dans votre navigateur.
Exemple d'usage :
bash
Copier le code
$ python location_tool.py
[!] Entrer le numéro à localiser (format international, ex: +33XXXX): +33123456789
[!] Localisation: France, Paris
[!] Fournisseur de service: Orange
...
[!] Carte sauvegardée sous: cartefound.html
[!] Lien vers Google Maps: https://www.google.com/maps/place/48.8566,2.3522
Avertissements :
Utilisation responsable : Ce programme est destiné à des fins éducatives. L'auteur ne se tient pas responsable de l'utilisation malveillante du programme.
Clé API OpenCage : Vous devez disposer d'une clé API valide pour interroger l'API OpenCage. Vous pouvez obtenir une clé gratuite sur leur site web.
License :
MIT License : Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.
Contact :
Auteur : Hackfut
Contact : Telegram
