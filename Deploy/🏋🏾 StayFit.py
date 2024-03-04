import streamlit as st

# Define the path to the project logo and introduction image
PROJECT_LOGO_PATH = "/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/logo.jpg"
INTRODUCTION_IMAGE_PATH = "/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/intro.jpg"

# Configure Streamlit page layout and appearance
st.set_page_config(
    page_title="🏋🏾 StayFit",
    page_icon="🏋🏾",
    layout="wide"
)

# Add project logo to the sidebar
st.sidebar.image(PROJECT_LOGO_PATH , width= 200 , caption="StayFit", use_column_width=True)

# Display project information in a container
with st.container():
    # Set the page title and subheader
    st.title(" 🏋🏾 StayFit For SmartWatches ⌚️ ")
    st.write("--------------------------------------------------")
    st.subheader("About My Project")
    
    # Provide a brief description of the project
    st.write(
        "My Final Project focuses on revolutionizing fitness tracking in gym environments. "
        "The objective is to design a machine learning model capable of accurately counting repetitions and "
        "classifying weightlifting exercises based on data collected from accelerometer and gyroscope sensors. "
        "The project began with meticulous data collection and preprocessing to ensure suitability for our objectives."
    )
    st.write("--------------------------------------------------")
    # Display the project goal
    st.subheader("Goal")
    st.write(
        "The goal is to empower fitness enthusiasts to track their progress and optimize training routines. "
        "By leveraging advanced machine learning techniques, our Python script provides users with actionable insights "
        "derived from biometric and behavioral data. This project aligns with the ethos of the quantified self movement, "
        "where individuals seek to enhance well-being through data-driven decision-making."
    )
    
    # Display introduction image
    st.image(INTRODUCTION_IMAGE_PATH , caption="StayFit", use_column_width=True , width=500)
    
# Display author information in the sidebar
st.sidebar.success("Made with ❤️ / \n Created by 0XNROUS")
