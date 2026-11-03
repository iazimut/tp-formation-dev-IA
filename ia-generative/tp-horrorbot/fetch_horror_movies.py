"""Fetch horror movies from TMDB API for tutorial dataset.

Clé API TMDB gratuite :
  1. Créer un compte sur https://www.themoviedb.org/signup
  2. Aller dans https://www.themoviedb.org/settings/api
  3. Demander une clé API (type : Developer, usage : Education)
  4. Copier la valeur "Clé de l'API (v3 auth)"

Usage (3 méthodes au choix) :

  Méthode 1 — argument en ligne de commande :
    python fetch_horror_movies.py --api-key VOTRE_CLE_ICI

  Méthode 2 — fichier .env dans le même dossier :
    Créer un fichier .env contenant :
      TMDB_API_KEY=VOTRE_CLE_ICI
    Puis lancer :
      python fetch_horror_movies.py

  Méthode 3 — variable d'environnement :
    Linux/Mac : export TMDB_API_KEY="VOTRE_CLE_ICI"
    Windows   : set TMDB_API_KEY=VOTRE_CLE_ICI
    Puis lancer :
      python fetch_horror_movies.py
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

TMDB_BASE_URL = "https://api.themoviedb.org/3"
HORROR_GENRE_ID = 27
TOTAL_MOVIES = 50
OUTPUT_FILE = Path("horror_movies_dataset.json")


def _resolve_api_key(cli_key: str | None) -> str:
    """Resolve TMDB API key from CLI arg, .env file, or environment.

    Priority: CLI argument > .env file > environment variable.

    Args:
        cli_key: Key passed via --api-key argument (or None).

    Returns:
        The resolved API key.
    """
    # 1. CLI argument
    if cli_key:
        return cli_key

    # 2. .env file
    env_file = Path(".env")
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("TMDB_API_KEY="):
                value = line.split("=", 1)[1].strip().strip("\"'")
                if value:
                    return value

    # 3. Environment variable
    env_key = os.getenv("TMDB_API_KEY", "")
    if env_key:
        return env_key

    # Nothing found
    print("=" * 60)
    print("ERREUR : Clé API TMDB non trouvée.")
    print()
    print("3 façons de la fournir :")
    print()
    print("  1. python fetch_horror_movies.py --api-key VOTRE_CLE")
    print()
    print("  2. Créer un fichier .env contenant :")
    print("     TMDB_API_KEY=VOTRE_CLE")
    print()
    print("  3. Variable d'environnement :")
    print("     export TMDB_API_KEY=VOTRE_CLE")
    print()
    print("Clé gratuite sur : https://www.themoviedb.org/settings/api")
    print("=" * 60)
    sys.exit(1)


def _fetch_horror_page(api_key: str, page: int) -> list[dict]:
    """Fetch one page of horror movies sorted by vote count.

    Args:
        api_key: TMDB API v3 key.
        page: Page number to fetch.

    Returns:
        List of raw movie dicts from TMDB.
    """
    response = requests.get(
        f"{TMDB_BASE_URL}/discover/movie",
        params={
            "api_key": api_key,
            "with_genres": HORROR_GENRE_ID,
            "sort_by": "vote_count.desc",
            "vote_average.gte": 5.0,
            "vote_count.gte": 500,
            "language": "fr-FR",
            "page": page,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json().get("results", [])


def _normalize_movie(raw: dict) -> dict:
    """Extract and normalize relevant fields from TMDB result.

    Args:
        raw: Raw movie dict from TMDB API.

    Returns:
        Normalized movie dict with selected fields.
    """
    return {
        "id": raw["id"],
        "title": raw.get("title", ""),
        "original_title": raw.get("original_title", ""),
        "overview": raw.get("overview", ""),
        "release_date": raw.get("release_date", ""),
        "vote_average": raw.get("vote_average", 0.0),
        "vote_count": raw.get("vote_count", 0),
        "popularity": raw.get("popularity", 0.0),
    }


def _is_valid(movie: dict) -> bool:
    """Reject movies without synopsis (useless for RAG exercises).

    Args:
        movie: Normalized movie dict.

    Returns:
        True if the movie has a usable synopsis.
    """
    return len(movie["overview"]) > 20


def fetch_dataset(api_key: str) -> list[dict]:
    """Fetch and assemble the complete horror movies dataset.

    Args:
        api_key: TMDB API v3 key.

    Returns:
        List of normalized movie dicts.
    """
    movies: list[dict] = []
    page = 1

    while len(movies) < TOTAL_MOVIES:
        print(f"  Page {page}...")
        raw_movies = _fetch_horror_page(api_key, page)

        if not raw_movies:
            break

        normalized = [_normalize_movie(m) for m in raw_movies]
        valid = [m for m in normalized if _is_valid(m)]
        movies.extend(valid)
        page += 1
        time.sleep(0.25)

    return movies[:TOTAL_MOVIES]


def main() -> None:
    """Entry point: fetch movies and write JSON dataset."""
    parser = argparse.ArgumentParser(
        description="Fetch horror movies from TMDB for tutorial dataset.",
    )
    parser.add_argument(
        "--api-key",
        help="TMDB API v3 key (or use .env file / TMDB_API_KEY env var)",
        default=None,
    )
    args = parser.parse_args()

    api_key = _resolve_api_key(args.api_key)
    print(f"Fetching {TOTAL_MOVIES} horror movies from TMDB...")
    movies = fetch_dataset(api_key)

    OUTPUT_FILE.write_text(
        json.dumps(movies, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Done: {len(movies)} movies → {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
