import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_case8():
    # Load combined data for Case 8
    combined_df = pd.read_csv("sql_queries/case8_combined.csv")

    # Display raw data
    st.markdown("📄Raw Data")
    st.write(combined_df)

    # ----------------- Query 1 ------------------
    st.subheader("🏆 Top States by User Registrations")

    df1 = combined_df[combined_df['query'] == 'Query 1'].dropna(subset=['state', 'total_registrations'])

    # Bar plot - Total Registrations by State
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df1, x='state', y='total_registrations', palette='coolwarm')
    plt.title("Top States by User Registrations", fontsize=16)
    plt.xlabel("State")
    plt.ylabel("Total Registrations")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 2 ------------------
    st.subheader("🏙️ Top Districts by User Registrations")

    df2 = combined_df[combined_df['query'] == 'Query 2'].dropna(subset=['district', 'total_registrations'])

    # Bar plot - Total Registrations by District
    plt.figure(figsize=(14, 6))
    sns.barplot(data=df2, x='district', y='total_registrations', palette='crest')
    plt.title("Top Districts by User Registrations", fontsize=16)
    plt.xlabel("District")
    plt.ylabel("Total Registrations")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # ----------------- Query 3 ------------------
    st.subheader("📮 Top Pincodes by User Registrations")
    df3 = combined_df[combined_df['query'] == 'Query 3']

    # Drop rows where 'pin_code' or 'total_registrations' is NaN
    df3 = df3.dropna(subset=['pin_code', 'total_registrations'])

    # Convert 'total_registrations' to numeric if necessary
    df3['total_registrations'] = pd.to_numeric(df3['total_registrations'], errors='coerce')

    # Plotting using Matplotlib/Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='pin_code', y='total_registrations', data=df3)

    # Adding labels and title
    plt.xlabel('Pin Code')
    plt.ylabel('Total Registrations')
    plt.title('Top Pin Codes by Total Registrations')

    # Rotating x-axis labels for readability (if needed)
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(plt)