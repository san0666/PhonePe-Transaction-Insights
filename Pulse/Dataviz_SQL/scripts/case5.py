import pandas as pd
import mysql.connector

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Query 1: Total Users and Engagement by State
query1 = """
SELECT 
  state,
  SUM(registered_users) AS total_registered,
  SUM(app_opens) AS total_app_opens,
  ROUND(SUM(app_opens) * 100.0 / NULLIF(SUM(registered_users), 0), 2) AS engagement_rate
FROM aggregated_user
GROUP BY state
ORDER BY engagement_rate DESC;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2: Engagement Trends Over Time (Quarterly)
query2 = """
SELECT 
  state,
  year,
  quarter,
  SUM(registered_users) AS users,
  SUM(app_opens) AS opens,
  ROUND(SUM(app_opens) * 100.0 / NULLIF(SUM(registered_users), 0), 2) AS engagement_rate
FROM aggregated_user
GROUP BY state, year, quarter
ORDER BY state, year, quarter;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3: Top 5 States with Highest App Engagement
query3 = """
SELECT 
  state,
  ROUND(SUM(app_opens) * 100.0 / NULLIF(SUM(registered_users), 0), 2) AS engagement_rate
FROM aggregated_user
GROUP BY state
ORDER BY engagement_rate DESC
LIMIT 5;
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Combine all query results into one DataFrame
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Export to CSV
combined_df.to_csv("case5_combined.csv", index=False)

# Close the database connection
conn.close()

print("case5_combined.csv created successfully!")
