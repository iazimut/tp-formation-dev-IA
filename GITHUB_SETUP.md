# 🚀 Guide de Mise en Ligne sur GitHub

## ✅ Étape 1 : Préparation (Déjà fait !)

Le dépôt Git local est déjà initialisé et le premier commit est créé.

## 📝 Étape 2 : Créer le dépôt sur GitHub

1. Allez sur [GitHub](https://github.com)
2. Cliquez sur le bouton **"New"** ou **"+"** en haut à droite
3. Remplissez les informations :
   - **Repository name** : `optuna-breast-cancer-classification`
   - **Description** : `Optimisation d'hyperparamètres avec Optuna pour la classification de cancer du sein (96% de précision)`
   - **Visibility** : Public ou Private (selon votre préférence)
   - ⚠️ **NE COCHEZ PAS** "Add a README" (on en a déjà un)
   - ⚠️ **NE COCHEZ PAS** "Add .gitignore" (on en a déjà un)
4. Cliquez sur **"Create repository"**

## 🔗 Étape 3 : Lier le dépôt local à GitHub

Une fois le dépôt créé sur GitHub, vous verrez des instructions. Utilisez ces commandes :

```powershell
# Ajouter le remote GitHub (remplacez YOUR_USERNAME par votre nom d'utilisateur)
git remote add origin https://github.com/YOUR_USERNAME/optuna-breast-cancer-classification.git

# Renommer la branche en 'main' (optionnel, si vous préférez 'main' à 'master')
git branch -M main

# Pousser le code sur GitHub
git push -u origin main
```

**Ou si vous gardez 'master' :**

```powershell
git remote add origin https://github.com/YOUR_USERNAME/optuna-breast-cancer-classification.git
git push -u origin master
```

## 🔐 Authentification

Si GitHub vous demande de vous authentifier :

### Option 1 : Token Personnel (Recommandé)
1. Allez dans **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**
2. Cliquez sur **Generate new token (classic)**
3. Sélectionnez **repo** (accès complet aux dépôts)
4. Générez et copiez le token
5. Utilisez ce token comme mot de passe lors du push

### Option 2 : GitHub CLI
```powershell
# Installer GitHub CLI
winget install --id GitHub.cli

# Se connecter
gh auth login

# Pousser le code
git push -u origin main
```

## 📊 Étape 4 : Vérifier

Une fois poussé, allez sur votre dépôt GitHub. Vous devriez voir :
- ✅ Tous les fichiers Python
- ✅ README.md affiché automatiquement
- ✅ Les graphiques PNG
- ✅ Le fichier .gitignore

## 🎨 Étape 5 : Améliorer le dépôt (Optionnel)

### Ajouter des Topics
Sur la page du dépôt, cliquez sur la roue dentée à côté de "About" et ajoutez :
- `optuna`
- `machine-learning`
- `hyperparameter-optimization`
- `scikit-learn`
- `random-forest`
- `python`
- `breast-cancer`

### Ajouter un Badge
Ajoutez ceci au début du README.md :

```markdown
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Optuna](https://img.shields.io/badge/optuna-4.5.0-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
```

### Activer GitHub Pages (si vous voulez un site web)
1. Allez dans **Settings** > **Pages**
2. Sélectionnez la branche **main** ou **master**
3. Votre README sera visible comme site web

## 🔄 Commandes Git Utiles pour la Suite

```powershell
# Voir l'état des fichiers
git status

# Ajouter des modifications
git add .

# Créer un commit
git commit -m "Description des changements"

# Pousser les changements
git push

# Récupérer les changements
git pull

# Voir l'historique
git log --oneline --graph

# Créer une nouvelle branche
git checkout -b nouvelle-fonctionnalite

# Revenir à la branche principale
git checkout main
```

## 📦 Fichiers Ignorés

Le fichier `.gitignore` empêche ces fichiers d'être versionnés :
- ✅ `optuna_study.db` (trop gros et spécifique à chaque exécution)
- ✅ `__pycache__/` (fichiers Python compilés)
- ✅ `*.pyc` (bytecode Python)
- ✅ `.vscode/`, `.idea/` (configurations IDE)

## 🌟 Exemple de URL Final

Votre projet sera accessible à :
```
https://github.com/YOUR_USERNAME/optuna-breast-cancer-classification
```

## 🎉 C'est tout !

Une fois sur GitHub, vous pourrez :
- 📤 Partager votre travail avec d'autres
- 🌟 Recevoir des stars
- 🔄 Collaborer avec d'autres développeurs
- 📝 Documenter vos expériences dans les Issues
- 🚀 Continuer à améliorer le projet

---

**Besoin d'aide ?** Consultez la [documentation GitHub](https://docs.github.com/fr)

