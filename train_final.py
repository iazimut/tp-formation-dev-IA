from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import optuna
from prepare_data import load_data

# Charger les données
X_train, X_test, y_train, y_test = load_data()

# Charger l'étude
study = optuna.load_study(
    study_name='breast_cancer_optimization',
    storage='sqlite:///optuna_study.db'
)

# Récupérer les meilleurs hyperparamètres
best_params = study.best_params

# Créer le modèle final
model = RandomForestClassifier(
    n_estimators=best_params['n_estimators'],
    max_depth=best_params['max_depth'],
    min_samples_split=best_params['min_samples_split'],
    min_samples_leaf=best_params['min_samples_leaf'],
    random_state=42,
    n_jobs=-1
)

# Entraîner le modèle
model.fit(X_train, y_train)

# Évaluer sur l'ensemble de test
y_pred = model.predict(X_test)

print("Rapport de Classification :")
print(classification_report(y_test, y_pred))

print("\nMatrice de Confusion :")
print(confusion_matrix(y_test, y_pred))

