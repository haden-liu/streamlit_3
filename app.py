import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


DATA_URL = (
"Jan_2020_ontime.csv"
)

st.title("Flight Delay Analysis Jan 2020")
st.markdown("This application is a Streamlit dashboard that"
"to analyze flight delay in US Cities")

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.dropna(inplace=True)
    return data

data = load_data(150000)

st.header("How many flight occur during a day of month?")
dayMonth = st.selectbox("Day to look at", range(1,32),1)
data = data[data['DAY_OF_MONTH'] == dayMonth]




if st.checkbox("Show Raw Data", False):
    st.subheader("Raw Data")
    st.write(data)