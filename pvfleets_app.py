import numpy as np
import pandas as pd
import streamlit as st
from st_aggrid  import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode
import plotly.graph_objects as go
import os
from PIL import Image
from button_functions import download_button
import page_data
import create_sidebar

#------------------------------------------------------------------------------------------------------
def getData(target_file):
        df = pd.read_csv(target_file)
        return df

#------------------------------------------------------------------------------------------------------
def build_sidebar():
        #Display banner
        dmt_image=Image.open('C:/Projects/TestCode/streamlit/PVFleets-Example/images/PV_Fleets_400.png')
        st.sidebar.image(dmt_image)
        
        menu = ["Home","About"]
        choice = st.sidebar.selectbox("Menu",menu)
        return choice


#------------------------------------------------------------------------------------------------------
def main():
        print ('..: Starting PV Fleets Streamlit app - Local edition')
        dp = page_data.PageData()
        sb = create_sidebar.CreateSidebar()

        #title
        st.title("PV Fleets Public Data Explorer App")
        
        #Side bar
        choice = sb.build()

        if choice == "Home":
                #Data page layout
                st.subheader("PV Fleets Data Results")
                #get data
                df_pvf = getData('C:/PV_Fleets/analysis/PVFleetDataInitiative/Results/fleet_results_public.csv')
                dp.create_page(df_pvf)
        else:
                #Aboout page layout
                st.subheader("About")



########################
##  ENTRY
########################
if __name__ == '__main__':
  
        #df_pvf = getData('C:/PV_Fleets/analysis/PVFleetDataInitiative/Results/fleet_results_public.csv')
        #df_sensor=df_pvf[df_pvf['plr_type']=='sensor']
        #sensor_data = df_sensor['plr_median'].tolist()
  
        main()
