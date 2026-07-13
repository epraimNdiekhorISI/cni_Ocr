# Plan de test — Projet OCR CNI Sénégal

**Version :** 1.0
**Date :** 2026-07-12

## 1. Objectifs et périmètre

Vérifier que le pipeline d'extraction, validation et persistance des données
de la CNI sénégalaise respecte les exigences fonctionnelles FR-001 à FR-013
et non fonctionnelles NFR-001 à NFR-005 définies dans le SRS.

## 2. Éléments à tester (Test items)

- Module de prétraitement d'image (`app/preprocessing`)
- Module OCR recto/verso (`app/ocr`)
- Module de parsing et validation MRZ (`app/mrz`)
- Module de structuration et validation (`app/structuring`)
- Couche de persistance PostgreSQL (`app/db`)
- API FastAPI (`app/api`)

## 3. Fonctionnalités à tester / à ne pas tester

**À tester :** tous les éléments listés en section 2, couvrant FR-001 à FR-013.

**Hors périmètre :** performance sous charge élevée (>100 requêtes
simultanées), interface graphique custom (aucune prévue), compatibilité
multi-navigateurs (l'API n'a pas de frontend).

## 4. Stratégie de test (niveaux)

| Niveau | Portée | Outil |
|---|---|---|
| Tests unitaires | Chaque fonction pure (validators, mrz_parser) isolée | pytest |
| Tests d'intégration | Pipeline complet image → base de données | pytest + base PostgreSQL de test |
| Tests système | Endpoints API de bout en bout | pytest + `TestClient` FastAPI, ou Swagger manuel documenté |
| Tests manuels documentés | Démonstration via Swagger `/docs` | Cas de test formels (voir `docs/tests/test-cases/`) |

## 5. Critères d'entrée

- Le code du module concerné est écrit et exécutable sans erreur d'import.
- L'environnement de test (base PostgreSQL de test, jeu d'images) est disponible.

## 6. Critères de sortie

- 100 % des exigences FR-001 à FR-013 couvertes par au moins un cas de test.
- Couverture de code ≥ 70 % sur `app/`.
- 0 anomalie bloquante ouverte sur les modules prétraitement, OCR, MRZ.
- Taux de réussite d'extraction mesuré et documenté, même s'il n'atteint pas 100 %.

## 7. Environnement de test

- Python 3.11+, dépendances de `pyproject.toml` / `requirements.txt`.
- Instance PostgreSQL locale ou conteneurisée, base dédiée aux tests
  (jamais la base de développement).
- Jeu de 5 à 10 images de CNI anonymisées/fictives (`tests/images/`).

## 8. Risques et mitigations

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Qualité variable des images de test (angle, luminosité) fausse les métriques OCR | Moyenne | Moyen | Standardiser un protocole de capture pour le jeu de test |
| Tesseract non installé sur la machine d'exécution des tests | Moyenne | Élevé | Documenter le prérequis dans le README, vérifier dans la CI |
| Checksum MRZ mal implémenté (faux positifs/négatifs) | Faible | Élevé | Test dédié avec MRZ volontairement corrompue (`test_mrz_checksum_invalid_detected`) |
| Données sensibles committées par erreur | Faible | Élevé | `.gitignore` dédié + revue avant chaque commit |

## 9. Calendrier

| Phase | Début | Fin |
|---|---|---|
| Tests unitaires (prétraitement, validators) | Semaine 2 | Semaine 2 |
| Tests unitaires (OCR, MRZ) | Semaine 3 | Semaine 3 |
| Tests d'intégration (pipeline + BDD) | Semaine 4 | Semaine 4 |
| Tests système (API via Swagger) | Semaine 4 | Semaine 5 |
| Rapport de test final | Semaine 5 | Avant soutenance |