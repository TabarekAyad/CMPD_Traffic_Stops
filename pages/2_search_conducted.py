import streamlit as st
import pandas as pd
import altair as alt

st.title("CMPD Traffic Stops")


@st.cache_data  # 👈 Add the caching decorator
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

search_chart = (
    alt.Chart(stops)
    .mark_bar()
    .encode(x="Was_a_Search_Conducted", y="count()")
    .properties(width=300)
)

st.altair_chart(search_chart)
