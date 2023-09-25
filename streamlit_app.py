import streamlit as st
import pandas as pd
import requests

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import geopandas as gpd
import folium


brute = pd.read_csv('https://github.com/OliverGam/first_streamlit_app/blob/main/Aire_production_AOP.csv')
