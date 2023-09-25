import streamlit
import pandas
import requests

import sys
!{sys.executable} -m pip install fuzzywuzzy
!{sys.executable} -m pip install python-Levenshtein
!{sys.executable} -m pip install difflib

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

brute = pd.read_csv('C:/Users/frup00090287/OneDrive - GFI/Bureau/Tuto snowflake/Fromages/Aire_production_AOP.csv',sep=';', encoding='latin-1')
