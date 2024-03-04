#import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import plotly.graph_objects as go 
import pickle
import urllib.request

# Set page configuration and title
st.set_page_config(
    page_title='📉 Analysis Data Stage',
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
page_title = st.title("📈 Data Analysis")
st.write("--------------------------------------------------")
st.image("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/Deploy/intro2.jpg")
st.write("--------------------------------------------------")
st.write("In this stage we will explore the data more by vizualizing it")
df = pd.read_pickle("/Users/0xnrous/Developer/Epslilon_Projects/e2e_ds_final_StayFit/e2e_ds_StayFit/data/interim/1_df_resampled_datetime.pkl")
df_set = df[df['set']== 1]


viz_1 = st.container()
with viz_1:
    st.subheader(" 📊  Visualization of Basic Barbell Exercises ")
    st.write("--------------------------------------------------")
    # use an expander for the first question for Top videos 
    with st.expander(" >> [Vizualization of Mean XC for Set 1 (Squat)] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        col1 , col2 = st.columns(2)
        with col1:
            fig = go.Figure()
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=df_set.index,
                y=df_set['mean_xc'],
                mode='lines',
                name='Mean XC'
            ))

            # Update layout for better readability
            fig.update_layout(
                title='Mean XC Plot',
                xaxis_title='Time',
                yaxis_title='Mean XC',
                template='plotly_dark' 
            )

            # Show the plot
            st.plotly_chart(fig)
        with col2:        
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                y=df_set['mean_yc'].reset_index(drop=True),
                mode='lines',
                name='Mean YC'
            ))

            # Update layout for better readability
            fig.update_layout(
                title='Mean YC Plot',
                xaxis_title='Index',
                yaxis_title='Mean YC',
                template='plotly_dark'  
            )

            # Show the plot
            st.plotly_chart(fig)
        st.write("--------------------------------------------------")
        st.write("From this plot we can see that the mean of YC is working with the mean of XC for **Squat** game that make sense because the mean of YC is the mean of the vertical height of the barbell while XC is the mean of the horizontal distance between the barbell and the ground. ")
        
# ### Exploring all Exarcise using Graphs :
df_posture_unique = df['posture'].unique()
for pos in df_posture_unique:
    df_posture_subset = df[df['posture'] == pos]




viz_2 = st.container()
with viz_2:
    st.subheader(" 📈 Exploring all every unique Exarcise using Graphs  ")
    st.write("--------------------------------------------------")
    st.caption("- Based on posture column we will explore it first ")
    # use an expander for the first question for Top videos 
    with st.expander(" >> [Vizualization of {Mean YC} Up and Down movement for all basic Exercise (Squat - Bench Press - Overhead - Deadlift - Row)] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        # Iterate over each unique posture
        for pos in df_posture_unique:
            df_posture_subset = df[df['posture'] == pos]
            # Create a new figure for each posture
            fig = go.Figure()
            # Add trace for the current posture
            fig.add_trace(go.Scatter(
                y=df_posture_subset['mean_yc'][:200].reset_index(drop=True),
                mode='lines',
                name=pos
            ))
            # Update layout for better readability
            fig.update_layout(
                title=f'Mean YC Plot for {pos} Posture',
                xaxis_title='Index',
                yaxis_title='Mean YC',
                template='plotly_dark'  
            )
            # Show the plot for the current posture
            st.plotly_chart(fig)
        st.write("--------------------------------------------------")
        st.write("Based on these plots, it's evident that the mean of YC effectively captures the vertical movement associated with various postures. This observation aligns with expectations, as YC represents the vertical height of the barbell during its upward and downward motion. Conversely, the graph depicting resting periods indicates minimal vertical movement, consistent with real-world scenarios where the barbell remains static. ")
        
# ### comparsion between Squats and A Specimen with different Types of Posture
df_posture= df.loc[(df['posture'] == 'squat') & (df['specimen '] == 'A')].reset_index()
viz_3 = st.container()
with viz_3:
    st.subheader(" 📉 comparsion between Squats and A Specimen with different Types of Posture  ")
    st.write("--------------------------------------------------")
    st.caption("- Based on posture = 'squat'  and specimen = 'A' ")
    # use an expander for the first question for Top videos 
    with st.expander(" >> [Vizualization of {Mean YC} Up and Down movement for  Types [heavy - meduim] for posture squat - A ] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        col1 , col2 = st.columns(2)
        with col1:
            fig = go.Figure()
            # Iterate over each unique posture
            for posture, data in df_posture.groupby('types'):
                fig.add_trace(go.Scatter(
                    x=data.index,
                    y=data['mean_yc'],
                    mode='lines',
                    name=posture
                ))

            fig.update_layout(
                title='Mean YC Plot for Different Postures [Squat - A]',
                xaxis=dict(title='Index'),
                yaxis=dict(title='Mean YC'),
                template='plotly_dark'
            )
            st.plotly_chart(fig)
        with col2 :
            fig = go.Figure()
            for posture, data in df_posture.groupby('types'):
                fig.add_trace(go.Scatter(
                    x=data.index,
                    y=data['mean_zc'],
                    mode='lines',
                    name=posture
                ))

            fig.update_layout(
                title='Mean ZC Plot for Different Postures',
                xaxis=dict(title='Index'),
                yaxis=dict(title='Mean ZC'),
                template='plotly_dark'
            )
            st.plotly_chart(fig)    
        st.write("--------------------------------------------------")
        st.write("- Based on these plots, it's evident that the mean of YC  and ZC effectively captures the vertical movement associated with Squat postures. This observation aligns with expectations, as YC represents the vertical height of the barbell during its upward and downward motion , as ZC represent the movement of Front and back motion. ")
        st.write("- the plot show that when sqaut - A with type meduim as barbell the person is doing higher and YC , ZC also  is increasing.")
        st.write("- the plot show that when sqaut - A with type heavy as barbell the person is doing less and YC , ZC is decreasing.")
        
# ### Comparing All specimen Sets 
df_specimen_posture = df.loc[(df['posture'] == 'bench')].sort_values('specimen ').reset_index()
# - To see the difference between A , B , C , D and E Specimens


viz_4 = st.container()
with viz_4:
    st.subheader(" 📈 Comparing All specimen Sets ")
    st.write("--------------------------------------------------")
    st.caption("- To see the difference between A , B , C , D and E Specimens for bench postures ")
    # use an expander for the first question for Top videos 
    with st.expander(" >> [Vizualization of {Mean YC} Up and Down movement for all specimens A , B , C , D and E  "):
        # Create a line plot for the 'mean_xc' column using Plotly
        col1 , col2 = st.columns(2)
        with col1:
            fig = go.Figure()
            for specimen, data in df_specimen_posture.groupby('specimen '):
                fig.add_trace(go.Scatter(x=data.index, y=data['mean_yc'], mode='lines', name=specimen))

            fig.update_layout(title='Mean YC for Different Specimens',
                            xaxis_title='Index',
                            yaxis_title='Mean YC',
                            template='plotly_dark')
                # Show the plot for the current posture
            st.plotly_chart(fig)
        with col2 :
            st.write("--------------------------------------------------")
            st.write(" - From the above plots, we can see that the mean YC for each specimen is not significantly different. ")
            st.write("--------------------------------------------------")
            st.write("- In reviewing these plots, we observe the mean YC for each specimen. They appear somewhat similar, with slight variations.")
            st.write("--------------------------------------------------")
            st.write("- Specimen E notably exhibits higher values, indicating more frequent engagement in the bench press posture. This could suggest a larger chest or a preference for this particular exercise.")
            st.write("--------------------------------------------------")
            st.write("- Conversely, specimen B shows lower mean YC values, suggesting less involvement in the bench press posture. This could imply a smaller chest or a beginner level of engagement in weightlifting.")
        st.write("--------------------------------------------------")        
        
        
### Ploting X , Y , Z Axis for all posture and Specimen
# - `First when specimen is A and Posture is Squat`

viz_5 = st.container()
with viz_5:
    st.subheader(" 🏋🏾 Ploting X , Y , Z Axis for all posture and Specimen - A ")
    st.write("--------------------------------------------------")
    st.caption("- First when specimen is A and Posture is Squat ")
    posture = 'squat'
    specimen = 'A'
    xyz_axis = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)
    # use an expander for the first question for Top videos 
    with st.expander(f" >> [Vizualization of all axis acceleration for {posture} - {specimen} ] "):
    # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        for column in ['mean_xc', 'mean_yc', 'mean_zc']:
            fig.add_trace(go.Scatter(x=xyz_axis.index, y=xyz_axis[column], mode='lines', name=column))

        fig.update_layout(title='Mean Accelerometer Values',
                        xaxis_title='Index',
                        yaxis_title='Mean Value',
                        template='plotly_dark')
            # Show the plot for the current posture
        st.plotly_chart(fig)
        st.write("--------------------------------------------------")
        st.write(" - From the above plots, we can see that the mean YC  and ZC for each specimen is working well for squat ")
        st.write("--------------------------------------------------")
        st.write("- In reviewing these plots, we observe the mean YC and ZC for specimen A. They appear somewhat similar, with slight variations.")
        st.write("--------------------------------------------------")
        st.write("- So YC and ZC notably exhibits higher values, indicating more frequent engagement in the Squat posture. This make sense because in squat in real we uping and downing as motion also we move front and back ")
        st.write("--------------------------------------------------")
        st.write("- Conversely, Squat shows lower mean XC values, suggesting less involvement in the squats posture. Also this make sense in squat we don't move left and right in weightlifting.")
    st.write("--------------------------------------------------") 
        
    posture = 'bench'
    specimen = 'A'
    xyz_axis = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)
    st.caption("- Second when specimen is A and Posture is Bench Press ")
    with st.expander(f" >> [Vizualization of all axis acceleration for {posture} - {specimen} ] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        for column in ['mean_xc', 'mean_yc', 'mean_zc']:
            fig.add_trace(go.Scatter(x=xyz_axis.index, y=xyz_axis[column], mode='lines', name=column))

        fig.update_layout(title='Mean Accelerometer Values',
                        xaxis_title='Index',
                        yaxis_title='Mean Value',
                        template='plotly_dark')
            # Show the plot for the current posture
        st.plotly_chart(fig)
        st.write(" - From the above plot, we can see that the mean YC for each specimen is working well for Bench ")
        st.write("--------------------------------------------------")
        st.write("- So YC notably exhibits higher values, indicating more frequent engagement in the bench posture. This make sense because in bench press in real we uping and downing as motion")
        st.write("--------------------------------------------------")
        st.write("- Conversely, Bench press shows lower mean XC  and ZC values, suggesting less involvement in the Bech Press posture. Also this make sense in Bech Press we don't move left and right also front and back in weightlifting.")
    st.write("--------------------------------------------------")     
    
    
    # ohp
    posture = 'ohp'
    specimen = 'A'
    xyz_axis = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)
    st.caption("- Third when specimen is A and Posture is Overhead Press ")
    with st.expander(f" >> [Vizualization of all axis acceleration for {posture} - {specimen} ] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        for column in ['mean_xc', 'mean_yc', 'mean_zc']:
            fig.add_trace(go.Scatter(x=xyz_axis.index, y=xyz_axis[column], mode='lines', name=column))

        fig.update_layout(title='Mean Accelerometer Values',
                        xaxis_title='Index',
                        yaxis_title='Mean Value',
                        template='plotly_dark')
            # Show the plot for the current posture
        st.plotly_chart(fig)
        st.write(" - From the above plot, we can see that the mean YC for each specimen is working well for Overhead Press ")
        st.write("--------------------------------------------------")
        st.write("- So YC notably exhibits higher values, indicating more frequent engagement in the bench posture. This make sense because in bench press in real we uping and downing as motion")
        st.write("--------------------------------------------------")
        st.write("- Conversely, Overhead Press shows lower mean XC  and ZC values, suggesting less involvement in the Bech Overhead Press. Also this make sense in Overhead Press we don't move left and right also front and back in weightlifting.")
        st.write("--------------------------------------------------")
        st.write("-  **Overhead Press and Bech Press is most similatr exercises** (Graphs tells us)")
    st.write("--------------------------------------------------")     


    # dead
    posture = 'dead'
    specimen = 'A'
    xyz_axis = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)

    st.caption("- Fourth when specimen is A and Posture is Deadlift ")
    with st.expander(f" >> [Vizualization of all axis acceleration for {posture} - {specimen} ] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        for column in ['mean_xc', 'mean_yc', 'mean_zc']:
            fig.add_trace(go.Scatter(x=xyz_axis.index, y=xyz_axis[column], mode='lines', name=column))

        fig.update_layout(title='Mean Accelerometer Values',
                        xaxis_title='Index',
                        yaxis_title='Mean Value',
                        template='plotly_dark')
            # Show the plot for the current posture
        st.plotly_chart(fig)
        st.write(" - From the above plot, we can see that the mean YC for A specimen is working well for Deadlift ")
        st.write("- here we can see also that the mean ZC working in good way when we see the deadlift posture structure in real life it's make sense ")
    st.write("--------------------------------------------------")    
    # row
    posture = 'row'
    specimen = 'A'
    xyz_axis = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)

    st.caption("- Fifth when specimen is A and Posture is row ")
    with st.expander(f" >> [Vizualization of all axis acceleration for {posture} - {specimen} ] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        for column in ['mean_xc', 'mean_yc', 'mean_zc']:
            fig.add_trace(go.Scatter(x=xyz_axis.index, y=xyz_axis[column], mode='lines', name=column))

        fig.update_layout(title='Mean Accelerometer Values',
                        xaxis_title='Index',
                        yaxis_title='Mean Value',
                        template='plotly_dark')
            # Show the plot for the current posture
        st.plotly_chart(fig)
        st.write(" - From the above plot, we can see that the mean YC for A specimen is working well for row , it's make sense in real life ")
    st.write("--------------------------------------------------")    
    # rest
    posture = 'rest'
    specimen = 'A'
    xyz_axis = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)

    st.caption("- Fifth when specimen is A and Posture is row ")
    with st.expander(f" >> [Vizualization of all axis acceleration for {posture} - {specimen} ] "):
        # Create a line plot for the 'mean_xc' column using Plotly
        fig = go.Figure()
        for column in ['mean_xc', 'mean_yc', 'mean_zc']:
            fig.add_trace(go.Scatter(x=xyz_axis.index, y=xyz_axis[column], mode='lines', name=column))

        fig.update_layout(title='Mean Accelerometer Values',
                        xaxis_title='Index',
                        yaxis_title='Mean Value',
                        template='plotly_dark')
            # Show the plot for the current posture
        st.plotly_chart(fig)
        st.write(" - From the above plot, it's tell us that when posture is rest , the Accelerometer values are not specify any insight ")
    st.write("--------------------------------------------------")    



viz_6 = st.container()
with viz_6:
    st.subheader(" 📈 Combine plots in one figure [Accelerometer - Gyroscope] sensors ")
    st.write("--------------------------------------------------")
    st.caption("- To see all sensors plots ")
    # use an expander for the first question for Top videos 
    with st.expander(" >> [Vizualization with Loop over all combinations per sensors"):
        # Create a line plot for the 'mean_xc' column using Plotly
        col1 , col2 = st.columns(2)
        with col1:
            posture = 'ohp'
            specimen = 'A'
            df_combined_xyz = df[(df['posture'] == posture) & (df['specimen '] == specimen)].reset_index(drop=True)

            fig = go.Figure()

            # Adding traces for accelerometer data (xc, yc, zc)
            fig.add_trace(go.Scatter(x=df_combined_xyz.index, y=df_combined_xyz['mean_xc'], mode='lines', name='Mean XC'))
            fig.add_trace(go.Scatter(x=df_combined_xyz.index, y=df_combined_xyz['mean_yc'], mode='lines', name='Mean YC'))
            fig.add_trace(go.Scatter(x=df_combined_xyz.index, y=df_combined_xyz['mean_zc'], mode='lines', name='Mean ZC'))

            # Update layout for accelerometer plot
            fig.update_layout(title=f"Accelerometer - {posture} ({specimen})",
                            xaxis_title='Index',
                            yaxis_title='Mean Value',
                            template='plotly_dark',
                            legend=dict(x=0.5, y=1.15, orientation='h', bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'))

            st.plotly_chart(fig)
        with col2 :
                        # Creating a separate figure for gyroscope data (xg, yg, zg)
            fig_gyro = go.Figure()

            # Adding traces for gyroscope data (xg, yg, zg)
            fig_gyro.add_trace(go.Scatter(x=df_combined_xyz.index, y=df_combined_xyz['mean_xg'], mode='lines', name='Mean XG'))
            fig_gyro.add_trace(go.Scatter(x=df_combined_xyz.index, y=df_combined_xyz['mean_yg'], mode='lines', name='Mean YG'))
            fig_gyro.add_trace(go.Scatter(x=df_combined_xyz.index, y=df_combined_xyz['mean_zg'], mode='lines', name='Mean ZG'))

            # Update layout for gyroscope plot
            fig_gyro.update_layout(title=f"Gyroscope - {posture} ({specimen})",
                                    xaxis_title='Index',
                                    yaxis_title='Mean Value',
                                    template='plotly_dark',
                                    legend=dict(x=0.5, y=1.15, orientation='h', bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'))
                # Show the plot for the current posture
            st.plotly_chart(fig_gyro)
        st.write("--------------------------------------------------")        
      
 # Insights 
# Header
st.title("**Weightlifting Exercise Analysis**")

# Squat Exercise Analysis
st.subheader("- Squat Exercise Analysis")
st.write(
    """
    - The combination of mean YC and ZC effectively captures the vertical and front-back movement associated with Squat postures.
    - Observing Squat - A with medium barbell types, we note that higher YC and ZC values correspond to increased engagement in the squat posture, which aligns with the expected motion during squats.
    - Conversely, lower YC and ZC values for Squat - A with heavy barbell type indicate reduced involvement in the squat posture, which is consistent with lighter lifting or fewer repetitions.
    """
)

# Bench Press Exercise Analysis
st.subheader("- Bench Press Exercise Analysis")
st.write(
    """
    - Mean YC shows significant variation among specimens, suggesting differing levels of engagement in the bench press posture.
    - Specimen E exhibits higher mean YC values, indicating more frequent involvement in bench press exercises, possibly due to a preference for this activity or a larger chest size.
    - Conversely, Specimen B displays lower mean YC values, suggesting less engagement in bench press exercises, which could indicate a beginner level or lesser interest in chest exercises.
    """
)

# Overhead Press Exercise Analysis
st.subheader("- Overhead Press Exercise Analysis")
st.write(
    """
    - Mean YC demonstrates a noticeable difference among specimens, indicating varied levels of participation in overhead press exercises.
    - Higher mean YC values suggest increased involvement in overhead press activities, reflecting the upward and downward motion characteristic of this exercise.
    - Lower mean YC values for overhead press exercises suggest lesser engagement, possibly due to different preferences or focus on other types of weightlifting exercises.
    """
)

# Row Exercise Analysis
st.subheader("- Row Exercise Analysis")
st.write(
    """
    - From the above plot, we can see that the mean YC for specimen A is working well for the row exercise.
    - This observation aligns with expectations based on real-life rowing movements.
    - The plot indicates that the mean YC effectively captures the vertical movement associated with rowing exercises.
    - This suggests that specimen A is effectively performing the row exercise, as reflected by the consistent and appropriate vertical motion.
    """
)

# Rest Analysis
st.subheader("- Rest Analysis")
st.write(
    """
    - In resting periods, there is minimal movement, resulting in consistent and low accelerometer values.
    """
)

# Deadlift Exercise Analysis
st.subheader("- Deadlift Exercise Analysis")
st.write(
    """
    - The plot illustrates that the mean YC for specimen A effectively captures the vertical movement associated with the Deadlift posture.
    - Additionally, the mean ZC also exhibits notable variations, which align with the expected movement patterns during Deadlift exercises.
    - This observation is consistent with real-life Deadlift movements, where both vertical and forward/backward motions are prominent.
    """
)      
    