import pandas as pd
import mysql.connector

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Query 1: Top-Performing States by Transaction Value
query1 = """
SELECT 
  entity_name AS state,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM top_transaction
WHERE entity_type = 'state'
GROUP BY entity_name
ORDER BY total_amount DESC;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2: Top Districts by Transaction Value
query2 = """
SELECT 
  entity_name AS district,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM top_transaction
WHERE entity_type = 'district'
GROUP BY entity_name
ORDER BY total_amount DESC;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3: Top Pin Codes by Transaction Volume
query3 = """
SELECT 
  entity_name AS pincode,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM top_transaction
WHERE entity_type = 'pincode'
GROUP BY entity_name
ORDER BY total_transactions DESC
LIMIT 10;
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Query 4: Quarterly Trends for All Entity Types
query4 = """
SELECT 
  entity_type,
  year,
  quarter,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM top_transaction
GROUP BY entity_type, year, quarter
ORDER BY entity_type, year, quarter;
"""
df4 = pd.read_sql(query4, conn)
df4['query'] = 'Query 4'

# Combine all query results into one DataFrame
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Export to CSV
combined_df.to_csv("case7_combined.csv", index=False)

# Close the database connection
conn.close()

print("case7_combined.csv created successfully!")
