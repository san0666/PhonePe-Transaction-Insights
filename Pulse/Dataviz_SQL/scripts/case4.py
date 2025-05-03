import pandas as pd
import mysql.connector

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Query 1: Total Transactions and Value by State
query1 = """
SELECT 
  state,
  SUM(transacion_count) AS total_transactions,
  SUM(transacion_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2: Year-over-Year Growth by State
query2 = """
SELECT 
  state,
  year,
  SUM(transacion_count) AS yearly_transactions,
  SUM(transacion_amount) AS yearly_amount
FROM aggregated_transaction
GROUP BY state, year
ORDER BY state, year;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3: Top 5 Emerging States (Last Year Only)
query3 = """
SELECT 
  state,
  SUM(transacion_amount) AS recent_amount
FROM aggregated_transaction
WHERE year = 2024 
GROUP BY state
ORDER BY recent_amount DESC
LIMIT 5;
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Combine all query results into one DataFrame
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Export to CSV
combined_df.to_csv("case4_combined.csv", index=False)

# Close the database connection
conn.close()

print("case4_combined.csv created successfully!")
