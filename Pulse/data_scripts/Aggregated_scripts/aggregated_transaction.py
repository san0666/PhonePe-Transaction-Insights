import pandas as pd # type: ignore
import json
import os

# Path to the transaction data folder
path = "pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path)

# Create a dictionary to hold extracted data
clm = {
    'State': [], 
    'Year': [], 
    'Quater': [], 
    'Transacion_type': [], 
    'Transacion_count': [], 
    'Transacion_amount': []
}

# Loop through each state folder
for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        
        for k in Agg_yr_list:
            p_k = p_j + k
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    
                    clm['Transacion_type'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))

# Create a DataFrame from the dictionary
df_aggregated_transaction = pd.DataFrame(clm)

# Print preview
print(df_aggregated_transaction.head())
