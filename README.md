# CNI OCR — Extraction et structuration des données de la CNI sénégalaise

Projet tutoré — Institut Supérieur d'Informatique (ISI)
Module : Intelligence Artificielle — Année 2025-2026

## Description

Ce projet extrait automatiquement les champs du recto et du verso de la Carte
Nationale d'Identité (CNI) sénégalaise via OCR, valide les données extraites
(y compris via la zone MRZ), et les enregistre dans une base PostgreSQL.

## Prérequis

- Python 3.11+
- PostgreSQL 14+
- Tesseract OCR installé sur la machine (`tesseract --version` pour vérifier)

## Installation

```bash
git clone <url-du-depot>
cd cni_ocr_project
python -m venv venv
source venv/bin/activate        # sous Windows : venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # puis renseigner les vraies valeurs
```

## Lancer l'application

```bash
uvicorn app.main:app --reload
```

L'API est accessible sur `http://localhost:8000`.
La documentation interactive Swagger est sur `http://localhost:8000/docs`.

## Lancer les tests

```bash
pytest
```

## Qualité de code

```bash
black .
ruff check .
```

## Licence

Projet académique — usage privé, aucune licence publique.