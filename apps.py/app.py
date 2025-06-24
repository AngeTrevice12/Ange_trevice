import streamlit as st
import pandas as pd

# Let's read VIIRS csv sample data set into a DataFrame df GOES-R,VIIRS_NOAA21_NRT,VIIRS_S_NPP,Météosat
st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
   initial_sidebar_state="expanded")

st.title(" Visualisation des incendies actifs en temps réel✅🔥🌳")

MAP_KEY= "4ec1e3c89060b2d307d5763358818604"
civ_url  = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/'  +  MAP_KEY  +  '/VIIRS_NOAA21_NRT/CIV/4'
civ_url1  = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/'  +  MAP_KEY  +  '/VIIRS_NOAA20_NRT/CIV/4'
civ_url2  = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/'  +  MAP_KEY  +  '/VIIRS_S_NPP/CIV/4'

df_civ  = pd.read_csv(civ_url)
df_civ1  = pd.read_csv(civ_url1)
df_civ2  = pd.read_csv(civ_url2)

df_civ= pd.concat([df_civ,df_civ1,df_civ2 ])

dt_filter = st.selectbox("Select one date", pd.unique(df_civ["acq_date"]))
dff = df_civ[df_civ["acq_date"]== dt_filter]
st.map(dff)

st.dataframe(dff)






