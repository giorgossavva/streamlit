# simple_streamlit_app.py
"""
A simple streamlit app
run the app by installing streamlit with pip and typing
> streamlit run simple_streamlit_app.py
"""

import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
#import missingno as msno
import datetime as dt

# Read in the dataset
airbnb = pd.read_csv('https://github.com/marios096/streamlit/blob/main/data.csv?raw=true')

#st.title('Simple Streamlit App')

#st.text('Type a number in the box below')

#n = st.number_input('Number', step=1)

#st.write(f'{n} + 1 = {n+1}')
#
#s = st.text_input('Type a name in the box below')

st.write(f'Hello {airbnb.head()}')

#trying to clear the duplicates 19_10_2021
#drop duplicates from suburb, address and date step 1
#airbnb=airbnb.drop_duplicates(subset=['Suburb','Address','Date','Price','Rooms','Type','Method','SellerG','Regionname','Postcode','Propertycount','Distance','CouncilArea'], keep='last')
#step 2
#airbnb=airbnb.drop_duplicates(subset=['Suburb','Address','Date','Price'], keep='last')
#airbnb.loc[airbnb.duplicated(subset=['Suburb','Address','Date','Price']),:]
#temp=airbnb[airbnb.duplicated(subset=['Suburb','Address','Date'])]
#temp
airbnb.sort_values(by=['Price'], inplace=True)
df = airbnb[airbnb[(['Suburb','Address','Date'])].duplicated(keep=False)]
#df.index

#the drop must be done in airbnb to change the rows of csv
df=df.dropna(subset=['Price'])
df
