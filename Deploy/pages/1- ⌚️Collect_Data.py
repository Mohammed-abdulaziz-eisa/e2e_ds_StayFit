#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import urllib.request

# Set page configuration and title
st.set_page_config(
    page_title='⌗ Collecting Data Process',
    page_icon='🏋🏾',
    layout='wide'
)
# Set custom styling
st.markdown(
    """
    <style>
    .st-cb {
        background-color: #f5f5f5;
    }
    .css-1e26y49 {
        font-family: Monospace;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Sidebar
st.sidebar.markdown("Made with ❤️ / Created by 0XNROUS")

# Main content
page_title = st.title("☞ Data Collection")
st.write("The program is made up of 5 fundamental barbell exercises: Bench Press, Deadlift, Overhead Press, Row, and Squat")
st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/barbell.jpg")

st.write("-----------------------------------------------------------------")
# Questions Container to make it easy for code reader to make it simple 
sensor_selection = st.container()
with sensor_selection:
    # Use an expander to hide and show question i asked before EDA 
    with st.expander(" 1. Sensor Selection and Setup  "):
        st.subheader("Accelerometer & Gyroscopes Sensors" )
        st.write("[ we use IPhone two application (Sensor-App) & (GFRecorder) for data collection due to widespread use and sensor integration.]")
        st.write("[ Sensor-App to get all gyroscope axis (X- axis for Left and Right movement) ]")
        st.write("[ Gforce Recorder to collect Accelerometer axis data  ")
        st.write("[(X- axis for Left and Right movement) and (Y- axis for Up and Down movement) and (Z- axis for Front and Back movement)]")
        st.write("[ we worked on five different smaples of people with different exercises]")            
        st.write("[ Finally Export the data to CSV file ]") 
        st.write("[We worked in basics barbell exercises (Bench Press, Deadlift, Overhead Press, Row, and Squat)]")
        col1 , col2 ,col3 = st.columns(3)
        with col1:
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/sensors.webp")
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/csv_export.webp")
        with col2:
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/ACC.webp")
        with col3:
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/Gyro.webp")
        

barbell_exercises = st.container()
with barbell_exercises:
        # Use an expander to hide and show question i asked before EDA 
        with st.expander(" 2. Barbell Exercises and Repetitions "):
            st.write("[ 1- Bench Press Exercise ]")
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/bench-press.jpg")
            st.write("[ 2- Squat Press Exercise ]")
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/squat.jpg")
            st.write("[ 3- Deadlift Exercise ]")
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/deadlift.jpg")
            st.write("[ 4- Row Exercise ]")
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/row.png")
            st.write("[ 5- Overhead Press Exercise ]")
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/overhead.png")
        

df = pd.read_csv("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/data/raw/raw_data.csv")
df_final = st.container()
with df_final:
        # Use an expander to hide and show question i asked before EDA 
        with st.expander(" Final Look of the data "):
            st.dataframe(df)
            st.write("--------------------------------------------------")
            col1 , col2 ,col3 = st.columns(3)
            with col1:
                st.write("First 3 axis of Accelerometer Sensor")
                st.write(df[['mean_xc','mean_yc','mean_zc']].head(3))
            with col2:
                st.write("Second 3 axis of Gyroscope Sensor")
                st.write(df[['mean_xg','mean_yg','mean_zg']].head(3))
            with col3:
                st.write("Last 4 Columns our categorical data")
                st.write(df[['posture','types','specimen ', 'set']].sample(3))
            st.write("--------------------------------------------------")
            st.subheader(" Our final dataset have 9009 rows and 11 columns")
            st.write("- we have 7 columns numeric ")
            st.write("- we have  3 columns categorical")
            st.write("- we have  1 column  datetime ")