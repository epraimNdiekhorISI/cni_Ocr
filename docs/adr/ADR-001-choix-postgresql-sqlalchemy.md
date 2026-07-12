# ADR-001 — Choix de PostgreSQL + SQLAlchemy comme couche de persistance

## Statut
Accepté

## Contexte
Le projet doit stocker les données extraites de la CNI (recto/verso) dans une
base relationnelle. Le verso est lié au recto par le numéro de CNI (relation
1-1), et plusieurs champs doivent être validés (dates, format numéro CNI,
etc.) avant écriture. Le cahier des charges impose explicitement PostgreSQL.

## Décision
Utiliser PostgreSQL comme SGBD, avec SQLAlchemy comme ORM en mode déclaratif,
plutôt qu'un accès SQL brut (psycopg2 seul) ou une base NoSQL (MongoDB).

## Justification
- Les données sont naturellement relationnelles (recto ↔ verso liés par clé
  étrangère) → un modèle relationnel est plus adapté qu'un document NoSQL.
- PostgreSQL supporte nativement les contraintes CHECK, ce qui permet de
  valider `sexe IN ('M','F')` ou `date_expiration > date_delivrance`
  directement au niveau base, en plus de la validation applicative.
- SQLAlchemy permet de définir le schéma en Python (`models.py`), ce qui
  facilite les migrations et les tests (base de test isolée possible).

## Conséquences
- Positif : cohérence des données garantie même en cas de bug applicatif.
- Positif : navigation recto ↔ verso simplifiée via `relationship()`.
- Négatif : légère courbe d'apprentissage de l'ORM par rapport au SQL brut —
  acceptable ici puisque comprendre l'ORM fait partie de l'objectif pédagogique.