import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case1():
    # Step 1: Load the combined CSV file (case1_combined.csv)
    combined_df = pd.read_csv("sql_queries/case1_combined.csv")

    # Step 2: Visualize the results in Streamlit

    st.markdown("📄Raw Data")

    # Display the combined data
    st.write(combined_df)

    # Query 1 - Plot: Top 10 States by Transaction Amount (with Quarter Breakdown)
    st.subheader("Top 10 States by Transaction Amount with Year and Quarter Breakdown")

    # Filter for Query 1: State-wise transaction with year and quarter
    df1 = combined_df[combined_df['query'] == 'Query 1']

    # Group by state, year, and quarter and sum the transaction amount
    state_year_quarter = df1.groupby(["state", "year", "quater"])["total_amount"].sum().reset_index()

    # Get the top 10 states by total transaction amount (aggregated across all years and quarters)
    top_states = state_year_quarter.groupby("state")["total_amount"].sum().sort_values(ascending=False).head(10).reset_index()

    # Filter the data to include only the top 10 states
    top_states_data = state_year_quarter[state_year_quarter["state"].isin(top_states["state"])]

    # Create a barplot for Query 1
    plt.figure(figsize=(14,8))
    sns.barplot(x="total_amount", y="state", hue="quater", data=top_states_data)
    plt.title("Top 10 States by Transaction Amount with Year and Quarter Breakdown")
    plt.xlabel("Transaction Amount")
    plt.ylabel("State")
    plt.tight_layout()
    st.pyplot(plt)

    # Query 2 - Plot: Transaction Type-wise (Aggregated by Year and Quarter)
    st.subheader("Transaction Type-wise Amount with Year and Quarter Breakdown")

    # Filter for Query 2: Transaction type-wise
    df2 = combined_df[combined_df['query'] == 'Query 2']

    # Group by transaction type, year, and quarter and sum the transaction amount
    transaction_type_data = df2.groupby(["transacion_type", "year", "quater"])["total_amount"].sum().reset_index()

    # Create a barplot for Query 2
    plt.figure(figsize=(14,8))
    sns.barplot(x="total_amount", y="transacion_type", hue="quater", data=transaction_type_data)
    plt.title("Transaction Type-wise Amount with Year and Quarter Breakdown")
    plt.xlabel("Transaction Amount")
    plt.ylabel("Transaction Type")
    plt.tight_layout()
    st.pyplot(plt)

    # Query 3 - Plot: State-wise Yearly Transaction (Query 3)
    st.subheader("State-wise Yearly Transaction Amount")

    # Filter for Query 3: State-wise yearly transaction
    df3 = combined_df[combined_df['query'] == 'Query 3']

    # Create a barplot for Query 3
    plt.figure(figsize=(14,8))
    sns.barplot(x="year", y="yearly_amount", hue="state", data=df3)
    plt.title("State-wise Yearly Transaction Amount")
    plt.xlabel("Year")
    plt.ylabel("Transaction Amount")
    plt.tight_layout()
    st.pyplot(plt)

    # Query 4 - Plot: Top 5 States by Total Transaction Amount (Query 4)
    st.subheader("Top 5 States by Total Transaction Amount")

    # Filter for Query 4: Top 5 states
    df4 = combined_df[combined_df['query'] == 'Query 4']

    # Create a barplot for Query 4
    plt.figure(figsize=(10,6))
    sns.barplot(x="total_amount", y="state", data=df4)
    plt.title("Top 5 States by Total Transaction Amount")
    plt.xlabel("Transaction Amount")
    plt.ylabel("State")
    plt.tight_layout()
    st.pyplot(plt)
