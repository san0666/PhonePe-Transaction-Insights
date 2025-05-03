import os
import json
import pandas as pd # type: ignore

map_transaction_data = []

# Set base path to the folder containing year folders
base_path = "Pulse/data/map/transaction/hover/country/india"

for year in os.listdir(base_path):
    year_path = os.path.join(base_path, year)
    if not os.path.isdir(year_path):
        continue

    for quarter_file in os.listdir(year_path):
        if not quarter_file.endswith(".json"):
            continue

        quarter = quarter_file.strip(".json")
        file_path = os.path.join(year_path, quarter_file)

        with open(file_path, 'r') as f:
            data = json.load(f)

        try:
            for state_entry in data['data']['hoverDataList']:
                state_name = state_entry['name']
                metric = state_entry['metric'][0]  # Only one metric (TOTAL)

                map_transaction_data.append({
                    "level": "state",
                    "state": state_name,
                    "year": int(year),
                    "quarter": int(quarter),
                    "type": metric["type"],
                    "count": metric["count"],
                    "amount": metric["amount"]
                })

        except Exception as e:
            print(f"Error in file {file_path}: {e}")
            continue

# Create DataFrame
df_map_transaction = pd.DataFrame(map_transaction_data)
print(df_map_transaction.head())
