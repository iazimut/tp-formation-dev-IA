# Prédiction des Frais Médicaux

## Description
Ce projet utilise le machine learning pour prédire les frais médicaux annuels des patients en se basant sur diverses caractéristiques personnelles. Le modèle développé peut aider les assureurs et les établissements de santé à mieux estimer les coûts médicaux.

## Fonctionnalités
- Analyse exploratoire des données
- Prétraitement et feature engineering
- Optimisation des hyperparamètres avec BayesSearchCV
- Comparaison de plusieurs modèles (Linear Regression, Ridge, Lasso, Random Forest, XGBoost)
- Visualisations détaillées des résultats
- Analyse de l'importance des features

## Technologies Utilisées
- Python 3.x
- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-optimize (skopt)

## Structure du Projet
- Le dossier `data` contient le fichier `insurance.csv` qui est la source de données pour ce projet.
- Le notebook `medical_expenses_prediction.ipynb` est le fichier principal de ce projet.
- Le fichier `README.md` est le fichier que vous lisez actuellement. Il contient des informations sur le projet, les fonctionnalités, les technologies utilisées et la structure du projet.

## Installation
Pour installer ce projet, veuillez cloner le dépôt GitHub suivant : https://github.com/seb54/prediction-frais-medicaux.git

## Utilisation
Pour utiliser ce projet, veuillez ouvrir le notebook `medical_expenses_prediction.ipynb` avec Jupyter Notebook.

## Variables du Dataset
- `age`: L'âge du patient.
- `sex`: Le sexe du patient (1 = homme, 0 = femme).
- `bmi`: L'indice de masse corporelle du patient.
- `children`: Le nombre d'enfants du patient.
- `smoker`: Si le patient est fumeur (1 = oui, 0 = non).
- `region`: La région du patient (4 catégories).
- `charges`: Les frais médicaux annuels du patient.

## Points Clés
1. **Prétraitement des Données**
   - Encodage des variables catégorielles
   - Normalisation des données numériques
   - Feature engineering avancé

2. **Modélisation**
   - Optimisation bayésienne des hyperparamètres
   - Validation croisée à 5 plis
   - Ensemble de modèles comparés

## Utilisation
1. Ouvrir le notebook `prediction-frais-medicaux.ipynb`
2. Exécuter les cellules dans l'ordre
3. Les résultats et visualisations seront générés automatiquement

