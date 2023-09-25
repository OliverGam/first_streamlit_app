import streamlit
import pandas
import requests

dat = pandas.DataFrame({'LAT':[46.05],'LONG':[5.20]});

streamlit.map(dat)
