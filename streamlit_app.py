import streamlit as st
import pandas as pd
import requests

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import geopandas as gpd
import folium


brute = pd.read_csv('https://raw.githubusercontent.com/OliverGam/first_streamlit_app/main/Aire_production_AOP.csv',sep=';',encoding='latin-1')
data_brute = brute[['Département','Aire géographique','CI']]

fromages_liste = pd.read_csv('https://raw.githubusercontent.com/OliverGam/first_streamlit_app/main/Streamlit_fromage.csv')

for a,b in data_brute.iterrows():
    for c,d in fromages_liste.iterrows():
        if fuzz.partial_ratio(b['Aire géographique'],d['NOM_FROMAGE'])>85:
                      data_brute.loc[a,'NOM_DU_FROMAGE'] = fromages_liste.loc[c,'NOM_FROMAGE']
