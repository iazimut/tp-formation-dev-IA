# LangChain Tutorial

Formation pratique à LangChain : RAG et Agents avec Python.

## Prérequis

- Python 3.10+
- Clé API Groq (gratuite sur [console.groq.com](https://console.groq.com))
- Clé API JCDecaux (pour l'agent vélos)

## Installation

```bash
# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Installer les dépendances
pip install langchain langchain-groq langchain-community langchain-huggingface
pip install faiss-cpu sentence-transformers
pip install python-dotenv numexpr requests
```

## Configuration

Créer un fichier `.env` à la racine :

```
GROQ_API_KEY=gsk_votre_cle_groq
JCDECAUX=votre_cle_jcdecaux
```

## Contenu

### Notebooks

| Notebook | Description |
|----------|-------------|
| `rag1.ipynb` | RAG complet : chargement, chunking, embeddings, retriever, chaîne LCEL |
| `agent1.ipynb` | Agent avec outils personnalisés (calcul, description) |
| `agent2.ipynb` | Agent VéloStan avec API JCDecaux |
| `agent3_langgraph.ipynb` | Agent avancé avec LangGraph |

### Données

- `data/reglement_interieur_enhanced.txt` : Règlement de copropriété (base de connaissances pour le RAG)

### Exercices

- `exercices/exercice_rag.md` : Exercice pratique sur le RAG
- `exercices/exercice_agent.md` : Exercice pratique sur les agents

## Concepts clés

### RAG (Retrieval-Augmented Generation)

```
Document → Chunks → Embeddings → VectorStore → Retriever → LLM → Réponse
```

### Agent

```
Question → LLM → Choix d'outil → Exécution → LLM → Réponse
```

## Ressources

- [Documentation LangChain](https://python.langchain.com/)
- [Groq Cloud](https://console.groq.com/)
- [API JCDecaux](https://developer.jcdecaux.com/)

