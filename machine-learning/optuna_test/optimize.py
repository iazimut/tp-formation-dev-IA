import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from prepare_data import load_data

def objective(trial):
    """
    Fonction objectif pour Optuna
    
    Cette fonction :
    1. Suggère des hyperparamètres
    2. Crée un modèle avec ces hyperparamètres
    3. Évalue le modèle
    4. Retourne le score à optimiser
    """
    # Charger les données
    X_train, X_test, y_train, y_test = load_data()
    
    # Suggérer des hyperparamètres
    n_estimators = trial.suggest_int('n_estimators', 10, 200)
    max_depth = trial.suggest_int('max_depth', 2, 32)
    min_samples_split = trial.suggest_int('min_samples_split', 2, 20)
    min_samples_leaf = trial.suggest_int('min_samples_leaf', 1, 10)
    
    # Créer le modèle avec les hyperparamètres suggérés
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=42,
        n_jobs=-1
    )
    
    # Évaluer le modèle avec validation croisée
    scores = cross_val_score(
        model, X_train, y_train, 
        cv=5, scoring='accuracy', n_jobs=-1
    )
    
    # Retourner le score moyen
    return scores.mean()

if __name__ == "__main__":
    # Créer une étude Optuna
    study = optuna.create_study(
        study_name='breast_cancer_optimization',
        direction='maximize',  # Maximiser la précision
        storage='sqlite:///optuna_study.db',
        load_if_exists=True
    )
    
    # Lancer l'optimisation
    study.optimize(objective, n_trials=50)
    
    # Afficher les résultats
    print("\nMeilleurs hyperparamètres :")
    print(study.best_params)
    print(f"\nMeilleur score : {study.best_value:.4f}")

