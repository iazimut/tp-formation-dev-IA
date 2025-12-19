# Exercice : Créer un RAG

## Prérequis

1. **Créer une clé API Groq** (gratuit) :
   - Aller sur [console.groq.com](https://console.groq.com)
   - Créer un compte (avec Google ou GitHub)
   - Dans **API Keys**, cliquer sur **Create API Key**
   - Copier la clé générée

2. **Créer un fichier `.env`** à la racine du projet :
   ```
   GROQ_API_KEY=votre_clé_ici
   ```

3. **Installer les dépendances** :
   ```bash
   pip install langchain langchain-groq langchain-community python-dotenv faiss-cpu sentence-transformers
   ```

---

## Énoncé

Créez un **système RAG** qui permet de poser des questions sur un document de votre choix. 📄

Par exemple, vous pouvez utiliser :
- Un article Wikipédia copié dans un fichier `.txt`
- Un extrait de documentation technique
- Un texte inventé sur un sujet qui vous plaît

L'utilisateur doit pouvoir poser des questions et obtenir des réponses basées **uniquement** sur le contenu du document.

---

## Consignes

1. Créer ou récupérer un document avec du contenu (quelques paragraphes)
2. **Charger** le document avec un Loader
3. **Découper** le document en chunks
4. Créer un **vectorstore** et un **retriever**
5. Créer la **chaîne RAG** (retriever → prompt → LLM)
6. Tester avec une question

---

## Rappels

**Les étapes du RAG** :
```
Document → Loader → Splitter → Embeddings → VectorStore → Retriever → Prompt + LLM → Réponse
```

**Composants utiles** :
- `TextLoader` : charge un fichier texte
- `RecursiveCharacterTextSplitter` : découpe en chunks
- `HuggingFaceEmbeddings` : convertit le texte en vecteurs
- `FAISS` : stocke et recherche les vecteurs
- `ChatPromptTemplate` : crée le prompt avec `{context}` et `{question}`

---

## Questions à se poser

- Quelle **taille de chunk** choisir pour mon document ?
- Combien de chunks (**k**) récupérer pour avoir assez de contexte ?
- Comment formuler le **prompt** pour que le LLM réponde bien ?