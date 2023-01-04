#Google Trends Part 1 : OK

import streamlit as st
from pytrends.request import TrendReq
import pandas as pd



default1 = "Dwayne Johnson"
default2 = "Spider man"

#1.In a side bar print value in the terminal


pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Mario", 'BMW']
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
df = pytrends.interest_over_time()
df = df.drop(labels=['isPartial'], axis='columns')

#df['trends'] = pytrends.interest_over_time()[default1, default2].values()
#print(df['trends'])
with st.sidebar:
    user_input1 = st.text_input("Confrontation 1 : ", default1)
    user_input2 = st.text_input("Confrontation 2 : ", default2)
    if st.button("Press for the graph and the new confrontation"):
        kw_list = [user_input1, user_input2]
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
        df = pytrends.interest_over_time()
        df = df.drop(labels=['isPartial'], axis='columns')

st.title("Google Trends confrontations")
st.line_chart(df)


















