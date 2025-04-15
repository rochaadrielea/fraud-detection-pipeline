from pyspark.sql.functions import col, when

def clean_data(df):
    return df.withColumn("claim_amount", col("claim_amount").cast("float")) \
             .withColumn("status", col("status").lower()) \
             .withColumn("is_high_value", when(col("claim_amount") > 10000, True).otherwise(False))