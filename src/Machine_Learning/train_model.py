import os
import pickle
import pandas as pd
from sklearn.ensemble import IsolationForest

def train_isolation_forest(spark_df, save_path="/dbfs/tmp/fraud_model.pkl"):
    """
    Trains an IsolationForest model on 'claim_amount' and saves it as a pickle file.
    Designed to mirror Databricks notebook logic for fraud detection.
    """
    print(" Converting to pandas...")
    df = spark_df.select("claim_amount").toPandas()

    print(" Training IsolationForest...")
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(df)

    print(" Saving model to:", save_path)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved successfully.")
    return model
