import streamlit as st
import pandas as pd
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(layout="wide", page_title="PyGWalker + Sttreamlit for EDA")

st.title("PyGWalker + Streamlit for EDA")

uploaded_file = st.file_uploader("Choose your .CSV Data File", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    renderer = StreamlitRenderer(df)
    renderer.explorer()
    