import os
import json
import pandas as pd # type: ignore

map_user_data = []

# Path to map/user/hover/country/india/
base_path = "Pulse/data/map/user/hover/country/india"

for year in os.listdir(base_path):
    year_path = os.path.join(base_path, year)
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
            for state_name, state_info in data["data"]["hoverData"].items():
                map_user_data.append({
                    "level": "state",
                    "state": state_name,
                    "year": int(year),
                    "quarter": int(quarter),
                    "registered_users": state_info["registeredUsers"],
                    "app_opens": state_info["appOpens"]
                })

        except Exception as e:
            print(f"Error in file {file_path}: {e}")
            continue

# Create DataFrame
df_map_user = pd.DataFrame(map_user_data)
print(df_map_user.head())
