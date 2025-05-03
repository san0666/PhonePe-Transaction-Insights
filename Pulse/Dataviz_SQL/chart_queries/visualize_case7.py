import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case7():
    
    # Load combined data for Case 7
    combined_df = pd.read_csv("sql_queries/case7_combined.csv")

    # Display raw data
    st.markdown("📄Raw Data")
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("💡 Top-Performing States by Transaction Value")

    df1 = combined_df[combined_df['query'] == 'Query 1'].dropna(subset=['state', 'total_transactions', 'total_amount'])

    # Bar plot - Total Transactions by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='total_transactions', palette='Blues_d')
    plt.title("Total Transactions by State", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Bar plot - Total Amount by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='total_amount', palette='viridis')
    plt.title("Total Amount by State", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("📈 Top Districts by Transaction Value")

    df2 = combined_df[combined_df['query'] == 'Query 2'].dropna(subset=['district', 'total_transactions', 'total_amount'])

    # Bar plot - Total Transactions by District
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df2, x='district', y='total_transactions', palette='Blues_d')
    plt.title("Total Transactions by District", fontsize=16)
    plt.xlabel("District")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Bar plot - Total Amount by District
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df2, x='district', y='total_amount', palette='viridis')
    plt.title("Total Amount by District", fontsize=16)
    plt.xlabel("District")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("🌟 Top Pin Codes by Transaction Volume")

    df3 = combined_df[combined_df['query'] == 'Query 3'].dropna(subset=['pincode', 'total_transactions', 'total_amount'])

    # Bar plot - Total Transactions by Pincode
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df3, x='pincode', y='total_transactions', palette='Blues_d')
    plt.title("Total Transactions by Pincode", fontsize=16)
    plt.xlabel("Pincode")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Bar plot - Total Amount by Pincode
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df3, x='pincode', y='total_amount', palette='viridis')
    plt.title("Total Amount by Pincode", fontsize=16)
    plt.xlabel("Pincode")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 4 ------------------
    st.subheader("📊 Quarterly Trends for All Entity Types")

    df4 = combined_df[combined_df['query'] == 'Query 4'].dropna(subset=['entity_type', 'year', 'quarter', 'total_transactions', 'total_amount'])

    # Lineplot - Total Transactions by Quarter and Entity Type
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df4, x='quarter', y='total_transactions', hue='entity_type', marker='o')
    plt.title("Total Transactions by Quarter and Entity Type", fontsize=16)
    plt.xlabel("Quarter")
    plt.ylabel("Total Transactions")
    plt.legend(title='Entity Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)

    # Lineplot - Total Amount by Quarter and Entity Type
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df4, x='quarter', y='total_amount', hue='entity_type', marker='o')
    plt.title("Total Amount by Quarter and Entity Type", fontsize=16)
    plt.xlabel("Quarter")
    plt.ylabel("Total Amount")
    plt.legend(title='Entity Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)
