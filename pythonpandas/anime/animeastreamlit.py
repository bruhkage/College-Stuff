import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st





df=pd.read_csv("anime-filteredUpdated.csv")

#st.map(df)

x = st.slider("x",max_value=10)  # 👈 this is a widget


text_search = st.text_input("Search By Anime Name", value="")
st.write(df.loc[(df["Score"] >= x) & (df["Name"].str.contains(text_search,case=False))])
