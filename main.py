import streamlit as st
import pandas as pd

st.title("CMPD Traffic Stops")


@st.cache_data  # 👈 Add the caching decorator
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")
st.dataframe(stops)