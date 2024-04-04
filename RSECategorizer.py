# RSECategorizer.py

from transformers import pipeline
import pandas as pd

# Charger le pipeline de classification avec un modèle léger
classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

def classify_rse_actions(descriptions):
    categories = [
        "La gouvernance de la structure",
        "Les droits humains",
        "Les conditions et relations de travail",
        "La responsabilité environnementale",
        "La loyauté des pratiques",
        "Les questions relatives au consommateur et à la protection du consommateur",
        "Les communautés et le développement local"
    ]
    
    classified_data = []
    for description in descriptions:
        # Classification de chaque description
        result = classifier(description, categories)
        # Récupération de la catégorie avec la probabilité la plus élevée
        top_category = result['labels'][0]
        classified_data.append(top_category)
    
    return classified_data

# Exemple d'utilisation (à des fins de test, à commenter ou supprimer pour l'intégration finale)
# descriptions = ["Promotion de l'énergie renouvelable", "Amélioration des conditions de travail"]
# print(classify_rse_actions(descriptions))


