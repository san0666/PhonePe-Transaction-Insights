import os
import json
import pandas as pd # type: ignore

map_insurance_data = []

# Set base path to: data/map/insurance/hover/country/india
base_path = "Pulse/data/map/insurance/hover/country/india"

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
            for entry in data["data"]["hoverDataList"]:
                metric = entry["metric"][0]
                map_insurance_data.append({
                    "level": "state",
                    "state": entry["name"],
                    "year": int(year),
                    "quarter": int(quarter),
                    "type": metric["type"],
                    "count": metric["count"],
                    "amount": metric["amount"]
                })

        except Exception as e:
            print(f"Error in {file_path}: {e}")
            continue

# Convert to DataFrame
df_map_insurance = pd.DataFrame(map_insurance_data)
print(df_map_insurance.head())
