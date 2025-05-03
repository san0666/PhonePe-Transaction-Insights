import pandas as pd
import mysql.connector

# Step 1: Connect to  MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Query 1: Total Insurance Transactions and Amount by State
query1 = """
SELECT 
  state,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM aggregated_insurance
GROUP BY state
ORDER BY total_amount DESC;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2: Quarterly Growth Trend of Insurance Amounts
query2 = """
SELECT 
  year,
  quarter,
  SUM(count) AS total_transactions,
  SUM(amount) AS total_amount
FROM aggregated_insurance
GROUP BY year, quarter
ORDER BY year, quarter;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3: Insurance Trends by State and Year
query3 = """
SELECT 
  state,
  year,
  SUM(count) AS yearly_transactions,
  SUM(amount) AS yearly_amount
FROM aggregated_insurance
GROUP BY state, year
ORDER BY year, yearly_amount DESC;
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Query 4: Top 5 States with Highest Insurance Value
query4 = """
SELECT 
  state,
  SUM(amount) AS total_insurance_value
FROM aggregated_insurance
GROUP BY state
ORDER BY total_insurance_value DESC
LIMIT 5;
"""
df4 = pd.read_sql(query4, conn)
df4['query'] = 'Query 4'

# Combine all query results into one DataFrame
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Export to CSV
combined_df.to_csv("case3_combined.csv", index=False)

# Close the database connection
conn.close()

print("case3_combined.csv created successfully!")
