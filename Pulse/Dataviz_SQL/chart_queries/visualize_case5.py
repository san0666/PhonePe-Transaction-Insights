import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case5():
    # Load combined data for case5
    combined_df = pd.read_csv("sql_queries/case5_combined.csv")

    # Display raw data
    st.markdown("📄Raw Data")
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("💡 Total Users and Engagement by State")

    df1 = combined_df[combined_df['query'] == 'Query 1'].dropna(subset=['state', 'total_registered', 'total_app_opens'])

    # Bar plot - Total App Opens by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='total_app_opens', palette='Blues_d')
    plt.title("Total App Opens by State", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Total App Opens")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Engagement Rate by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='engagement_rate', palette='viridis')
    plt.title("Engagement Rate by State", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Engagement Rate (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("📈 Engagement Trends Over Time by State")

    df2 = combined_df[combined_df['query'] == 'Query 2'].dropna(subset=['state', 'year', 'quarter', 'users', 'opens'])

    # Lineplot - App Opens over Quarters by State
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df2, x='quarter', y='opens', hue='state', marker='o')
    plt.title("App Opens Over Quarters by State", fontsize=16)
    plt.xlabel("Quarter")
    plt.ylabel("App Opens")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("🌟 Top 5 States with Highest Engagement")

    df3 = combined_df[combined_df['query'] == 'Query 3'].dropna(subset=['state', 'engagement_rate'])
    df3 = df3.sort_values(by="engagement_rate", ascending=False).head(5)

    # Highlight top state
    top_state = df3.iloc[0]['state']
    top_engagement = df3.iloc[0]['engagement_rate']
    st.markdown(f"**🚀 Top Engaged State:** {top_state} — {top_engagement}%")

    # Bar plot - Top 5 States with Highest Engagement
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df3, x='state', y='engagement_rate', palette='Set2')
    plt.title("Top 5 States by Engagement Rate", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Engagement Rate (%)")
    plt.tight_layout()
    st.pyplot(plt)
