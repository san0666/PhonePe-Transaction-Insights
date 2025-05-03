import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case6():
    
    # Load the cleaned CSV files
    query1_df = pd.read_csv("sql_queries/cleaned_query1.csv")
    query2_df = pd.read_csv("sql_queries/cleaned_query2.csv")

    # ------------------- Query 1 -------------------
    st.subheader("🔍 Insurance Summary for States and Districts")
    st.dataframe(query1_df)

    # Display number of records for Query 1
    st.write(f"Number of records for Query 1: {len(query1_df)}")

    if len(query1_df) > 0:
        # Barplot: Total Insurance Value by Entity
        plt.figure(figsize=(14, 6))
        sns.barplot(data=query1_df.sort_values(by='total_insurance_value', ascending=False).head(20),
                    x='entity_name', y='total_insurance_value', hue='entity_type')
        plt.title("Top 20 Insurance Transactions by Value")
        plt.xlabel("Entity Name")
        plt.ylabel("Total Insurance Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.write("No data available for Query 1.")

    # ------------------- Query 2 -------------------
    st.subheader("📈 Quarterly Insurance Trends (Nationwide)")
    st.dataframe(query2_df)

    # Display number of records for Query 2
    st.write(f"Number of records for Query 2: {len(query2_df)}")

    if len(query2_df) > 0:
        # Lineplot: Insurance Amount Over Quarters
        plt.figure(figsize=(12, 5))
        sns.lineplot(data=query2_df, x='quarter', y='total_amount', hue='year', marker='o', palette='tab10')
        plt.title("Quarterly Insurance Value Over Time")
        plt.xlabel("Quarter")
        plt.ylabel("Total Insurance Value")
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.write("No data available for Query 2.")
