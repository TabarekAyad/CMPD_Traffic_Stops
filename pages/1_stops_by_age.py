import streamlit as st
import pandas as pd
import altair as alt

st.title("CMPD Traffic Stops")


@st.cache_data  # 👈 Add the caching decorator
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

age_bar = (
    alt.Chart(stops)
    .mark_bar()
    .encode(x=alt.X("Driver_Age", bin=alt.Bin(maxbins=45)), y="count()")
    .properties(width=500)
)

st.altair_chart(age_bar)

