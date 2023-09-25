import streamlit
import pandas
import requests

dat = pandas.DataFrame({'LAT':[46.05],'LON':[5.20]});

streamlit.map(dat)
