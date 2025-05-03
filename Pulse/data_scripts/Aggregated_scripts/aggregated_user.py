import os
import json
import pandas as pd  # type: ignore
user_data = []

    # 1) Country-level parsing
base_country_path = "Pulse/data/aggregated/user/country/india"
for year in os.listdir(base_country_path):
        year_path = os.path.join(base_country_path, year)
        if not os.path.isdir(year_path):
            continue

        for quarter_file in os.listdir(year_path):
            if not quarter_file.endswith(".json"):
                continue
            quarter = quarter_file.strip(".json")
            file_path = os.path.join(year_path, quarter_file)

            try:
                with open(file_path, "r") as f:
                    data = json.load(f)

                registered_users = data["data"]["aggregated"]["registeredUsers"]
                app_opens = data["data"]["aggregated"]["appOpens"]

                users_by_device = data["data"].get("usersByDevice")
                if users_by_device and isinstance(users_by_device, list):
                    for device in users_by_device:
                        user_data.append({
                            "level": "country",
                            "state": None,
                            "year": int(year),
                            "quarter": int(quarter),
                            "registered_users": registered_users,
                            "app_opens": app_opens,
                            "device_brand": device["brand"],
                            "user_count": device["count"],
                            "percentage": device["percentage"]
                        })
            except Exception as e:
                print(f"Error in country file {file_path}: {e}")
                continue

    # 2) State-level parsing
base_state_path = "Pulse/data/aggregated/user/country/india/state"
for state in os.listdir(base_state_path):
        state_path = os.path.join(base_state_path, state)
        for year in os.listdir(state_path):
            year_path = os.path.join(state_path, year)
            for quarter_file in os.listdir(year_path):
                if not quarter_file.endswith(".json"):
                    continue
                quarter = quarter_file.strip(".json")
                file_path = os.path.join(year_path, quarter_file)

                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)

                    registered_users = data["data"]["aggregated"]["registeredUsers"]
                    app_opens = data["data"]["aggregated"]["appOpens"]

                    users_by_device = data["data"].get("usersByDevice")
                    if users_by_device and isinstance(users_by_device, list):
                        for device in users_by_device:
                            user_data.append({
                                "level": "state",
                                "state": state,
                                "year": int(year),
                                "quarter": int(quarter),
                                "registered_users": registered_users,
                                "app_opens": app_opens,
                                "device_brand": device["brand"],
                                "user_count": device["count"],
                                "percentage": device["percentage"]
                            })
                except Exception as e:
                    print(f"Error in state file {file_path}: {e}")
                    continue

df_aggregated_user = pd.DataFrame(user_data)
    
