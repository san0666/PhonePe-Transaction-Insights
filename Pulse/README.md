# PhonePe Transaction Insights

## 🚀 Purpose

With the increasing reliance on digital payment systems like PhonePe, understanding the dynamics of transactions, user engagement, and insurance-related data is crucial for improving services and targeting users effectively. This project aims to analyze and visualize aggregated values of payment categories, create maps for total values at state and district levels, and identify top-performing states, districts, and pin codes. By exploring trends, building visualizations, and creating an interactive dashboard, we aim to provide deeper insights into the digital payments landscape.

---

## 📝 Table of Contents

- [PhonePe Transaction Insights](#phonepe-transaction-insights)
  - [🚀 Purpose](#-purpose)
  - [📊 Main Features & Highlights](#-main-features--highlights)
  - [📁 Folder Structure](#-folder-structure)
  - [🔧 Installation & Setup](#-installation--setup)
  - [🖥️ Running the Project](#-running-the-project)
  - [📋 Business Case Studies Solved](#-business-case-studies-solved)
  - [🔒 License](#-license)

---

## 📊 Main Features & Highlights

This project aims to analyze and visualize the dynamics of transactions, user engagement, and insurance data on the PhonePe platform. The following business case studies have been solved through comprehensive data analysis:

1. **Decoding Transaction Dynamics on PhonePe**  
   - **Scenario:** Analyze variations in transaction behavior across states, quarters, and payment categories.  
   - **Objective:** Identify trends of growth, stagnation, or decline in transaction data to guide targeted business strategies.

2. **Device Dominance and User Engagement Analysis**  
   - **Scenario:** Understand user preferences across different device brands and their engagement with the PhonePe app.  
   - **Objective:** Investigate trends in device usage across regions and identify underutilized devices to improve app performance and user engagement.

3. **Insurance Penetration and Growth Potential Analysis**  
   - **Scenario:** Assess the growth trajectory of PhonePe’s insurance offerings.  
   - **Objective:** Analyze insurance adoption at the state level to identify untapped opportunities and prioritize regions for marketing and partnerships with insurers.

4. **Transaction Analysis for Market Expansion**  
   - **Scenario:** Explore transaction dynamics at the state level to guide PhonePe’s market expansion strategy.  
   - **Objective:** Identify trends, opportunities, and areas for expansion to make informed strategic decisions.

5. **User Engagement and Growth Strategy**  
   - **Scenario:** Analyze user engagement across states and districts to improve growth strategies.  
   - **Objective:** Gain insights into user behavior and enhance market position through data-driven growth strategies.

6. **Insurance Engagement Analysis**  
   - **Scenario:** Understand the uptake of insurance services by users across different regions.  
   - **Objective:** Provide insights into user behavior and market demand for insurance, identifying potential growth areas for insurance offerings.

7. **Transaction Analysis Across States and Districts**  
   - **Scenario:** Identify top-performing states, districts, and pin codes based on transaction volume and value.  
   - **Objective:** Understand user engagement patterns and guide targeted marketing efforts.

8. **User Registration Analysis**  
   - **Scenario:** Identify top states, districts, and pin codes with the highest user registration during a specific period.  
   - **Objective:** Provide insights into user growth patterns and identify regions for potential market expansion.

9. **Insurance Transactions Analysis**  
   - **Scenario:** Analyze insurance transactions to pinpoint areas with high engagement.  
   - **Objective:** Help PhonePe make informed decisions on expanding insurance offerings and improve strategic targeting.

---

## 📁 Folder Structure

phonepe_pulse_data/
├── Pulse/
│ └── data/
│ ├── aggregated/ # Contains aggregated transaction, user, and insurance data
│ ├── map/ # Contains map-level data (state & district)
│ └── top/ # Contains top-performing states, districts, and pin codes
├── data_scripts/
│ └── Aggregated scripts # Scripts to convert JSON data into CSV format
│ └── map_scripts/ # Scripts for processing map data
│ └── top_scripts/ # Scripts for processing top-performing data
├── dataviz_SQL/
| └──chart_queries # visualizing each cases
│ └── sql_queries/ # SQL queries to interact with the MySQL database
│ └── scripts/ # Data analysis scripts
│ └── visuals/ # Data visualization scripts
| └── Dashboard.py # Streamlit app for interactive data visualization
├── load_to_mysql/
| └── main.py # Scripts to load processed data into MySQL
|__ppt # This folder contains the PowerPoint presentation files related to the project PhonePe Transaction Insights. The presentation highlights key business insights, visualizations, and analyses derived from the case studies.



---

## 🔧 Installation & Setup

To get started with this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository-link.git
   cd PhonePe-Transaction-Insights

2. Install the required dependencies:
(pandas
matplotlib
seaborn
streamlit
mysql-connector-python)# these are the requirements

3. Navigate to the Pulse folder:
cd Pulse

4. Navigate to the dataviz_SQL folder:
cd dataviz_SQL

🖥️ Running the Project
To run the project, execute the following command to launch the Streamlit dashboard:

streamlit run Dashboard.py

This will start a local server, and you can access the interactive dashboard in your browser.
.

📋 Business Case Studies Solved
The project includes the analysis of nine key business case studies based on PhonePe's data:

Decoding Transaction Dynamics

Device Dominance and User Engagement

Insurance Penetration and Growth

Market Expansion

User Engagement and Growth

Insurance Engagement

Transaction Analysis Across States and Districts

User Registration Analysis

Insurance Transactions Analysis

Each case study helps uncover valuable insights into PhonePe's operations, user behavior, and market potential.

🔒 License
This project is licensed under the MIT License.

This `README.md` file should now serve as a comprehensive guide for your project. It includes all the necessary sections and highlights for a user to understand, set up, and run the project effectively.



