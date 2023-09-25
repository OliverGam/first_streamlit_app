import streamlit
import pandas
import requests

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import geopandas as gpd
import folium


brute = pd.read_csv('Aire_production_AOP.csv',sep=';', encoding='latin-1')
