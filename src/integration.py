def bronze_to_silver(df_bronze, transformer):
    return transformer(df_bronze)

def silver_to_gold(df_silver, fraud_detector):
    return fraud_detector(df_silver)