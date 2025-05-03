import pandas as pd
import mysql.connector

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Query 1: Insurance Summary for States and Districts
query1 = """
SELECT 
  entity_type,
  entity_name,
  SUM(count) AS total_insurance_transactions,
  SUM(amount) AS total_insurance_value
FROM top_insurance
WHERE entity_type IN ('state', 'district')
GROUP BY entity_type, entity_name
ORDER BY entity_type, total_insurance_value DESC;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'
print(f"Query 1 DataFrame Shape: {df1.shape}")
print(df1.head())

# Query 2: Quarterly Insurance Trends (Nationwide)
query2 = """
SELECT 
  year,
  quarter,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM top_insurance
GROUP BY year, quarter
ORDER BY year, quarter;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'
print(f"Query 2 DataFrame Shape: {df2.shape}")
print(df2.head())

# Combine all DataFrames into one
combined_df = pd.concat([df1, df2], ignore_index=True)

# Check combined dataframe
print(f"Combined DataFrame Shape: {combined_df.shape}")
print(combined_df.head())

# Export to CSV
combined_df.to_csv("case6_combined.csv", index=False)

# Close the connection
conn.close()

print("case6_combined.csv created successfully!")
