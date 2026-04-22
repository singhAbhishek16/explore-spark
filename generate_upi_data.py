# generate_upi_data.py

import csv
import random
from datetime import datetime, timedelta

cities    = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai",
             "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow"]

banks     = ["SBI", "HDFC", "ICICI", "Axis", "Kotak",
             "PNB", "BOB", "Canara", "IDBI", "Yes Bank"]

categories = ["Food", "Transport", "Shopping", "Recharge",
              "Utilities", "Healthcare", "Education", "Entertainment"]

def random_date(start, end):
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))

def generate(filename, num_rows):
    start_date = datetime(2023, 1, 1)
    end_date   = datetime(2023, 12, 31)

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "transaction_id", "date", "city",
            "sender_bank", "receiver_bank",
            "amount_inr", "category", "status"
        ])
        for i in range(num_rows):
            writer.writerow([
                f"TXN{i:010d}",
                random_date(start_date, end_date).strftime("%Y-%m-%d"),
                random.choice(cities),
                random.choice(banks),
                random.choice(banks),
                round(random.uniform(10, 50000), 2),
                random.choice(categories),
                random.choice(["SUCCESS", "FAILED", "PENDING"])
            ])
    print(f"Generated {filename} with {num_rows} rows")

generate("upi_sample.csv", 10)
generate("upi_100k.csv",  100_000)
generate("upi_1m.csv",  1_000_000)
generate("upi_10m.csv", 10_000_000)