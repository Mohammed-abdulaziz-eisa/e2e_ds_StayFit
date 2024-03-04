import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import pickle
import urllib.request
import sys
from pathlib import Path
import sys
from scipy.signal import butter, filtfilt, lfilter
import numpy as np
from sklearn.decomposition import PCA
sys.path.append(str(Path('../scripts').resolve().parent.parent))
from scripts.LowPassFilter import *
from scripts.PrincipalComponentAnalysis import *

colors = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 
          'rgb(148, 103, 189)', 'rgb(140, 86, 75)', 'rgb(227, 119, 194)', 'rgb(127, 127, 127)', 
          'rgb(188, 189, 34)', 'rgb(23, 190, 207)']
# Set page configuration and title
st.set_page_config(
    page_title='4- 📐 Feature Engineering Stage',
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
page_title = st.title("📐 Feature Engineering ")
st.write("-----------------------------------------------------------------")
# st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/feature.jpg")
# st.write("-----------------------------------------------------------------")
# st.write("In this stage we will explore and preprocess the data for further analysis.")
df = pd.read_pickle("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/data/processed/4_cleaned_outliers_data.pkl")


# subplot function 
## Plotting outliers wz time :



viz_0 = st.container()
with viz_0:
    st.subheader("Goal")
    #st.write("--------------------------------------------------")
    st.write('''
             First, we clean up the data by removing any subtle noise, which are small fluctuations that aren't outliers. 
             Then, we pinpoint the parts of the data that contribute the most to its overall patterns. 
             After that, we enhance the dataset by adding different types of features like numerical values, 
             time-related information, frequency details, and groupings based on similarity.
             This helps us better understand and analyze the data.    
             ''')
    st.write("--------------------------------------------------")
    
viz_1 = st.container()    
with viz_1:
    st.subheader("Topics to cover in this stage")
    with st.expander("What's Feature Engineering ?"):
        st.write('''
                    Feature engineering is the process of transforming raw data into meaningful features that can be used for machine learning. 
                    This involves selecting the most useful features from the raw data and using them to build or create new features that represent the information in the dataset in a more effective way.
                    These new, engineered features can make it easier for machine learning models to learn from the data and make more accurate predictions when done right.

                    Examples

                    • Alter existing data

                    • Use domain knowledge

                    • Numerical features

                    • Temporal features

                    • Frequency features

                    • Principle component analysis
        
                    ''')
    with st.expander("Butterworth filtering"):
        st.write("""
                 A Butterworth low-pass filter is a method employed to eliminate high-frequency noise from a dataset, particularly in machine learning tasks to enhance model accuracy. 
                 This filter effectively eradicates data points beyond a specified threshold frequency, while retaining the fundamental patterns within the data. 
                 Consequently, it diminishes the impact of noise, thereby improving model performance and yielding more reliable outcomes.
                 
                 """)
        st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/low-pass.jpg")
        st.caption('Source: Hoogendoorn, M., & Funk, B. (2018). Machine learning for the quantified self. On the art of learning from sensory data.')
    with st.expander("Principal Component Analysis | PCA"):
        st.write("""
                 Principal Component Analysis (PCA) is a statistical technique used to extract the most important features from a dataset. 
                 It aims to reduce the dimensionality of the data by projecting it onto a lower-dimensional subspace, known as the principal components. 
                 The first principal component captures the highest variance in the data, while the second principal component captures the second smallest variance.
                 This helps to reduce the complexity of the data and make it easier to analyze and make predictions from.
                 """)
        st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/pca.gif")
    with st.expander("Elbow Method"):
        st.write('''
                 
                 The elbow technique is a method used to determine the optimal number of components to use when conducting a PCA.
                 It works by testing multiple different component numbers and then evaluating the variance captured by each component number.
                 The optimal component number is then chosen as the number of components that capture the most variance while also not incorporating too many components.
                 This is done by plotting the variance captured against the component number and then selecting the point at which the rate of change in variance diminishes (the "elbow"),
                 as this is typically the point at which adding more components does not significantly improve the analysis.
                 ''')
        st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/elbow.png")
    with st.expander("Sum of Squares Method"):
        st.write('''
                    To further exploit the data, the scalar magnitudes r of the accelerometer and gyroscope were calculated. 
                    r is the scalar magnitude of the three combined data points: x, y, and z. 
                    The advantage of using r versus any particular data direction is that it is impartial to device orientation and can handle dynamic re-orientations. r is calculated by:
               
                **r = sqrt{x^2 + y^2 + z^2}**

                ''')
    with st.expander("Temporal abstraction"):
        st.write('''
                    A temporal abstraction is a technique used in machine learning to extract time-based features from a dataset.
                    Based on rolling mean in Pandas that helps to Create a rolling average allows you to “smooth” out small fluctuations in datasets, while gaining insight into trends. 
                    ''')
        st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/roll.jpg")
        
    
st.write("--------------------------------------------------")
viz_2 = st.container()
with viz_2:
    st.subheader(" Dealing with missing values")
    with st.expander(" >> Explore the missing values + interpolate "):
        # Create a line plot for the 'mean_xc' column using Plotly

            # Filter dataframe for set 1
        set_1_df = df[df['set'] == 1]

        # Create a scatter plot using Plotly
        fig = go.Figure(go.Scatter(x=set_1_df.index, y=set_1_df['mean_xg'], mode='lines'))

        # Update layout for better readability
        fig.update_layout(
            title='Mean XG Plot for Set 1',
            xaxis_title='Index',
            yaxis_title='Mean XG',
            template='plotly_dark' 
        )
        st.plotly_chart(fig)
        st.write('''
                    - Ok, as we can see there are gaps between graph that tell us there are something wrong aka (missing values)

                - There are serveral ways to deal with this gaps in the data for eaxmple we can drop it but it's not effective in this case

                - Imputing missing values is one of the best ways to deal with this gap like statistical imputation (mean - median - mode), 
                    but also this can interplate the data by trying to connect the points to fill the gaps 
                    **Interpolation Missing Values using pandas**
                    ''')
            
        st.subheader("Same graph after interpolation")
        # Filter dataframe for set 1
        predicator_columns = list(df.columns[0:6])
        for col in predicator_columns:
            df[col] = df[col].interpolate()
        set_1_df = df[df['set'] == 1]

        # Create a scatter plot using Plotly
        fig = go.Figure(go.Scatter(x=set_1_df.index, y=set_1_df['mean_xg'], mode='lines'))

        # Update layout for better readability
        fig.update_layout(
            title='Mean XG Plot for Set 1',
            xaxis_title='Index',
            yaxis_title='Mean XG',
            template='plotly_dark' 
        )

        # Show the plot
        st.plotly_chart(fig)
        st.write("- Now we can see that there are no gaps anymore ")
            
# Calculating set duration
viz_3 = st.container()
with viz_3:
    st.subheader(" Calculating set duration")
    with st.expander(" >> Average Duration Time by Types"):
        # Create a line plot for the 'mean_xc' column using Plotly

            # Filter dataframe for set 1
        unique_sets = df['set'].unique()
        # for calculating the average duration of each set
        for second in unique_sets:
            start_time = df[df.set == second].index[0]
            stop_time = df[df.set == second].index[-1]
            duration_time = stop_time - start_time
            df.loc[(df.set == second), 'duration_time'] = duration_time.seconds
        


        # Create a scatter plot using Plotly
        avg_duration_by_types = df.groupby('types')['duration_time'].mean()

        # Create a Pie chart using Plotly
        fig = go.Figure(go.Pie(
            labels=avg_duration_by_types.index,
            values=avg_duration_by_types,
            textinfo='percent',
            marker=dict(colors=colors)
        ))

        # Update layout for better readability and adjust the size of the circle
        fig.update_layout(
            title='Average Duration Time by Types',
            title_font=dict(size=20),
            legend=dict(x=1, y=0.5),
            template='plotly_dark',
        )

        st.plotly_chart(fig)
        st.write('''
                    - Ok, as we can see there are four types of activities  (Standing - sitting - meduim - heavy)
                    - standing have the highest average duration time
                    - heavy have the lowest average duration time
                    ''')
            
            
            
            
# Butterworth low-pass filter 
      
viz_4 = st.container()
with viz_4:
    st.subheader(" Butterworth : ")
    with st.expander(" >> Low-Pass Filter : "):
        df_butter = df.copy()
        PassFilter = LowPassFilter()
        fs = 1000 / 200  # sampling frequency
        cutoff = 1.27 # desired cutoff frequency of the filter, Hz
        df_butter = PassFilter.apply_low_pass_filter(df_butter, 'mean_xc', fs, cutoff)
        subset_df = df_butter[df_butter['set'] == 45]
        fig = go.Figure()

        # Plot raw data
        fig.add_trace(go.Scatter(x=subset_df.index, y=subset_df["mean_xc"], mode='lines', name="Raw Data", line=dict(color='blue')))

        # Plot low-pass filtered data
        fig.add_trace(go.Scatter(x=subset_df.index, y=subset_df["mean_xc_lowpass"], mode='lines', name="Butterworth", line=dict(color='orange')))

        # Update layout for better readability
        fig.update_layout(
            title="Raw Data vs Low-pass Filtered Data",
            xaxis_title="Index",
            yaxis_title="Value",
            template='plotly_dark',
            legend=dict(x=0.5, y=1.15, orientation='h', bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
            margin=dict(l=0, r=0, t=50, b=0),  # Adjust margin for title visibility
        )
        st.plotly_chart(fig)
        st.write("We remove high frequency noise from a dataset by applying a low-pass filter to all the data.")    
        st.write("That will improve the accuracy of the model. The filter works by removing any data points above a certain threshold frequency.")         
        
# Loop over all columns to apply low-pass filter
for col in predicator_columns:
    df_butter = PassFilter.apply_low_pass_filter(df_butter, col, fs, cutoff)
    # overwrite the original column with the low-pass filtered column
    df_butter[col] = df_butter[col + "_lowpass"]
    del df_butter[col + "_lowpass"]
    


# **Principal Component Analysis (PCA):**
# Elbow method
 
viz_5 = st.container()
with viz_5:
    st.subheader(" Principal Component Analysis : ")
    with st.expander(" >> Applying Elbow method : "):
        PCA = PrincipalComponentAnalysis()
        df_pca = df_butter.copy()
        pca_val = PCA.determine_pc_explained_variance(df_pca, predicator_columns)
        fig = go.Figure()
        # Plot PCA values
        fig.add_trace(go.Scatter(x=list(range(0, len(pca_val)+1)), y=pca_val, mode='lines'))
        # Update layout
        fig.update_layout(
            title="PCA Explained Variance",
            xaxis_title="PCA Component",
            yaxis_title="Explained Variance",
            template='plotly_dark'
            
)
        st.plotly_chart(fig)
        st.write("the graph shows that the optimal k  = 3 .")    
        st.write ("We will apply PCA to reduce the dimensionality of the data using K = 3 to normalize data and fit transform to predict new values .")
        
        
    with st.expander(" >> Applying PCA : "):
        df_pca = PCA.apply_pca(df_pca, predicator_columns, 3)
        subset_df = df_pca[df_pca['set'] == 35]
        fig = go.Figure()

        # Add traces for each PCA component
        for col in ['pca_1', 'pca_2', 'pca_3']:
            fig.add_trace(go.Scatter(x=subset_df.index, y=subset_df[col], mode='lines', name=col, line=dict(width=2)))

        # Update layout
        fig.update_layout(
            title="PCA Components",
            xaxis_title="Index",
            yaxis_title="PCA Component Value",
            template='plotly_dark',
            legend=dict(x=1, y=1)
        )
        st.plotly_chart(fig)
    with st.expander(" >> Applying Sum Of Square "):
        st.write("Equation : r = sqrt{x^2 + y^2 + z^2} ")
        df_equation  = df_pca.copy()
        acceleration_sqrt = df_equation['mean_xc'] ** 2 + df_equation['mean_yc'] ** 2 + df_equation['mean_zc'] ** 2
        gyro_sqrt = df_equation['mean_xg'] ** 2 + df_equation['mean_yg'] ** 2 + df_equation['mean_zg'] ** 2
        df_equation['acc_sqrt'] = np.sqrt(acceleration_sqrt)
        df_equation['gyro_sqrt'] = np.sqrt(gyro_sqrt)
        subset_df = df_equation[df_equation['set'] == 35]
        fig = go.Figure()

        # Add traces for accelerometer and gyroscope data
        fig.add_trace(go.Scatter(x=subset_df.index, y=subset_df['acc_sqrt'], mode='lines', name='Accelerometer', line=dict(width=2)))
        fig.add_trace(go.Scatter(x=subset_df.index, y=subset_df['gyro_sqrt'], mode='lines', name='Gyroscope', line=dict(width=2)))

        # Update layout
        fig.update_layout(
            title="Accelerometer and Gyroscope Data",
            xaxis_title="Index",
            yaxis_title="Sensor Data",
            template='plotly_dark',
            legend=dict(x=1, y=1)
        )
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray', zeroline=False)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray')
        st.plotly_chart(fig)
        st.write("We make this to make the data impartial to device orientation and handle dynamic reorientation.")
        st.write("The main goal of implementing a magnitude-scaled of all the values is to make the model generalize better to different Specimens.")
        




viz_6 = st.container()
with viz_6:
    st.subheader(" Discrete Fourier Transformation (DFT) : ")
    
    with st.expander(" >> Applying DFT method : "):
        st.write("""A DFT is beneficial for Machine Learning, as it can be used to represent data in terms of frequency components,
                 allowing for more efficient analysis of the data. This provides a way to better understand and model complex data sets, 
                 as the frequency components produced by the DFT can provide insight into patterns and trends that would not otherwise be visible.
                 Additionally, the DFT can be used to reduce noise, allowing for more accurate models..""")           
        df = pd.read_pickle("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/data/processed/5b_feature_engineering_clustered_data.pkl")
        st.subheader("Final Look of Data after Feature Engineering Process : ")
        st.dataframe(df.sample(15))


# viz_2 = st.container()
# with viz_2:
#     st.subheader("-  Accelerometer Sensors Axis and Gyroscope Sensors Axis  : ")
#     st.write("--------------------------------------------------")
#     with st.expander(" >> Accelerometer and Gyroscope Sensors with X - Y - Z [axis] with all Posture: "):
        
#         col1 , col2 = st.columns(2)
#         with col1:
#             grouped_df = acc_df.groupby('posture')
#             # Create subplots
#             fig = make_subplots(rows=1, cols=3, subplot_titles=['mean_xc', 'mean_yc', 'mean_zc'])

#             # Iterate over each column and add box trace to the subplot
#             for i, col in enumerate(['mean_xc', 'mean_yc', 'mean_zc'], start=1):
#                 # Iterate over each group
#                 for group_name, group_data in grouped_df:
#                     # Add box trace for the current group and column to the subplot
#                     fig.add_trace(go.Box(y=group_data[col], name=group_name ,showlegend=False), row=1, col=i)

#             # Update layout for better readability
#             fig.update_layout(
#                 title='Box Plot Grouped by Posture',
#                 xaxis_title='Posture',
#                 yaxis_title='Values',
#                 template='plotly_dark',
#             )

#         st.plotly_chart(fig)
#         with col2:
#             grouped_df = gyr_df.groupby('posture')
#             fig = make_subplots(rows=1, cols=3, subplot_titles=['mean_xg', 'mean_yg', 'mean_zg'])

#             # Iterate over each column and add box trace to the subplot
#             for i, col in enumerate(['mean_xg', 'mean_yg', 'mean_zg'], start=1):
#                 # Iterate over each group
#                 for group_name, group_data in grouped_df:
#                     # Add box trace for the current group and column to the subplot
#                     fig.add_trace(go.Box(y=group_data[col], name=group_name, showlegend=False), row=1, col=i)

#             # Update layout for better readability
#             fig.update_layout(
#                 title='Box Plot Grouped by Posture',
#                 xaxis_title='Posture',
#                 yaxis_title='Values',
#                 template='plotly_dark',
#             )
#         st.plotly_chart(fig)
                  
#     st.write("--------------------------------------------------")