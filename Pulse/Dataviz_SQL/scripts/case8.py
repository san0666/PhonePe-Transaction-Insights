import pandas as pd
import mysql.connector

# Step 1: Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='san2003',
    database='phonepe'
)

# Query 1: Top States by User Registrations (Quarter 1, 2018–2024)
query1 = """
SELECT
    entity_name AS state,
    SUM(registered_users) AS total_registrations
FROM
    top_user
WHERE
    entity_type = 'state'
    AND year BETWEEN 2018 AND 2024 
    AND quarter = 1
GROUP BY
    entity_name
ORDER BY
    total_registrations DESC
LIMIT 10;
"""
df1 = pd.read_sql(query1, conn)
df1['query'] = 'Query 1'

# Query 2: Top Districts by User Registrations (Quarter 1, 2018–2024)
query2 = """
SELECT
    entity_name AS district,
    SUM(registered_users) AS total_registrations
FROM
    top_user
WHERE
    entity_type = 'district'
    AND year BETWEEN 2018 AND 2024
    AND quarter = 1
GROUP BY
    entity_name
ORDER BY
    total_registrations DESC
LIMIT 10;
"""
df2 = pd.read_sql(query2, conn)
df2['query'] = 'Query 2'

# Query 3: Top Pin Codes by User Registrations (Quarter 1, 2018–2024)
query3 = """
SELECT
    entity_name AS pin_code,
    SUM(registered_users) AS total_registrations
FROM
    top_user
WHERE
    entity_type = 'pincode'
    AND year BETWEEN 2018 AND 2024
    AND quarter = 1
GROUP BY
    entity_name
ORDER BY
    total_registrations DESC
LIMIT 10;
"""
df3 = pd.read_sql(query3, conn)
df3['query'] = 'Query 3'

# Combine all query results
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# Export to CSV
combined_df.to_csv("case8_combined.csv", index=False)

# Close DB connection
conn.close()

print(" case8_combined.csv created successfully!")
