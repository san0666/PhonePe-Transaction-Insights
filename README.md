# 📊 **PhonePe Transaction Insights** 🚀

## 🎯 **Purpose**
In today's fast-paced digital world, **PhonePe**, a leading digital payments platform, is constantly striving to provide insights into user behavior, transaction dynamics, device usage, and market expansion. This project aims to decode these patterns, enhance user engagement, and optimize the growth trajectory, especially in the insurance domain. 

By analyzing and visualizing aggregated transaction data, we uncover actionable insights that can guide business strategies for better targeting, user acquisition, and retention.

### 🚀 **Key Insights**:
- **Transaction Dynamics**: Understand how different states, districts, and payment categories perform over time.
- **Device Preferences**: Explore user engagement and device dominance across regions.
- **Insurance Growth Potential**: Pinpoint regions where insurance offerings can be expanded.
- **Market Expansion**: Identify the most promising regions for growth based on transaction data.
- **User Engagement & Strategy**: Develop insights into user behavior for strategic decision-making.

---

## 💻 **Technologies Used** 🛠️
- **Python** (Pandas, Matplotlib, Seaborn, Streamlit)
- **MySQL** (for data storage and querying)
- **Streamlit** (for building the interactive dashboard)
- **GeoJSON** (for visualization maps)

---

## 🗂️ **Folder Structure**

phonepe_pulse_data/
├── Pulse/
│   └── data/
│       ├── aggregated/         # Contains aggregated transaction, user, and insurance data
│       ├── map/                # Contains map-level data (state & district)
│       └── top/                # Contains top-performing states, districts, and pin codes
├── data_scripts/
│   ├── aggregated_scripts/    # Scripts to convert JSON data into CSV format
│   ├── map_scripts/           # Scripts for processing map data
│   └── top_scripts/           # Scripts for processing top-performing data
├── dataviz_SQL/
│   ├── chart_queries/         # SQL queries for visualizing each case
│   ├── sql_queries/           # SQL queries to interact with the MySQL database
│   ├── scripts/               # Data analysis scripts
│   └── visuals/               # Data visualization scripts
├── load_to_mysql/
│   └── main.py                # Script to load processed data into MySQL
├── dashboard/
│   └── Dashboard.py           # Streamlit app for interactive data visualization
└── ppt/
    └── PhonePe_Transaction_Insights.pptx  # PowerPoint presentation of the project
    
------
📦 Installation & Setup 🛠️
1. Clone the Repository 🔗
To get started, clone the project to your local machine using:
git clone https://github.com/san0666/PhonePe-Transaction-Insights.git

3. Install Dependencies 📥
Navigate to the project folder and install all necessary dependencies:
cd PhonePe-Transaction-Insights
pip install -r requirements.txt

5. Run the Streamlit Dashboard 🚀
Once the dependencies are installed, navigate to the dashboard directory and run the Streamlit app
cd dashboard
streamlit run Dashboard.py
This will start the dashboard in your default web browser.

"Project Features & Case Studies" 📊
1.Decoding Transaction Dynamics on PhonePe:
🏙️ Analyzes transaction behaviors across states, districts, and payment categories to provide actionable business insights.

2.Device Dominance and User Engagement Analysis:
📱 Explores device preferences and app engagement across different regions to optimize user experience.

3.Insurance Penetration and Growth Potential Analysis:
🛡️ Identifies potential regions for expanding insurance offerings based on transaction and user data.

4.Transaction Analysis for Market Expansion:
🌍 Provides insights into transaction trends at the state level, revealing promising regions for market expansion.

5.User Engagement and Growth Strategy:
👥 Unveils user engagement patterns, helping to shape strategic decisions for improving market positioning.

6.Insurance Engagement Analysis:
🔍 Offers insights into the uptake of insurance services and reveals opportunities for growth within the sector.

7.Transaction Analysis Across States and Districts:
📈 Identifies the top-performing regions (states, districts, and pin codes) based on transaction volume and value.

8.User Registration Analysis:
📝 Identifies where the highest number of users are registering, helping to highlight areas for potential growth.

9.Insurance Transactions Analysis:
📊 Analyzes insurance-related transactions to understand user engagement and strategic areas for improvement.

📈 Interactive Dashboard 🔍:
This project includes a Streamlit dashboard that allows for interactive data exploration. You can visualize transaction dynamics, insurance data, and user engagement, and drill down into specific states, districts, and time periods. The dashboard is built using Streamlit and integrates both transaction and insurance data, offering powerful visualizations and insights.

-------
🧑‍💻 Requirements
Make sure you have the following installed:

Python 3.x (any version above 3.6)

MySQL (for data storage)

Streamlit (for building and running the dashboard)

-----
Required Libraries:
*Pandas

*Matplotlib

*Seaborn

*Streamlit

*MySQL Connector (for database interaction)

*GeoJSON

-------
🔒 License 📝
This project is licensed under the MIT License. See the LICENSE file for more details.

📧 Contact
For any questions or suggestions, feel free to reach out to me via email at:
Email: sanjanaa543@gmail.com

🌱 Contributing 🤝
Contributions are always welcome! If you have any ideas or improvements, please feel free to fork this repository, create a pull request, and I’ll be happy to review it.

✨ Acknowledgements 💡
This project would not have been possible without the following resources:
->PhonePe Pulse Data
->Streamlit Documentation
->MySQL Documentation
