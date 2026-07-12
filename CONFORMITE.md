# CONFORMITE.md — Projet OCR CNI Sénégal

**Projet :** Extraction OCR des données de la CNI sénégalaise + persistance PostgreSQL
**Établissement :** Institut Supérieur d'Informatique (ISI) — Module Intelligence Artificielle
**Stack :** Python 3.11+, FastAPI, OpenCV, Tesseract/EasyOCR, SQLAlchemy, PostgreSQL, pytest
**Mode d'audit :** `NEW_PROJECT` + `ACADEMIC_DEFENSE` (projet tutoré avec soutenance)
**Équipe :** Solo
**Date :** 2026-07-11
**Licence :** Aucune (usage académique privé)

---

## 1. État du projet

| Élément | Statut |
|---|---|
| Architecture documentée (pipeline, arborescence, DDL, endpoints) | ✅ |
| Dépôt Git initialisé | ❌ |
| Code source | ❌ |
| Lint / format / pre-commit | ❌ |
| Tests (unitaires, plan, cas de test) | ❌ |
| CI/CD | ❌ |
| Documentation formelle (README, ADR, SRS) | ❌ |
| Conteneurisation (Docker) | ❌ |
| Gestion des données sensibles formalisée | 🟡 |
| Observabilité (logs, erreurs) | ❌ |

Rien n'est bloquant : c'est l'état normal d'un projet qui n'a pas encore de première ligne de code. L'objectif de ce document est d'éviter d'écrire 2000 lignes avant le premier commit propre.

---

## 2. Référentiels ciblés (adaptés au contexte)

| Référentiel | Pertinence | Application |
|---|---|---|
| ISO/IEC 12207 (cycle de vie logiciel) | Élevée | Structure des phases déjà posée dans l'architecture — sert de base au SDLC |
| ISTQB / STLC | Élevée | Projet évalué en soutenance → plan de test + cas de test formels attendus |
| OWASP Top 10 | Moyenne | API expose upload de fichiers + données d'identité → surface d'attaque réelle |
| Protection des données personnelles | Élevée | CNI/NIN = données sensibles. Le RGPD ne s'applique pas directement (utilisateurs/données au Sénégal) — le référentiel pertinent est la **loi sénégalaise n°2008-12 du 25/01/2008 sur la protection des données à caractère personnel**, sous supervision de la **CDP** (Commission de protection des Données personnelles). Les principes (minimisation, finalité, sécurité, durée de conservation) restent les mêmes que le RGPD et seront traités selon cette même logique. |
| WCAG 2.2 | Non applicable | Pas d'interface web custom — uniquement une API + Swagger auto-généré. À reconsidérer si un frontend est ajouté. |
| Processus agile formel | Non applicable | Projet solo, pas de méthodologie Scrum requise — des jalons hebdomadaires suffisent |

---

## 3. Analyse des écarts (12 sous-sections)

### 3.1 Documentation
❌ Aucun README, ADR, ou SRS formel n'existe. L'architecture actuelle (`architecture_projet_ocr_cni.md`) est une bonne base mais n'est pas structurée en exigences traçables (FR-XXX).

### 3.2 Tests — STLC complet
❌ Rien n'existe : pas de plan de test, pas de cas de test au format ISTQB, pas de pyramide de tests. **C'est le point le plus critique pour la soutenance** : le cahier des charges demande un "taux de réussite d'extraction" chiffré, ce qui n'a de valeur académique que si les tests sont documentés et reproductibles — pas juste "j'ai lancé le script et ça a marché".

### 3.3 CI/CD
❌ Aucun pipeline. Même en solo, une CI (lint → test → build) évite de découvrir un `ImportError` la veille de la soutenance.

### 3.4 Qualité de code
❌ Pas de lint/format/pre-commit configurés. Généré dans cette itération (voir §5).

### 3.5 Sécurité avancée (STRIDE + OWASP)
❌ Non traité. Points d'attention réels pour ce projet précis : upload de fichier non validé (taille/type MIME), injection SQL si les requêtes ne passent pas par SQLAlchemy paramétré, absence de limitation de taux sur `/upload`, stockage des identifiants PostgreSQL en clair si `.env` n'est pas exclu du dépôt.

### 3.6 Protection des données personnelles
🟡 Partiel. Le cahier des charges exige déjà des images "anonymisées ou fictives" pour les tests — bon réflexe. Manque : un registre de traitement minimal (quelles données, pourquoi, combien de temps conservées, qui y accède) et une règle explicite de ne jamais committer de vraies données personnelles.

### 3.7 Observabilité
❌ Pas de logging structuré prévu au-delà de la mention générale dans l'architecture. À formaliser avec le module `logging` standard (niveau, format, fichier de sortie) avant la phase API.

### 3.8 Conteneurisation
❌ Absent. Justifié ici : le projet a au moins deux services (FastAPI + PostgreSQL) → `docker-compose.yml` a du sens pour que la démo tourne pareil sur n'importe quelle machine, y compris celle du jury.

### 3.9 Accessibilité WCAG 2.2
Non applicable — pas d'interface web custom prévue à ce stade (uniquement API + Swagger). Aucune action requise sauf si un frontend est ajouté plus tard.

### 3.10 Processus agile
Non applicable formellement — projet solo. Recommandation légère : des jalons hebdomadaires alignés sur les 4 phases déjà définies dans le planning du cahier des charges, pour éviter l'effet tunnel.

### 3.11 Gouvernance IA dans le SDLC
🟡 Partiel. Le projet utilise des modèles OCR tiers (Tesseract/EasyOCR) sans entraînement custom — le risque de "gouvernance IA" ici est surtout la **documentation des limites** : biais possibles de l'OCR selon la qualité d'image, absence de garantie d'exactitude sans validation croisée MRZ, nécessité de signaler qu'aucune décision automatisée à conséquence légale n'est prise sans revue humaine. À documenter dans le README/SRS plutôt que dans un document de gouvernance séparé, vu l'échelle du projet.

### 3.12 Conformité ISTQB
❌ Absente. À produire : plan de test (portée, critères d'entrée/sortie, risques), cas de test formels par module (prétraitement, OCR, MRZ, validation, API), rapport de test final avec les métriques demandées par le cahier des charges.

---

## 4. Plan d'action priorisé

### Immédiat (aujourd'hui, ~30 min) — généré dans cette itération
- [x] `.gitignore` (Python, exclut `.env`, données de test réelles, artefacts de build)
- [x] `.editorconfig`
- [x] Config lint + format (`ruff` + `black` via `pyproject.toml`)
- [x] `.pre-commit-config.yaml`

### Semaine 1
- [ ] Initialiser le dépôt Git (`git init`, premier commit avec la scaffolding)
- [ ] `README.md` (installation, lancement, structure du projet)
- [ ] Premier ADR (ex. "Choix de PostgreSQL + SQLAlchemy plutôt que MongoDB")
- [ ] `.env.example`
- [ ] Pas de LICENSE (usage académique privé confirmé)

### Semaine 2-3
- [ ] Squelette de tests (`pytest`, structure `tests/`)
- [ ] `docs/SRS.md` — exigences formelles (FR-001 = extraction numéro CNI, FR-002 = validation MRZ, etc.)
- [ ] `docs/tests/test-plan.md` (ISTQB)
- [ ] Diagramme de séquence du pipeline (UML léger, peut être fait en Mermaid)

### Semaine 4+
- [ ] `Dockerfile` + `docker-compose.yml` (app + PostgreSQL)
- [ ] Pipeline CI (`.github/workflows/ci.yml` : lint → test → build)
- [ ] `docs/tests/test-cases/TC-XXX.md` — cas de test formels par module
- [ ] `docs/rgpd/registre-traitements.md` (adapté loi sénégalaise, pas RGPD UE)

### Avant la soutenance
- [ ] `docs/tests/test-report.md` — résultats chiffrés (taux de réussite par champ, taux de validation croisée MRZ, temps moyen de traitement)
- [ ] Mini analyse de risques STRIDE (une page suffit à ce niveau)
- [ ] Relecture du README + vérification que `docker-compose up` fonctionne sur une machine propre

---

## 5. Checklist de conformité par phase du projet

| Phase (cf. architecture) | Lint/format | Tests | Doc | Sécurité |
|---|---|---|---|---|
| Prétraitement (OpenCV) | ruff+black | test unitaire (dimensions/contraste) | docstrings | validation format image en entrée |
| OCR recto/verso | ruff+black | test comparatif Tesseract/EasyOCR | ADR sur le choix moteur OCR | — |
| MRZ + checksum | ruff+black | test sur checksum valide/invalide | doc format TD1 dans SRS | — |
| Structuration/validation | ruff+black | tests unitaires par regex | FR-XXX dans SRS | — |
| PostgreSQL | ruff+black | test insertion/contraintes FK | DDL versionné | pas de secrets en dur, `.env` |
| API FastAPI | ruff+black | tests endpoints (via TestClient) | Swagger + OpenAPI | validation taille/type fichier upload |
| Tests globaux | — | rapport de test ISTQB | test-report.md | — |

---

## 6. Métriques cibles

| Catégorie | Métrique | Cible |
|---|---|---|
| Qualité code | Couverture de tests | ≥ 70 % |
| Fonctionnel | Taux de réussite extraction par champ | Mesuré et documenté (cahier des charges) |
| Fonctionnel | Taux de validation croisée MRZ réussie | Mesuré et documenté |
| Fonctionnel | Temps moyen de traitement par image | Mesuré et documenté |
| Sécurité | Vulnérabilités OWASP Top 10 non mitigées | 0 critique |
| Process | Commits avec message clair (Conventional Commits recommandé) | 100 % |

---

## 7. Ce qui a été généré dans cette itération

Voir la scaffolding livrée avec ce document : `.gitignore`, `.editorconfig`, `pyproject.toml` (ruff + black + pytest), `.pre-commit-config.yaml`.

**Prochaine étape immédiate** : `git init`, copier ces fichiers à la racine de `cni_ocr_project/`, faire un premier commit, puis installer les hooks (`pip install pre-commit && pre-commit install`).

Dis-moi quand c'est fait pour qu'on attaque la Semaine 1 (README, ADR, `.env.example`).