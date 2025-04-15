def test_fraud_detection():
    from pyspark.sql import SparkSession
    from fraud_rules import rule_based_fraud_detection
    from pyspark.sql import Row

    spark = SparkSession.builder.master("local").appName("Test").getOrCreate()
    sample = [
        Row(claim_amount=45000.0, status="approved"),
        Row(claim_amount=12000.0, status="rejected"),
        Row(claim_amount=5000.0, status="approved")
    ]
    df = spark.createDataFrame(sample)
    df_result = rule_based_fraud_detection(df).collect()
    assert df_result[0].is_fraud == True
    assert df_result[1].is_fraud == True
    assert df_result[2].is_fraud == False