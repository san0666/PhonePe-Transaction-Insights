import pandas as pd
import mysql.connector

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Step 2: Write  3 SQL queries (Case 2)

# Query 1: Total Registered Users and App Opens by Device Brand
query1 = """
SELECT 
  device_brand,
  SUM(registered_users) AS total_registered,
  SUM(app_opens) AS total_opens
FROM aggregated_user
GROUP BY device_brand
ORDER BY total_registered DESC;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2: Compare App Opens vs Registrations Per Brand Per Quarter
query2 = """
SELECT 
  device_brand,
  year,
  quarter,
  SUM(registered_users) AS registered,
  SUM(app_opens) AS opens,
  ROUND(SUM(app_opens)*100.0 / NULLIF(SUM(registered_users), 0), 2) AS engagement_rate
FROM aggregated_user
GROUP BY device_brand, year, quarter
ORDER BY device_brand, year, quarter;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3: Device Usage by State
query3 = """
SELECT 
  state,
  device_brand,
  SUM(registered_users) AS registered,
  SUM(app_opens) AS opens
FROM aggregated_user
GROUP BY state, device_brand
ORDER BY state, registered DESC;
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Step 3: Combine all results into one CSV
combined_df = pd.concat([df1, df2, df3], ignore_index=True)
combined_df.to_csv("case2_combined.csv", index=False)

# Close the database connection
conn.close()

print("case2_combined.csv created successfully!")
