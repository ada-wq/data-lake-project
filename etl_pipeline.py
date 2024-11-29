import os
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from pyspark.sql.functions import col, when

# Création de la session Spark
spark = SparkSession.builder \
    .master("local") \
    .appName("DataLake_ETL_Fusion") \
    .getOrCreate()

# Chemin de base
base_path = "/mnt/c/Users/Mahamat Adam/OneDrive/Documents/Cours 2023-2024/S2/Datalake/projet/data-lake/"

# Schémas explicites pour les fichiers JSON
social_media_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("username", StringType(), True),
    StructField("text", StringType(), True),
    StructField("likes", IntegerType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("_corrupt_record", StringType(), True)
])

ads_schema = StructType([
    StructField("campaign_id", StringType(), True),
    StructField("platform", StringType(), True),
    StructField("impressions", IntegerType(), True),
    StructField("clicks", IntegerType(), True),
    StructField("_corrupt_record", StringType(), True)
])

# Lecture, nettoyage, transformation et sauvegarde
try:
    # 1. **Transactions CSV**
    print("Traitement des fichiers CSV...")
    df_transactions = spark.read.csv(
        f"{base_path}raw/transactions/transactions_raw.csv",
        header=True,
        inferSchema=True
    )
    df_filtered_transactions = df_transactions.filter(col("product") == "Laptop")
    df_filtered_transactions.write.csv(
        f"{base_path}processed/filtered_transactions.csv",
        header=True,
        mode="overwrite"
    )
    print(f"Transactions sauvegardées : {base_path}processed/filtered_transactions.csv")

    # 2. **Logs TXT**
    print("Traitement des fichiers TXT...")
    df_logs = spark.read.text(f"{base_path}raw/logs/server_logs.txt")
    df_logs_cleaned = df_logs.selectExpr(
        "split(value, ',')[0] as session_id",
        "split(value, ',')[1] as action",
        "split(value, ',')[2] as timestamp",
        "split(value, ',')[3] as url"
    )
    df_logs_cleaned.write.csv(
        f"{base_path}processed/cleaned_logs.csv",
        header=True,
        mode="overwrite"
    )
    print(f"Logs sauvegardés : {base_path}processed/cleaned_logs.csv")

    # 3. **Réseaux sociaux JSON**
    print("Traitement des fichiers JSON de réseaux sociaux...")
    df_social_media = spark.read \
        .schema(social_media_schema) \
        .json(f"{base_path}raw/social-media/social_media_clean.json")
    df_social_media_clean = df_social_media.filter("_corrupt_record IS NULL").drop("_corrupt_record")
    df_social_media_transformed = df_social_media_clean.withColumn(
        "hashtag",
        when(col("text").contains("#sale"), "sale")
        .when(col("text").contains("#tech"), "tech")
        .otherwise("other")
    )
    df_social_media_transformed.write.json(
        f"{base_path}processed/social_media_transformed.json",
        mode="overwrite"
    )
    print(f"Réseaux sociaux sauvegardés : {base_path}processed/social_media_transformed.json")

    # 4. **Publicités JSON**
    print("Traitement des fichiers JSON de publicités...")
    df_ads = spark.read \
        .schema(ads_schema) \
        .json(f"{base_path}raw/ads-campaigns/ads_raw.json")
    df_ads_clean = df_ads.filter("_corrupt_record IS NULL").drop("_corrupt_record")
    df_ads_clean.write.json(
        f"{base_path}processed/ads_cleaned.json",
        mode="overwrite"
    )
    print(f"Publicités sauvegardées : {base_path}processed/ads_cleaned.json")

    print("Toutes les données ont été traitées et sauvegardées avec succès.")

except Exception as e:
    print(f"Erreur lors du traitement des fichiers : {e}")
    spark.stop()
    exit(1)

# Arrêt de Spark
spark.stop()