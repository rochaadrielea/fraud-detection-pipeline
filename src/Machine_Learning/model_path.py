import os
import pickle

# Create directory if needed
os.makedirs("/dbfs/tmp", exist_ok=True)

# Save model to file
model_path = "/dbfs/tmp/fraud_model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f" IsolationForest model saved to: {model_path}")