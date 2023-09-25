import streamlit as st
import pandas as pd
import requests

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import geopandas as gpd
import folium
from PIL import Image

# brute = pd.read_csv('https://raw.githubusercontent.com/OliverGam/first_streamlit_app/main/Aire_production_AOP.csv',sep=';',encoding='latin-1')
# data_brute = brute[['Département','Aire géographique','CI']]

# fromages_liste = pd.read_csv('https://raw.githubusercontent.com/OliverGam/first_streamlit_app/main/Streamlit_fromage.csv')

# for a,b in data_brute.iterrows():
#    for c,d in fromages_liste.iterrows():
#        if fuzz.partial_ratio(b['Aire géographique'],d['NOM_FROMAGE'])>85:
#                      data_brute.loc[a,'NOM_DU_FROMAGE'] = fromages_liste.loc[c,'NOM_FROMAGE']

#data_brute.drop(columns=['CI'],inplace=True)
#data_brute_merge = data_brute[~data_brute['NOM_DU_FROMAGE'].isna()].copy()
#data_brute_merge[(data_brute_merge['Aire géographique'].str.strip() != data_brute_merge['NOM_DU_FROMAGE'].str.strip())]
#mes_fromages_merge = fromages_liste.merge(data_brute_merge,how='left',left_on='NOM_FROMAGE',right_on='NOM_DU_FROMAGE').drop_duplicates()
#mes_fromages = mes_fromages_merge.drop(columns=['Aire géographique','NOM_DU_FROMAGE']).copy().reset_index(drop=True)
#mes_fromages.drop_duplicates(inplace=True)

mes_fromages_end = pd.read_csv('https://raw.githubusercontent.com/OliverGam/first_streamlit_app/main/mes_fromages_end.csv')
mes_fromages_end = mes_fromages_end[['NOM_FROMAGE','LAIT','Département']]
st.title('Les départements producteurs de fromages AOP')
#st.dataframe(mes_fromages_end)

dep_select = st.multiselect('Quel département souhaitez-vous consulter ?',mes_fromages_end.sort_values('Département').loc[:,'Département'].unique(),['HAUTE-SAONE'])

st.dataframe(mes_fromages_end[mes_fromages_end['Département'].isin(dep_select)][['Département','NOM_FROMAGE','LAIT']].sort_values('Département'))

st.button("Reset",type="primary")
if st.button('Voir à quoi ressemble mon fromage'):
  try:
    for a in dep_select:
      mes_from_dep = mes_fromages_end[mes_fromages_end['Département']==a]
      for b in mes_from_dep['NOM_FROMAGE']: 
        fromage = Image.open(b + '.jpg')
        st.image(fromage,caption = b)
  except:
    print('Il n'y a pas d'image de ce fromage.')
    



