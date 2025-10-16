from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import pandas as pd

def load_data():
    """Charger les données de cancer du sein"""
    # On charge le dataset (c'est inclus dans scikit-learn)
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name='target')

    # On divise en train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data()
    print(f"Données d'entraînement : {X_train.shape}")
    print(f"Données de test : {X_test.shape}")

