# Prédiction d'Éligibilité de Crédit Bancaire

## Description
Ce projet est un exercice utilisant le Machine Learning pour prédire l'éligibilité d'un client à un crédit bancaire. Il se base sur différentes caractéristiques du demandeur comme le revenu, l'historique de crédit, le statut matrimonial, etc.

## Structure du Projet

- racine/
  - data/
    - loan-data-673b233f1c1cb921157550.csv
  - model/
    - loan_prediction_model.joblib
  - sebastien_gerard_prediction_eligibilite_credit.ipynb
  - README.md
  - requirements.txt


## Fonctionnalités
- Analyse exploratoire des données
- Traitement des valeurs manquantes
- Encodage des variables catégorielles
- Normalisation des données
- Comparaison de différents modèles de ML
- Implémentation d'un modèle de régression logistique
- Sauvegarde et chargement du modèle

## Installation
1. Cloner le repository
bash
git clone [https://github.com/seb54/prediction-eligibilite-credit-banque.git]
2. Installer les dépendances

pip install -r requirements.txt

## Utilisation
1. Ouvrir le notebook Jupyter :

jupyter notebook sebastien_gerard_prediction_eligibilite_credit.ipynb

2. Pour utiliser le modèle sauvegardé :

```python
import joblib

# Charger le modèle
model = joblib.load('model/loan_prediction_model.joblib')

# Exemple de prédiction
sample_input = {
    'Gender': 'Male',
    'Married': 'Yes',
    'Dependents': '2',
    'Education': 'Graduate',
    'Self_Employed': 'No',
    'ApplicantIncome': 5000,
    'CoapplicantIncome': 2000,
    'LoanAmount': 200,
    'Loan_Amount_Term': 360,
    'Credit_History': 1,
    'Property_Area': 'Urban'
}
```

## Performance du Modèle
- Accuracy : 89%
- Performant sur la prédiction des prêts accordés

## Améliorations Possibles
- Feature Engineering supplémentaire
- Optimisation des hyperparamètres
- Gestion des outliers
- Test d'autres algorithmes (GradientBoosting, AdaBoost)


## Auteur
Sébastien GERARD



