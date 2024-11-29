# README - Projet Data Lake pour une Entreprise de Commerce en Ligne

Ce projet vise à concevoir, développer et exploiter un Data Lake pour une entreprise de commerce en ligne. Le système centralise les données provenant de diverses sources pour permettre une prise de décision éclairée grâce à des analyses complètes et des visualisations efficaces.

---

## **Table des Matières**
1. [Introduction](#introduction)
2. [Vue d'ensemble de l'Architecture](#vue-densemble-de-larchitecture)
3. [Instructions d'Installation](#instructions-dinstallation)
4. [Fonctionnalités](#fonctionnalités)
   - Ingestion des Données
   - Transformation des Données
   - API pour l'Accès aux Données
   - Gouvernance et Sécurité des Données
5. [Structure des Fichiers](#structure-des-fichiers)
6. [Technologies Utilisées](#technologies-utilisées)
7. [Améliorations Futures](#améliorations-futures)
8. [Contact](#contact)

---

## **Introduction**
Ce projet repose sur une architecture Data Lake pour :
- Centraliser et stocker des données provenant de différentes sources.
- Traiter et transformer des données structurées, semi-structurées et non structurées.
- Fournir des capacités de traitement en temps réel et par lots.
- Sécuriser et gouverner les données pour garantir leur qualité et leur fiabilité.

---

## **Vue d'ensemble de l'Architecture**
L’architecture du Data Lake comprend :
1. **Sources de Données :**
   - Transactions clients (base de données relationnelle, exportées en CSV).
   - Logs de serveurs (fichiers texte).
   - Données des réseaux sociaux (JSON semi-structuré).
   - Données des campagnes publicitaires (flux en temps réel au format JSON).
2. **Couche de Stockage :** Les données sont stockées localement (système de fichiers) avec la possibilité de migrer vers des plateformes comme Amazon S3 ou HDFS.
3. **Couche de Traitement :** Apache Spark est utilisé pour les pipelines ETL.
4. **Couche d’Accès :** API RESTful basée sur Flask pour exposer les données.
5. **Gouvernance et Sécurité :** Des politiques pour cataloguer, sécuriser et surveiller la qualité des données.

---

## **Instructions d'Installation**
### Prérequis :
- **Python 3.8 ou supérieur** : Assurez-vous que Python est installé.
- **Apache Spark** : Installez Spark localement ou configurez un cluster.
- **Flask** : Utilisé pour exposer les données via une API.
- **pandas et PySpark** : Librairies Python pour manipuler les données.

### Étapes d'installation :
1. **Cloner le projet** :
   ```bash
   git clone <URL_DU_REPO>
   cd data-lake-project
   ```

2. **Configurer l'environnement Python** :
   ```bash
   python -m venv venv
   source venv/bin/activate   # Sur Windows : venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configurer les chemins des données** :
   - Mettez à jour les chemins dans les scripts `etl_pipeline.py` et `api.py` selon la structure de vos dossiers.

4. **Lancer les traitements ETL** :
   ```bash
   python etl_pipeline.py
   ```

5. **Lancer l’API Flask** :
   ```bash
   python api.py
   ```

6. **Accéder aux données** :
   - Accédez à l'API à l’adresse [http://localhost:5000](http://localhost:5000).

---

## **Fonctionnalités**

### **1. Ingestion des Données**
- Récupération des données brutes depuis plusieurs sources (CSV, JSON, TXT).
- Implémentation d’un pipeline d’ingestion pour gérer différents formats.

### **2. Transformation des Données**
- Nettoyage et enrichissement des données avec Apache Spark.
- Sauvegarde des données transformées dans la couche de stockage.

### **3. API pour l’Accès aux Données**
- Exposition des données via une API RESTful Flask.
- Endpoints pour accéder aux transactions, logs, données des réseaux sociaux et campagnes publicitaires.

### **4. Gouvernance et Sécurité des Données**
- Catalogage et versioning des datasets.
- Politiques de contrôle d’accès et gestion des anomalies.

---

## **Structure des Fichiers**
```
data-lake-project/
│
├── raw/                        # Données brutes
│   ├── transactions/           # Fichiers CSV des transactions
│   ├── logs/                   # Logs des serveurs
│   ├── social-media/           # Données JSON des réseaux sociaux
│   └── ads-campaigns/          # Flux JSON des campagnes publicitaires
│
├── processed/                  # Données transformées
│
├── scripts/                    # Scripts principaux
│   ├── etl_pipeline.py         # Pipeline ETL
│   └── api.py                  # API Flask
│
├── requirements.txt            # Dépendances Python
└── README.md                   # Documentation du projet
```

---

## **Technologies Utilisées**
- **Apache Spark** : Traitement distribué des données.
- **Flask** : Création d’une API RESTful.
- **Python** : Scripts pour ingestion, transformation et exposition des données.
- **pandas** : Manipulation des données au format tabulaire.
- **HDFS/Local File System** : Stockage des données.

---

## **Améliorations Futures**
- Intégration avec des outils BI comme Tableau ou Power BI pour la visualisation.
- Migration vers des solutions Cloud (AWS S3, Azure Data Lake).
- Mise en œuvre d’un moteur de recherche de métadonnées.
- Surveillance en temps réel des pipelines de données.
