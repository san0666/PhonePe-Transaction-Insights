import pandas as pd

# Load the messy CSV
raw_df = pd.read_csv("case6_combined.csv", header=None)

# Define header columns for all possible values
columns = ['entity_type', 'entity_name', 'total_insurance_transactions', 'total_insurance_value',
           'query', 'year', 'quarter', 'total_transactions', 'total_amount', 'district']

# Assign column names
raw_df.columns = columns

# Drop fully empty rows
raw_df.dropna(how='all', inplace=True)

# Separate Query 1 and Query 2
query1_df = raw_df[raw_df['query'] == 'Query 1'].copy()
query2_df = raw_df[raw_df['query'] == 'Query 2'].copy()

# For Query 1, select relevant columns
query1_df = query1_df[['entity_type', 'entity_name', 'total_insurance_transactions', 'total_insurance_value', 'district']]

# For Query 2, select relevant columns
query2_df = query2_df[['year', 'quarter', 'total_transactions', 'total_amount']]

# Save cleaned files
query1_df.to_csv("cleaned_query1.csv", index=False)
query2_df.to_csv("cleaned_query2.csv", index=False)

print("Cleaned CSVs saved as 'cleaned_query1.csv' and 'cleaned_query2.csv'")
