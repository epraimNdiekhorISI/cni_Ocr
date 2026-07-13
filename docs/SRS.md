# SRS — Spécification des exigences logicielles
## Projet OCR CNI Sénégal

**Version :** 1.0
**Date :** 2026-07-12

## 1. Introduction

### 1.1 Objectif
Ce document spécifie les exigences fonctionnelles et non fonctionnelles du
pipeline d'extraction, validation et persistance des données de la CNI
sénégalaise, conformément au cahier des charges du module Intelligence
Artificielle (ISI).

### 1.2 Portée
Couvre : prétraitement d'image, OCR recto/verso, parsing MRZ, validation
croisée, persistance PostgreSQL, API FastAPI.
Ne couvre pas : authentification utilisateur, interface web graphique
(hors Swagger auto-généré).

## 2. Exigences fonctionnelles

| ID | Exigence | Priorité |
|---|---|---|
| FR-001 | Le système DOIT redresser, recadrer et débruiter une image de CNI avant tout traitement OCR. | Haute |
| FR-002 | Le système DOIT extraire par OCR les champs du recto (numéro CNI, nom, prénom, sexe, taille, lieu de naissance, dates, centre, adresse). | Haute |
| FR-003 | Le système DOIT extraire par OCR les champs administratifs du verso (région, département, commune, NIN, numéro électeur, etc.). | Haute |
| FR-004 | Le système DOIT isoler et parser la zone MRZ (format TD1, 3 lignes) selon la norme ICAO 9303. | Haute |
| FR-005 | Le système DOIT vérifier les checksums intégrés dans la MRZ et signaler toute incohérence. | Haute |
| FR-006 | Le système DOIT valider le format de chaque champ structuré (dates réelles et cohérentes, sexe ∈ {M, F}, format numéro CNI). | Haute |
| FR-007 | Le système DOIT comparer le numéro CNI extrait par OCR classique avec celui de la MRZ et calculer un score de confiance. | Haute |
| FR-008 | Le système DOIT enregistrer les données validées dans PostgreSQL, avec `cni_verso` lié à `cni_recto` par clé étrangère. | Haute |
| FR-009 | Le système DOIT exposer un endpoint `POST /upload/recto` acceptant un fichier image et retournant les champs extraits. | Haute |
| FR-010 | Le système DOIT exposer un endpoint `POST /upload/verso` avec le même comportement pour le verso. | Haute |
| FR-011 | Le système DOIT exposer un endpoint `GET /cni/{numero_cni}` retournant les données consolidées. | Moyenne |
| FR-012 | Le système DOIT exposer un endpoint `GET /cni/{numero_cni}/confiance` retournant les scores de confiance par champ. | Moyenne |
| FR-013 | Le système DOIT permettre de basculer entre Tesseract et EasyOCR via une variable de configuration (`OCR_ENGINE`). | Basse |

## 3. Exigences non fonctionnelles

| ID | Exigence | Catégorie |
|---|---|---|
| NFR-001 | Le traitement complet d'une image (prétraitement + OCR + validation) DEVRAIT prendre moins de 10 secondes sur une machine standard. | Performance |
| NFR-002 | Aucun identifiant de connexion PostgreSQL ne DOIT apparaître en dur dans le code source. | Sécurité |
| NFR-003 | Les images de test committées dans le dépôt DOIVENT être anonymisées ou fictives. | Confidentialité |
| NFR-004 | Le système DOIT journaliser chaque étape du pipeline (réception image, champs extraits, score de confiance) sans exposer de données personnelles en clair dans les logs. | Observabilité / Confidentialité |
| NFR-005 | Chaque endpoint DOIT documenter ses codes d'erreur possibles dans Swagger. | Maintenabilité |

## 4. Traçabilité

Chaque exigence FR-XXX sera couverte par au moins un cas de test formel
(voir `docs/tests/test-cases/`), référencé dans la matrice de traçabilité du
rapport de test final.