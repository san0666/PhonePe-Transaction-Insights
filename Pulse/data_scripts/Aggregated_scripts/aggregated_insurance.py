import os
import json
import pandas as pd # type: ignore

insurance_data = []

# Country-level parsing
base_path_country = "Pulse/data/aggregated/insurance/country/india"

for year in os.listdir(base_path_country):
    year_path = os.path.join(base_path_country, year)
    if not os.path.isdir(year_path):
        continue

    for quarter_file in os.listdir(year_path):
        if not quarter_file.endswith(".json"):
            continue

        quarter = quarter_file.strip(".json")
        file_path = os.path.join(year_path, quarter_file)

        with open(file_path, "r") as f:
            data = json.load(f)

        try:
            for transaction in data["data"]["transactionData"]:
                instrument = transaction["paymentInstruments"][0]
                insurance_data.append({
                    "level": "country",
                    "state": None,
                    "year": int(year),
                    "quarter": int(quarter),
                    "transaction_type": transaction["name"],
                    "count": instrument["count"],
                    "amount": instrument["amount"]
                })
        except Exception as e:
            print(f"Error in {file_path}: {e}")
            continue

# State-level parsing
base_path_state = "Pulse/data/aggregated/insurance/country/india/state"

for state in os.listdir(base_path_state):
    state_path = os.path.join(base_path_state, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for quarter_file in os.listdir(year_path):
            if not quarter_file.endswith(".json"):
                continue

            quarter = quarter_file.strip(".json")
            file_path = os.path.join(year_path, quarter_file)

            with open(file_path, "r") as f:
                data = json.load(f)

            try:
                for transaction in data["data"]["transactionData"]:
                    instrument = transaction["paymentInstruments"][0]
                    insurance_data.append({
                        "level": "state",
                        "state": state,
                        "year": int(year),
                        "quarter": int(quarter),
                        "transaction_type": transaction["name"],
                        "count": instrument["count"],
                        "amount": instrument["amount"]
                    })
            except Exception as e:
                print(f"Error in {file_path}: {e}")
                continue

# Create DataFrame
df_aggregated_insurance = pd.DataFrame(insurance_data)
print(df_aggregated_insurance.head())
print(df_aggregated_insurance.info())




