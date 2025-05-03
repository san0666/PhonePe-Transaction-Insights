from sqlalchemy import create_engine
import pandas as pd
import sys
import os

# Add the parent directory of 'Pulse' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Pulse.data_scripts.Aggregated_scripts.aggregated_user import user_data
from Pulse.data_scripts.Aggregated_scripts.aggregated_transaction import clm
from Pulse.data_scripts.Aggregated_scripts.aggregated_insurance import insurance_data

from Pulse.data_scripts.Map_scripts.map_user import map_user_data
from Pulse.data_scripts.Map_scripts.map_transaction import map_transaction_data
from Pulse.data_scripts.Map_scripts.map_insurance import map_insurance_data

from Pulse.data_scripts.Top_scripts.top_user import top_user
from Pulse.data_scripts.Top_scripts.top_transaction import top_transaction
from Pulse.data_scripts.Top_scripts.top_insurance import top_insurance

# credentials
username = "root"
password = "san2003"
host = "localhost"
port = 3306
database = "phonepe"

# Create SQLAlchemy connection
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Load all DataFrames

df_aggregated_user = pd.DataFrame(user_data)

# Define df_aggregated_transaction and df_aggregated_insurance 
df_aggregated_transaction = pd.DataFrame(clm)  
df_aggregated_insurance = pd.DataFrame(insurance_data)  

# Aggregated
df_aggregated_user.to_sql("aggregated_user", con=engine, if_exists="replace", index=False)
df_aggregated_transaction.to_sql("aggregated_transaction", con=engine, if_exists="replace", index=False)
df_aggregated_insurance.to_sql("aggregated_insurance", con=engine, if_exists="replace", index=False)

# Map
df_map_user = pd.DataFrame(map_user_data)  
df_map_transaction = pd.DataFrame(map_transaction_data)  
df_map_insurance = pd.DataFrame(map_insurance_data)  

df_map_user.to_sql("map_user", con=engine, if_exists="replace", index=False)
df_map_transaction.to_sql("map_transaction", con=engine, if_exists="replace", index=False)
df_map_insurance.to_sql("map_insurance", con=engine, if_exists="replace", index=False)

# Top
df_top_user = pd.DataFrame(top_user) 
df_top_transaction = pd.DataFrame(top_transaction)  
df_top_insurance = pd.DataFrame(top_insurance)  

df_top_user.to_sql("top_user", con=engine, if_exists="replace", index=False)
df_top_transaction.to_sql("top_transaction", con=engine, if_exists="replace", index=False)
df_top_insurance.to_sql("top_insurance", con=engine, if_exists="replace", index=False)


print("All DataFrames successfully loaded into MySQL!")
