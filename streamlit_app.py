import streamlit as st
import pandas as pd
import requests

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import geopandas as gpd
import folium


brute = pd.read_csv('https://raw.githubusercontent.com/OliverGam/first_streamlit_app/main/Aire_production_AOP.csv',sep=';',encoding='latin-1')
data_brute = brute[['Département','Aire géographique','CI']]

fromages_liste = pd.read_csv('C:/Users/frup00090287/OneDrive - GFI/Bureau/Tuto snowflake/Fromages/Streamlit_fromage.csv')
