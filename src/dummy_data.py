import os
import csv
import random

from faker import Faker
fake = Faker()

# Folder and file setup
folder_path = "data"
file_path = os.path.join(folder_path, "claims_stream.csv")

# Create folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Only create the file if it doesn't exist
if not os.path.exists(file_path):
    print("🔧 File doesn't exist. Creating claims_stream.csv with 100 rows...")
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["claim_id", "customer_id", "claim_amount", "status"])

        statuses = ["approved", "pending", "rejected"]
        for i in range(1, 101):
            claim_id = f"C{i:03d}"
            customer_id = f"U{random.randint(1000, 9999)}"
            claim_amount = round(random.uniform(50.0, 50000.0), 2)
            status = random.choice(statuses)
            writer.writerow([claim_id, customer_id, claim_amount, status])
    print(f" File created at: {file_path}")
else:
    print(f" File already exists at: {file_path}. No changes made.")
