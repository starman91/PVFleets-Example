import pandas as pd
import streamlit as st
from st_aggrid  import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode
from button_functions import download_button
import plotly.graph_objects as go
from PIL import Image

###########################################################################
class CreateSidebar():
    
    #------------------------------------------------------------------------------------------------------
    def __init__(self):
        return
    
    #------------------------------------------------------------------------------------------------------
    def build(self):
        #Display banner
        dmt_image=Image.open('C:/Projects/TestCode/streamlit/PVFleets-Example/images/PV_Fleets_400.png')
        st.sidebar.image(dmt_image)
    
        menu = ["Home","About"]
        choice = st.sidebar.selectbox("Menu",menu)
        return choice
        
        