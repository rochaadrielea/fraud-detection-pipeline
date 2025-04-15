from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

raw_df = spark.read.option("header", True).csv("/FileStore/tables/claims_stream.csv")
raw_df.write.mode("overwrite").format("delta").save("/mnt/raw/bronze/claims_stream")
print("✅ Bronze data written to /mnt/raw/bronze/claims_stream")