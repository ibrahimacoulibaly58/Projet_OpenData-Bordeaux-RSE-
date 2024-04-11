
import requests

# URL de base de l'API bziiit
BASE_URL = "https://bziiitapi-api.azurewebsites.net"

def get_labels():
    # Récupère les labels RSE depuis l'API bziiit
    response = requests.get(f"{BASE_URL}/opendata/labels")
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return []

def get_rse_projects():
    # Récupère les projets RSE depuis l'API bziiit
    response = requests.get(f"{BASE_URL}/opendata/bordeaux-rse/projects")
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return []

def get_engaged_brands():
    # Récupère les marques engagées depuis l'API bziiit
    response = requests.get(f"{BASE_URL}/opendata/bordeaux-rse/brands")
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return []
