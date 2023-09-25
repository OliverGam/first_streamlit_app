import streamlit
import pandas
import requests

dat = pandas.DataFrame({'Lat':[46.05],'Long':[5.20]});

streamlit.map(dat)
