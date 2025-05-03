import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case2():
    # Load combined data
    combined_df = pd.read_csv("sql_queries/case2_combined.csv")

    # Streamlit Title
    st.markdown("📄Raw Data")

    # Display raw data
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("Total Registered Users and App Opens by Device Brand")

    # Filter for Query 1
    df1 = combined_df[combined_df['query'] == 'Query 1']

    # Melt data for grouped bar plot
    df1_melted = df1.melt(id_vars='device_brand', value_vars=['total_registered', 'total_opens'], 
                        var_name='Metric', value_name='Count')

    # Plot grouped bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(x='device_brand', y='Count', hue='Metric', data=df1_melted)
    plt.title("Total Registered Users and App Opens by Device Brand")
    plt.xlabel("Device Brand")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("Engagement Rate per Device Brand per Quarter")

    # Filter for Query 2
    df2 = combined_df[combined_df['query'] == 'Query 2']

    # Plot
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=df2, x="quarter", y="engagement_rate", hue="device_brand", marker="o")
    plt.title("Engagement Rate per Device Brand per Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Engagement Rate (%)")
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("Device Usage by State")

    # Filter for Query 3
    df3 = combined_df[combined_df['query'] == 'Query 3']

    # Plot grouped bar chart by state and device brand
    plt.figure(figsize=(16, 8))
    sns.barplot(data=df3, x="state", y="registered", hue="device_brand")
    plt.title("Device Usage by State (Registered Users)")
    plt.xlabel("State")
    plt.ylabel("Registered Users")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)


