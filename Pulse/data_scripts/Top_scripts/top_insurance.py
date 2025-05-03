import os
import json
import pandas as pd  # type: ignore

top_insurance = []

base_path = "Pulse/data/top/insurance/country/india"

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
            for level_key in ["states", "districts", "pincodes"]:
                for item in data["data"].get(level_key, []):
                    metric = item["metric"]
                    top_insurance.append({
                        "level": "country",
                        "entity_type": level_key[:-1],  # 'state', 'district', 'pincode'
                        "entity_name": item["entityName"],
                        "year": int(year),
                        "quarter": int(quarter),
                        "type": metric["type"],
                        "count": metric["count"],
                        "amount": metric["amount"]
                    })
        except Exception as e:
            print(f"Error in file {file_path}: {e}")
            continue

# Create single DataFrame
df_top_insurance = pd.DataFrame(top_insurance)

# Preview
print("Top Insurance Combined:\n", df_top_insurance.head())
