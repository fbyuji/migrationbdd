# Vérification de l'Intégration des Données avec Pytest & SQL

Ce projet automatise la vérification de l'intégration des données migrées depuis une ancienne base de données.  
L'objectif est d'assurer que les données transférées sont **intactes**, **complètes** et **cohérentes**.

## Contexte
La base de données utilisée, `istore_db`, provient d'un **ancien projet**.  
Elle contient plusieurs tables, dont :
- **`articles`** (produits en stock)
- **`inventories`** (gestion des stocks)

L'automatisation a été réalisée avec **Python**, **Pytest**, et **MariaDB**.

## Fonctionnalités
 - Vérification du **nombre d'articles** après migration  
 - Vérification de **l'intégrité des données** (pas de valeurs corrompues)  
 - Vérification des **relations entre les tables** (clés étrangères valides)  
 - Automatisation avec **pytest** pour exécuter les tests en un clic  

## Technologies Utilisées
- **Python 3.11** 🐍
- **MariaDB / MySQL** 🛢️
- **Pytest** 🧪
- **Pandas** 📊
- **VS Code** 💻

## 🔧 Installation & Exécution
1. **Installer les dépendances**
   ```bash
   pip install mariadb

2. **Importer la BDD existante**
mysql -u root -p istore_db < istore_db.sql

3. **Lancer les tests**
pytest test_integration.py


