# Exercice : Créer un Agent

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
   pip install langchain langchain-groq python-dotenv
   ```

---

## Énoncé

Créez un **agent** capable de lancer des dés pour un jeu de rôle. 🎲

L'utilisateur doit pouvoir demander :
- *"Lance un dé à 6 faces"*
- *"Lance un dé à 20 faces"*
- *"Lance un dé à 100 faces"*

Et l'agent doit utiliser un **outil** pour effectuer le lancer et répondre avec le résultat.

---

## Consignes

1. Créer une **fonction Python** qui lance un dé avec un nombre de faces donné
2. Créer un **agent** qui utilise cette fonction comme outil
3. Tester l'agent avec une question

---

## Rappels

**Créer un outil** :
```python
def mon_outil(parametre: str) -> str:
    """La docstring est IMPORTANTE : elle explique l'outil au LLM."""
    # votre code
    return resultat
```

**Créer un agent** :
```python
agent = create_agent(
    model=llm,
    tools=[mon_outil],
    system_prompt="Description du rôle de l'agent"
)
```

**Invoquer l'agent** :
```python
result = agent.invoke({"messages": [{"role": "user", "content": "Ma question"}]})
print(result["messages"][-1].content)
```
