import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case4():
    # Load combined data for case4
    combined_df = pd.read_csv("sql_queries/case4_combined.csv")

    # Display raw data
    st.markdown("📄Raw Data")
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("💰 Total Transactions and Value by State")

    df1 = combined_df[combined_df['query'] == 'Query 1'].dropna(subset=['state', 'total_transactions', 'total_amount'])

    # Bar plot - Total Transaction Amount by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='total_amount', palette='Blues_d')
    plt.title("Total Transaction Amount by State", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("📈 Year-over-Year Growth by State")

    df2 = combined_df[combined_df['query'] == 'Query 2'].dropna(subset=['state', 'year', 'yearly_transactions', 'yearly_amount'])

    # Lineplot - Yearly Transaction Amount by State
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df2, x='year', y='yearly_amount', hue='state', marker='o')
    plt.title("Year-over-Year Transaction Amount by State", fontsize=16)
    plt.xlabel("Year")
    plt.ylabel("Yearly Amount")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("🌟 Top 5 Emerging States in 2024")

    df3 = combined_df[combined_df['query'] == 'Query 3'].dropna(subset=['state', 'recent_amount'])
    df3 = df3.sort_values(by="recent_amount", ascending=False).head(5)

    # Highlight top emerging state
    top_state = df3.iloc[0]['state']
    top_amount = df3.iloc[0]['recent_amount']
    st.markdown(f"**🚀 Top Emerging State in 2024:** {top_state} — ₹{top_amount:,.2f}")

    # Bar plot - Top 5 Emerging States
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df3, x='state', y='recent_amount', palette='Set2')
    plt.title("Top 5 States by Transaction Amount in 2024", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Transaction Amount (₹)")
    plt.tight_layout()
    st.pyplot(plt)
