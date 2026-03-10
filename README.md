# HorrorBot Tutorial — RAG Pipeline de A à Z

Tutoriel pratique pour construire un pipeline **RAG (Retrieval-Augmented Generation)**
appliqué aux films d'horreur.

## Contenu

| Notebook | Durée | Thème |
| -------- | ----- | ----- |
| `01_embeddings.ipynb` | 35 min | Embeddings, similarité cosinus, recherche sémantique |
| `02_intent_classification.ipynb` | 35 min | Classification d'intention (TF-IDF vs Embeddings + SVM) |
| `03_mini_rag_pipeline.ipynb` | 35 min | Pipeline RAG complet avec LLM (simulé ou Ollama) |

## Prérequis

- **Python 3.10+**
- **uv** — gestionnaire de paquets Python moderne
  ([installation](https://docs.astral.sh/uv/getting-started/installation/))

## Installation

```bash
# Installer uv (si pas déjà fait)
# Windows (PowerShell) :
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux / macOS :
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# Cloner le projet et installer les dépendances
git clone <url-du-repo>
cd horrorbot-tutorial
uv sync
```

`uv sync` crée automatiquement un environnement virtuel (`.venv`) et installe
toutes les dépendances du projet.

## Lancer les notebooks

```bash
uv run jupyter notebook
```

## Dataset

`horror_movies_dataset.json` contient des films d'horreur extraits de l'API TMDB
(titre, synopsis, note, date de sortie). Le script `fetch_horror_movies.py` permet
de le régénérer si nécessaire (clé API TMDB requise) :

```bash
cp env.example .env
# Éditer .env avec votre clé API TMDB
uv run python fetch_horror_movies.py
```

## Licence

MIT — Usage pédagogique. Voir [LICENSE](LICENSE).
