import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case3():
    # Load combined data
    combined_df = pd.read_csv("sql_queries/case3_combined.csv")

    # Display raw data
    st.markdown("📄Raw Data")
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("💰 Total Insurance Transactions and Amount by State")

    df1 = combined_df[combined_df['query'] == 'Query 1']

    # Bar plot for total amount
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x="state", y="total_amount", palette="viridis")
    plt.title("Total Insurance Amount by State")
    plt.xlabel("State")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("📈 Quarterly Growth of Insurance Amounts")

    df2 = combined_df[combined_df['query'] == 'Query 2']

    # Line plot for total amount over quarters
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df2, x="quarter", y="total_amount", hue="year", marker="o")
    plt.title("Quarterly Insurance Amount Growth")
    plt.xlabel("Quarter")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("📊 Insurance Trends by State and Year")

    df3 = combined_df[combined_df['query'] == 'Query 3']

    # Heatmap pivot
    pivot_df = df3.pivot_table(values='yearly_amount', index='state', columns='year', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_df, cmap="YlGnBu", annot=True, fmt=".0f")
    plt.title("Yearly Insurance Amount by State")
    plt.xlabel("Year")
    plt.ylabel("State")
    st.pyplot(plt)

    # ----------------- Query 4 ------------------
    st.subheader("🏆 Top 5 States with Highest Insurance Value")

    df4 = combined_df[combined_df['query'] == 'Query 4']

    # Drop rows where state or insurance value is missing
    df4 = df4.dropna(subset=["state", "total_insurance_value"])

    # Sort by value and pick top 5
    df4 = df4.sort_values(by="total_insurance_value", ascending=False).head(5)

    # Display state with highest insurance value
    top_state = df4.iloc[0]["state"]
    top_value = df4.iloc[0]["total_insurance_value"]
    st.markdown(f"**🥇 State with Highest Insurance Value:** {top_state} — ₹{top_value:,.2f}")

    # Pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(df4["total_insurance_value"], labels=df4["state"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title("Top 5 States by Insurance Value")
    st.pyplot(plt)
