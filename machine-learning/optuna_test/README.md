# Exercice Optuna - Optimisation Random Forest

Petit projet d'apprentissage pour découvrir **Optuna** : optimisation des hyperparamètres d'un Random Forest sur le dataset Breast Cancer.

## Résultats

- **Précision obtenue :** 96.26%
- **Nombre de trials :** 50

**Meilleurs hyperparamètres trouvés :**
```python
{
    'n_estimators': 196,
    'max_depth': 22,
    'min_samples_split': 3,
    'min_samples_leaf': 1
}
```

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
# 1. Lancer l'optimisation (3-5 minutes)
python optimize.py

# 2. Générer les graphiques
python visualize.py

# 3. Entraîner le modèle final
python train_final.py

# 4. Dashboard interactif (optionnel)
optuna-dashboard sqlite:///optuna_study.db
```

## Fichiers

- `prepare_data.py` - Chargement des données
- `optimize.py` - Optimisation avec Optuna
- `visualize.py` - Génération des graphiques
- `train_final.py` - Entraînement du modèle final

## Ressources

- [Documentation Optuna](https://optuna.readthedocs.io)
- [Scikit-learn](https://scikit-learn.org)
