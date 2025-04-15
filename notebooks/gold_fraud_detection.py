from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.getOrCreate()

df_silver = spark.read.format("delta").load("/mnt/raw/silver/claims_stream")

df_gold = df_silver.withColumn("is_fraud", when(
    (col("claim_amount") > 30000) | (col("status") == "rejected"), True
).otherwise(False))

df_gold.write.mode("overwrite").format("delta").save("/mnt/raw/gold/claims_stream")
print("✅ Gold data written to /mnt/raw/gold/claims_stream")