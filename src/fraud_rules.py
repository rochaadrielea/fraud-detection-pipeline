from pyspark.sql.functions import col, when

def rule_based_fraud_detection(df):
    return df.withColumn("is_fraud", when(
        (col("claim_amount") > 30000) | (col("status") == "rejected"), True
    ).otherwise(False))
