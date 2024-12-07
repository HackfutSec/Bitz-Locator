import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
import requests
import os
import sys
import time


os.system('cls')
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

banner = {'''
          
          #Author  : Hackfut
          #Contact : t.me/HackfutSec
          #License : MIT  
          #Key Api : 31e252c500824c59ba5976071afad9b0
          #Version : BITZ Pro 2.0
          [Warning] I am not responsible for the way you will use this program [Warning]
          __________.__  .__  __         .____                         __  .__               
          \______   \  | |__|/  |________|    |    ____   ____ _____ _/  |_|__| ____   ____  
            |    |  _/  | |  \   __\___   /    |   /  _ \_/ ___\\__  \\   __\  |/  _ \ /    \ 
            |    |   \  |_|  ||  |  /    /|    |__(  <_> )  \___ / __ \|  | |  (  <_> )   |  \\n
            |______  /____/__||__| /_____ \_______ \____/ \___  >____  /__| |__|\____/|___|  /
                   \/                    \/       \/          \/     \/                    \/ 
                                                      
                                    ██████╗░██╗████████╗███████╗
                                    ██╔══██╗██║╚══██╔══╝╚════██║
                                    ██████╦╝██║░░░██║░░░░░███╔═╝
                                    ██╔══██╗██║░░░██║░░░██╔══╝░░
                                    ██████╦╝██║░░░██║░░░███████╗
                                    ╚═════╝░╚═╝░░░╚═╝░░░╚══════╝
'''}

for col in banner:
    print(bcolors.GREEN + col, end="")
    sys.stdout.flush()
    time.sleep(0.00005)


# Entrée du numéro de téléphone
number = input(bcolors.RED + "\n[!] Entrer le numéro à localiser (format international, ex: +33XXXX): ")  # Remplacez par le numéro à analyser

# Analyse du numéro de téléphone
pepnumber = phonenumbers.parse(number)

# Récupération de la localisation
location = geocoder.description_for_number(pepnumber, 'fr')
print(bcolors.GREEN + "\n[!] Localisation:", location)

# Récupération du nom du fournisseur de service
service_pro = phonenumbers.parse(number)
service_provider = carrier.name_for_number(service_pro, 'fr')
print(bcolors.GREEN + "\n[!] Fournisseur de service:", service_provider)

# Demande de la clé API OpenCage
key = input(bcolors.RED + "\n[ OpenCage ] Entrez votre clé API GooLocate Premium: ")

try:
    # Initialisation de l'API OpenCage avec la clé API fournie
    geocoder_api = OpenCageGeocode(key)
    
    # Requête à OpenCage pour obtenir les coordonnées géographiques
    query = location
    results = geocoder_api.geocode(query)
    print(bcolors.GREEN + "\n..................................Information Detailler Sur l Emplacement de Location ..................................\n")
    time.sleep(0.0005)
    print(results)
    print(bcolors.GREEN + "\n..................................Information Precise Sur l Emplacement de Location ..................................\n")
    time.sleep(0.0005)

    # Vérifier si les résultats existent
    if results and len(results) > 0:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        # Récupérer le pays, la ville et d'autres informations à partir des résultats
        country = results[0]['components'].get('country', 'Inconnu')
        city = results[0]['components'].get('city', service_pro)
        service = results[0]['annotations'].get('ISP', service_provider)

        print(bcolors.GREEN + f"\n[!] Latitude: {lat}, Longitude: {lng}, Country: {country}, City: {city}, Service: {service}")


        # Création de la carte avec Folium
        mymap = folium.Map(location=[lat, lng], zoom_start=10)
        folium.Marker([lat, lng], popup=location).add_to(mymap)

        # Sauvegarde de la carte dans un fichier HTML
        print(bcolors.GREEN + "\n.................................. Information Sur la Sauvegarde du Fichier Mapping ..................................\n")
        time.sleep(0.0005)
        mymap.save("cartefound.html")
        print(bcolors.RED + "\n[!] Carte sauvegardée sous: cartefound.html")

        # Lien vers Google Maps
        print(bcolors.GREEN + "\n..................................Information Sur le Lien GoogleMap ..................................\n")
        time.sleep(0.0005)
        GoogleMap = bcolors.GREEN + f'https://www.google.com/maps/place/{lat}@{lng},16z'
        print(bcolors.GREEN + "\n[!] Lien vers Google Maps:", GoogleMap)
        print(bcolors.GREEN + "\n....................Fin de Localisation Veillez Patienter la Fermuture du Programme ....................\n")
        time.sleep(0.0900)
        
    else:
        print(bcolors.YELLOW + "[!] Aucun résultat trouvé pour la localisation.")
        
except requests.exceptions.RequestException as e:
    # Gestion des erreurs réseau liées à l'API OpenCage
    print(bcolors.YELLOW + f"\n[!] Erreur de connexion avec l'API OpenCage: {e}")
except ValueError as e:
    # Gestion des erreurs liées à des valeurs incorrectes dans la réponse de l'API
    print(bcolors.YELLOW + f"\n[!] Erreur avec la clé API ou les données reçues: {e}")
except Exception as e:
    # Gestion des autres types d'erreurs
    print(bcolors.YELLOW + f"\n[!] Une erreur inconnue est survenue: {e}")
