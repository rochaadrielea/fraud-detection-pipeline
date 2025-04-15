from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.getOrCreate()

df_bronze = spark.read.format("delta").load("/mnt/raw/bronze/claims_stream")

df_silver = df_bronze.withColumn("claim_amount", col("claim_amount").cast("float")) \
    .withColumn("status", col("status").lower()) \
    .withColumn("is_high_value", when(col("claim_amount") > 10000, True).otherwise(False))

df_silver.write.mode("overwrite").format("delta").save("/mnt/raw/silver/claims_stream")
print("✅ Silver data written to /mnt/raw/silver/claims_stream")