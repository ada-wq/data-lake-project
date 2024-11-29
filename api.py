from flask import Flask, jsonify, request
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialisation de la session Spark
spark = SparkSession.builder \
    .master("local") \
    .appName("DataLake_API") \
    .getOrCreate()

# Initialisation de Flask
app = Flask(__name__)

# Chemin de base du Data Lake
base_path = "/mnt/c/Users/Mahamat Adam/OneDrive/Documents/Cours 2023-2024/S2/Datalake/projet/data-lake/processed/"

# Route pour obtenir les transactions filtrées
@app.route("/transactions", methods=["GET"])
def get_transactions():
    try:
        # Paramètre de filtrage (par exemple, filtrer par produit)
        product = request.args.get("product", default=None, type=str)
        
        # Lecture des données depuis le Data Lake (CSV filtré)
        df_transactions = spark.read.csv(f"{base_path}filtered_transactions.csv", header=True, inferSchema=True)
        
        # Filtrage par produit si nécessaire
        if product:
            df_transactions = df_transactions.filter(col("product") == product)

        # Convertir le DataFrame Spark en JSON0
        transactions_json = df_transactions.toPandas().to_dict(orient="records")
        
        return jsonify(transactions_json), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route pour obtenir les logs nettoyés
@app.route("/logs", methods=["GET"])
def get_logs():
    try:
        # Lecture des données de logs
        df_logs = spark.read.csv(f"{base_path}cleaned_logs.csv", header=True, inferSchema=True)
        
        # Convertir le DataFrame Spark en JSON
        logs_json = df_logs.toPandas().to_dict(orient="records")
        
        return jsonify(logs_json), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route pour obtenir les réseaux sociaux transformés
@app.route("/social_media", methods=["GET"])
def get_social_media():
    try:
        # Lecture des données de réseaux sociaux
        df_social_media = spark.read.json(f"{base_path}social_media_transformed.json")
        
        # Convertir le DataFrame Spark en JSON
        social_media_json = df_social_media.toPandas().to_dict(orient="records")
        
        return jsonify(social_media_json), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route pour obtenir les publicités nettoyées
@app.route("/ads", methods=["GET"])
def get_ads():
    try:
        # Lecture des données de publicités
        df_ads = spark.read.json(f"{base_path}ads_cleaned.json")
        
        # Convertir le DataFrame Spark en JSON
        ads_json = df_ads.toPandas().to_dict(orient="records")
        
        return jsonify(ads_json), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Lancer l'application Flask
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)