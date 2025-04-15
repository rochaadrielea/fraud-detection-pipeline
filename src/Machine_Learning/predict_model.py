import pickle
import pandas as pd

def load_model_and_predict(spark_df, model_path="/dbfs/tmp/fraud_model.pkl"):
    """
    Loads trained model and returns a pandas DataFrame with anomaly predictions.
    """
    print(" Loading model from:", model_path)
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    print(" Predicting...")
    df = spark_df.select("claim_amount").toPandas()
    df["anomaly_score"] = model.predict(df)
    df["is_fraud_ml"] = df["anomaly_score"] == -1

    print(f" Prediction complete.")
    return df
