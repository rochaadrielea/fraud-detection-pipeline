# This is NOT executed here, just a summary of what was run in Databricks

# Databricks notebook steps:
# 1. Load Silver data from Delta Lake
# 2. Train IsolationForest on 'claim_amount'
# 3. Save model to DBFS
# 4. Reload model and predict fraud (anomaly = -1)
# 5. Join prediction with Silver and write to Gold Delta Table

# Final Delta output: /mnt/raw/gold/claims_stream_ml
