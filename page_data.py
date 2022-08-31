import pandas as pd
import streamlit as st
from st_aggrid  import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode
from button_functions import download_button

#Viz Libs
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt

###########################################################################
class PageData():
    #---------------------------------------------------------------------------
    def __init__(self):
        return
    
    #---------------------------------------------------------------------------
    def create_page(self, df_pvf):      
        gb = GridOptionsBuilder.from_dataframe(df_pvf)
        # enables pivoting on all columns, change ag grid to allow export of pivoted/grouped data, however it select/filters groups
        gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
        gb.configure_selection(selection_mode="multiple", use_checkbox=True)
        gb.configure_side_bar() 
        gridOptions = gb.build()
        
        response = AgGrid(
                df_pvf,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
            fit_columns_on_grid_load=False,
        )
        st.text("")
        
        
        df = pd.DataFrame(response["selected_rows"])
        
        if df.empty:
            st.write('empty')
            #Use all sites from csv
            df_tech = df_pvf.groupby(['technology1'])['technology1'].count()
            df_sub_tech = df_pvf.groupby(['technology2'])['technology2'].count()
            df_sensor=df_pvf[df_pvf['plr_type']=='sensor']
            df_clearsky=df_pvf[df_pvf['plr_type']=='clearsky']
            df_nsrdb=df_pvf[df_pvf['plr_type']=='nsrdb']
            selection = 'all'
        else:
            st.write('selection')
            df_tech = df.groupby(['technology1'])['technology1'].count()
            df_sub_tech = df.groupby(['technology2'])['technology2'].count()
            df_sensor=df[df_pvf['plr_type']=='sensor']
            df_clearsky=df[df_pvf['plr_type']=='clearsky']
            df_nsrdb=df[df_pvf['plr_type']=='nsrdb']
            selection = 'data subset of '
            
            
        dist_tab, tech_tab, map_tab = st .tabs(['Performance Distribution', 'Module Technologies', 'Geo Location'])   
                            
        #Distribution plot
        with dist_tab:
            # Add histogram data
            sensor = df_sensor['plr_median'].tolist() #np.random.randn(200) - 2
            cs = df_clearsky['plr_median'].tolist() #np.random.randn(200)
            nsrdb = df_nsrdb['plr_median'].tolist() #np.random.randn(200) + 2
            
            # Group data together
            hist_data = [sensor, cs, nsrdb]
            
            group_labels = ['Sensor', 'Clear Sky', 'NSRDB']
            
            # Plot!
            bin_width= 0.2
            nbins = round((max(sensor) - min(sensor)) / bin_width)            
            fig = px.histogram(sensor, histnorm='density', title='Sensor based performance          median=' + str(np.median(sensor)), width=1200, height=600, opacity=0.60, nbins=nbins, marginal="box",)
           #fig = ff.create_distplot( hist_data, group_labels, bin_size=[.2, .2, .2]) 
            st.plotly_chart(fig, use_container_width=True)
            st.write ('Median =' + str(np.median(sensor)))


        #Tech type pie charts
        with tech_tab:
            #Pie chart of technologies, Plotly
            fig1 = go.Figure(
                    data=[go.Pie(
                            labels = df_tech.index.values.tolist(),
                            values = df_tech.tolist()
                        )]
                )
            fig1 = fig1.update_traces(
                    hoverinfo='label+percent',
                        textinfo='value',
                        textfont_size=15
                )
            fig2 = go.Figure(
                    data=[go.Pie(
                            labels = df_sub_tech.index.values.tolist(),
                            values = df_sub_tech.tolist()
                        )]
                )
            fig2 = fig2.update_traces(
                    hoverinfo='label+percent',
                        textinfo='value',
                        textfont_size=15
                )
            #Display plot       
            st.subheader ("Module Technology types:")
            st.write("From " + selection +  " sites")
            st.plotly_chart(fig1)
         
            st.subheader ("Module Technology Sub types:")
            st.write("From " + selection +  " sites")
            st.plotly_chart(fig2)
 
        with map_tab:
            st.write ('Site map here')
 
 
        #Out of container and columns
        st.subheader("Filtered data will appear below 👇 ") #Adds subheader with finger pointing down emoji graphic 
        st.text("")        # space
        st.table(df)    # table of data frame
        st.text("")        # space
        
        #Buttons for Downloading
        c29, c30, c31 = st.columns([1, 1, 2])
        with c29:
                CSVButton = download_button(
                    df,
                "File.csv",
                "Download to CSV",
            )
        with c30:
                CSVButton = download_button(
                    df,
                "File.csv",
                "Download to TXT",
            )                       
                
        return