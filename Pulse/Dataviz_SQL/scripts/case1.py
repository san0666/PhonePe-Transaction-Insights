import pandas as pd
import mysql.connector

# Step 1: Connect to  MySQL Database
conn = mysql.connector.connect(
    host='localhost',            
    user='root',      
    password='san2003',  
    database='phonepe'   
)

# Step 2: Write  4 SQL queries (Case 1)

# Query 1
query1 = """
SELECT state, year, quater, SUM(transacion_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state, year, quater
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2
query2 = """
SELECT transacion_type, year, quater, SUM(transacion_amount) AS total_amount
FROM aggregated_transaction
GROUP BY transacion_type, year, quater
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3
query3 = """
SELECT state, year, SUM(transacion_amount) AS yearly_amount
FROM aggregated_transaction
GROUP BY state, year
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Query 4
query4 = """
SELECT state, SUM(transacion_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 5
"""
df4 = pd.read_sql(query4, conn)
df4['query'] = 'Query 4'

# Step 3: Combine all results into one CSV
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)
combined_df.to_csv("case1_combined.csv", index=False)

conn.close()
print("case1_combined.csv created successfully!")
