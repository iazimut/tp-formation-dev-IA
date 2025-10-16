# 🚀 Guide de Démarrage Rapide

## Installation en une commande

```powershell
pip install -r requirements.txt
```

## Utilisation

### Option 1 : Exécution complète (recommandé pour la première fois)

```powershell
# 1. Tester les données
python prepare_data.py

# 2. Lancer l'optimisation (prend 3-5 minutes)
python optimize.py

# 3. Générer les graphiques
python visualize.py

# 4. Entraîner le modèle final
python train_final.py
```

### Option 2 : Utilisation rapide (si l'optimisation est déjà faite)

```powershell
# Voir le modèle final
python train_final.py

# Voir les graphiques
python visualize.py
```

## Dashboard Interactif

```powershell
# Lancer le dashboard
optuna-dashboard sqlite:///optuna_study.db

# Ouvrir dans le navigateur
start http://localhost:8080
```

**Pour arrêter le dashboard :** Appuyez sur `Ctrl+C` dans le terminal

## 📊 Ce que vous devriez voir

### 1. Optimisation (optimize.py)
- 50 trials en ~3-5 minutes
- Score final : ~96.26%

### 2. Modèle final (train_final.py)
- Précision : 96%
- Matrice de confusion : [[40, 3], [1, 70]]

### 3. Dashboard (http://localhost:8080)
- Graphiques interactifs
- Historique des trials
- Importance des paramètres

## ❓ Problèmes courants

### Le dashboard ne démarre pas
```powershell
# Vérifier si le port 8080 est déjà utilisé
netstat -ano | findstr :8080

# Si oui, arrêter le processus ou utiliser un autre port
optuna-dashboard sqlite:///optuna_study.db --port 8081
```

### Erreur d'import
```powershell
# Réinstaller les dépendances
pip install -r requirements.txt --upgrade
```

### L'optimisation prend trop de temps
Modifiez `optimize.py` ligne 48 :
```python
study.optimize(objective, n_trials=10)  # Au lieu de 50
```

## 🎯 Prochaines Étapes

1. ✅ Parcourir le dashboard interactif
2. 📊 Analyser les graphiques générés
3. 🔬 Modifier les hyperparamètres dans `optimize.py`
4. 🚀 Relancer l'optimisation avec vos propres paramètres
5. 💡 Essayer avec vos propres données

Bon apprentissage ! 🎉

