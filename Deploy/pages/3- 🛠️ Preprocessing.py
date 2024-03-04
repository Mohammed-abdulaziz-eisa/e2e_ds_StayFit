import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import pickle
import urllib.request

# Set page configuration and title
st.set_page_config(
    page_title='🛠️ Preprocessing Data Stage',
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
page_title = st.title("🛠️ Preprocessing Data ")
st.write("-----------------------------------------------------------------")
st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/preprocess_page.jpg")
st.write("-----------------------------------------------------------------")
st.write("In this stage we will explore and preprocess the data for further analysis.")
df = pd.read_pickle("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/data/interim/1_df_resampled_datetime.pkl")



# subplot function 
## Plotting outliers wz time :
def plot_binary_outliers_plotly(dataset, col, outlier_col, reset_index=False):
    dataset = dataset.dropna(subset=[col, outlier_col])
    dataset[outlier_col] = dataset[outlier_col].astype(bool)

    if reset_index:
        dataset = dataset.reset_index(drop=True)

    non_outliers = dataset[~dataset[outlier_col]]
    outliers = dataset[dataset[outlier_col]]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=non_outliers.index, y=non_outliers[col], mode='markers', marker=dict(color='blue'), name=f"No Outlier {col}"))
    fig.add_trace(go.Scatter(x=outliers.index, y=outliers[col], mode='markers', marker=dict(color='red'), name=f"Outlier {col}"))

    fig.update_layout(
        xaxis_title="Samples",
        yaxis_title="Value",
        legend=dict(
            x=0.5,
            y=1.15,
            orientation="h",
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        )
    )

    st.plotly_chart(fig)
    
    
    

## Function to marking outliers using IQR

def mark_outliers_percentile(dataset, col, lower_percentile=5, upper_percentile=95):
    dataset = dataset.copy()
    lower_bound = dataset[col].quantile(lower_percentile / 100)
    upper_bound = dataset[col].quantile(upper_percentile / 100)
    dataset[col + "_outlier"] = (dataset[col] < lower_bound) | (dataset[col] > upper_bound)
    return dataset


new_df = mark_outliers_percentile(dataset = df, col = 'mean_xc')

viz_1 = st.container()
with viz_1:
    st.subheader(" 🔭 Detecting Outliers wz (IQR): ")
    st.write("--------------------------------------------------")
    with st.expander(" >> Pandas Boxplot "):
        # Create a line plot for the 'mean_xc' column using Plotly
        col1 , col2 = st.columns(2)
        with col1:
            st.write(
    """
    **A box plot** is a method for graphically depicting groups of numerical data through their quartiles. 
    The box extends from the Q1 to Q3 quartile values of the data, with a line at the median (Q2). 
    The whiskers extend from the edges of box to show the range of the data. By default,
    they extend no more than 1.5 * IQR (IQR = Q3 - Q1) from the edges of the box, ending at the farthest data point within that interval. 
    Outliers are plotted as separate dots.
    
    """
    )
        with col2:
            st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/IQR.png")
    st.write("--------------------------------------------------")
outlier_df_col = ['mean_xc', 'mean_yc', 'mean_zc', 'mean_xg', 'mean_yg', 'mean_zg']
acc_df = df[outlier_df_col[:3] + ['posture']]
gyr_df = df[outlier_df_col[3:] + ['posture']]


viz_2 = st.container()
with viz_2:
    st.subheader("-  Accelerometer Sensors Axis and Gyroscope Sensors Axis  : ")
    st.write("--------------------------------------------------")
    with st.expander(" >> Accelerometer and Gyroscope Sensors with X - Y - Z [axis] with all Posture: "):
        
        col1 , col2 = st.columns(2)
        with col1:
            grouped_df = acc_df.groupby('posture')

            # Create subplots
            fig = make_subplots(rows=1, cols=3, subplot_titles=['mean_xc', 'mean_yc', 'mean_zc'])

            # Iterate over each column and add box trace to the subplot
            for i, col in enumerate(['mean_xc', 'mean_yc', 'mean_zc'], start=1):
                # Iterate over each group
                for group_name, group_data in grouped_df:
                    # Add box trace for the current group and column to the subplot
                    fig.add_trace(go.Box(y=group_data[col], name=group_name ,showlegend=False), row=1, col=i)

            # Update layout for better readability
            fig.update_layout(
                title='Box Plot Grouped by Posture',
                xaxis_title='Posture',
                yaxis_title='Values',
                template='plotly_dark',
            )

        st.plotly_chart(fig)
        with col2:
            grouped_df = gyr_df.groupby('posture')
            fig = make_subplots(rows=1, cols=3, subplot_titles=['mean_xg', 'mean_yg', 'mean_zg'])

            # Iterate over each column and add box trace to the subplot
            for i, col in enumerate(['mean_xg', 'mean_yg', 'mean_zg'], start=1):
                # Iterate over each group
                for group_name, group_data in grouped_df:
                    # Add box trace for the current group and column to the subplot
                    fig.add_trace(go.Box(y=group_data[col], name=group_name, showlegend=False), row=1, col=i)

            # Update layout for better readability
            fig.update_layout(
                title='Box Plot Grouped by Posture',
                xaxis_title='Posture',
                yaxis_title='Values',
                template='plotly_dark',
            )
        st.plotly_chart(fig)
                 
    st.write("--------------------------------------------------")


viz_3 = st.container()
with viz_3:
    with st.expander(" >> Accelerometer and Gyroscope Sensors with X - Y - Z [axis] with all Time and samples : "):
        
        col1 , col2 = st.columns(2)
        with col1:
            col = 'mean_xc'
            plot_binary_outliers_plotly(dataset=new_df, col=col, outlier_col=col+"_outlier", reset_index=False)
            
        with col2:
            plot_binary_outliers_plotly(dataset=new_df, col=col, outlier_col=col+"_outlier", reset_index=True)
                 
    st.write("--------------------------------------------------")


st.title('Insights')
st.write("--------------------------------------------------")
st.write('''
         
        - Outliers, represented by red dots in the data, are extreme values that deviate significantly from the central tendency of the data distribution.
        - Notably, there appear to be fewer outliers in the accelerometer data compared to the gyroscope data.
        - This observation that the gyroscope data exhibits greater variability.
    
    ''')

st.write("--------------------------------------------------")
    
st.write('''
        - We emphasize the importance of understanding and visualizing outliers to gain insights into the data.
        - However, we express concern about the potential loss of valuable information in the current approach, 
            
            which does not differentiate between different exercises or labels. 
            
        - To address this limitation, we plan to implement a loop to identify outliers in all outlier columns and plot them for visualization.
        ''')

st.write("--------------------------------------------------")
st.write('''
        - The current approach may result in the loss of valuable data, as it does not differentiate between different exercises or postures
        - we solve it by starting with using IQR to deal with outliers with lower bound  = 5 and upper bound = 95
        - Also don't drop outlier values, so we try to solve it by think if the value is outlier so make it as nan i will deal with it with IQR later
        - we done with using IQR and we don't loss any valuable data
            
        ''')