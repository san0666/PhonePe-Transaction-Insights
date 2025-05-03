import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case9():
    # Load combined data for Case 9
    combined_df = pd.read_csv("sql_queries/case9_combined.csv")

    # Display raw data with emoji
    st.markdown("📄**Raw Data**")
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("📍 Top States by Insurance Transactions")

    df1 = combined_df[combined_df['query'] == 'Query 1'].dropna(subset=['state', 'total_transactions'])

    # Bar plot - Total Transactions by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='total_transactions', palette='viridis')
    plt.title("Top States by Insurance Transactions", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("🏙️ Top Districts by Insurance Transactions")

    df2 = combined_df[combined_df['query'] == 'Query 2'].dropna(subset=['district', 'total_transactions'])

    # Bar plot - Total Transactions by District
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df2, x='district', y='total_transactions', palette='mako')
    plt.title("Top Districts by Insurance Transactions", fontsize=16)
    plt.xlabel("District")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("📮 Top Pin Codes by Insurance Transactions")

    df3 = combined_df[combined_df['query'] == 'Query 3'].dropna(subset=['pincode', 'total_transactions'])

    df3['total_transactions'] = pd.to_numeric(df3['total_transactions'], errors='coerce')

    # Bar plot - Total Transactions by Pincode
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df3, x='pincode', y='total_transactions', palette='flare')
    plt.title("Top Pincodes by Insurance Transactions", fontsize=16)
    plt.xlabel("Pin Code")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
