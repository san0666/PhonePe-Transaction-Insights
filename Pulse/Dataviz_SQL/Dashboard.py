import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import requests

# Import case study visualizations
from chart_queries.visualize_case1 import show_case1
from chart_queries.visualize_case2 import show_case2
from chart_queries.visualize_case3 import show_case3
from chart_queries.visualize_case4 import show_case4
from chart_queries.visualize_case5 import show_case5
from chart_queries.visualize_case6 import show_case6
from chart_queries.visualize_case7 import show_case7
from chart_queries.visualize_case8 import show_case8
from chart_queries.visualize_case9 import show_case9

# ------------------------- Streamlit Config -------------------------
from PIL import Image
import streamlit as st

# Set the page layout to wide mode for better horizontal space utilization
st.set_page_config(layout="wide")

# ------------------------- Custom CSS -------------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f9ff;
        }
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #4b4b4b;
            text-align: center;
        }
        .sub-text {
            font-size: 18px;
            text-align: center;
            color: #6e6e6e;
        }
        .sidebar .css-1d391kg {
            background-color: #f0f8ff;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------- Top Banner -------------------------

st.markdown('<div class="main-title"> PHONEPE TRANSACTION INSIGHTS DASHBOARD </div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">A comprehensive view of PhonePe transactions across India</div>', unsafe_allow_html=True)
st.markdown("---")
# Create a header container
from PIL import Image
import streamlit as st

# Open the image
image = Image.open("visuals/phonepe.png")

# Get original dimensions
original_width, original_height = image.size

# Set new width to stretch 
new_width = 1200 
new_height = int(original_height *0.6)
# Resize only the width, keeping original height
resized_image = image.resize((new_width, new_height))

# Display in Streamlit 
st.image(resized_image, use_container_width=True)

# ------------------------- Layout: Two Columns -------------------------
col1, col2 = st.columns([1.2, 2])

# ------------------------- Left Column: India Map -------------------------
with col1:
    st.header("🗺️ India Transaction Map")

    # Load transaction data
    df = pd.read_csv('visuals/states.csv')
    df['state'] = df['state'].str.title().str.strip()

    # Load GeoJSON for states
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    india_states = requests.get(geojson_url).json()

    # Choropleth Map
    fig = go.Figure(go.Choropleth(
        geojson=india_states,
        featureidkey='properties.ST_NM',
        locations=df['state'],
        z=df['total_transactions'],
        colorscale='Blues',
        colorbar_title="Transactions",
        marker_line_color='white',
        marker_line_width=0.7
    ))

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        height=550,
        geo=dict(projection_type='mercator'),
    )

    st.plotly_chart(fig, use_container_width=True)

# ------------------------- Right Column: Case Study Selector -------------------------
case_titles = {
    "Case 1": "📊 Decoding Transaction Dynamics on PhonePe",
    "Case 2": "📱 Device Dominance and User Engagement Analysis",
    "Case 3": "🛡️ Insurance Penetration and Growth Potential Analysis",
    "Case 4": "🌐 Transaction Analysis for Market Expansion",
    "Case 5": "📈 User Engagement and Growth Strategy",
    "Case 6": "🏥 Insurance Engagement Analysis",
    "Case 7": "📍 Transaction Analysis Across States and Districts",
    "Case 8": "👤 User Registration Analysis",
    "Case 9": "💼 Insurance Transactions Analysis"
}

with col2:
    st.header("📚 Explore Case Studies")
    selected_case = st.selectbox("Choose a Case Study", list(case_titles.keys()))
    st.subheader(case_titles[selected_case])

    # Display visualizations
    if selected_case == "Case 1":
        show_case1()
    elif selected_case == "Case 2":
        show_case2()
    elif selected_case == "Case 3":
        show_case3()
    elif selected_case == "Case 4":
        show_case4()
    elif selected_case == "Case 5":
        show_case5()
    elif selected_case == "Case 6":
        show_case6()
    elif selected_case == "Case 7":
        show_case7()
    elif selected_case == "Case 8":
        show_case8()
    elif selected_case == "Case 9":
        show_case9()
