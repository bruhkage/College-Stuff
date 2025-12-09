import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import  plotly.express as px
from matplotlib.pyplot import title

df = pd.read_csv("fixed_ufo_data.csv")
print(df.head())
"""
shape_counts = df["shape"].value_counts().reset_index()
shape_counts.columns = ["Shape","Count"]

fig = px.bar(shape_counts, x="Shape",y="Count",color="Shape",
             title="Distribution of UFO Shapes",
             labels={"Shape": "Shape", "Count": "Count"},
             template="plotly_white")
fig.show()
"""

"""
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce",format="%m/%d/%Y %H:%M")
df["duration_seconds"] = pd.to_numeric(df["duration_seconds"],errors="coerce")
df["date posted"] = pd.to_datetime(df["date posted"], errors="coerce")
df["latitude"] = pd.to_numeric(df["latitude"],errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"],errors="coerce")
df["year"]=df["datetime"].dt.year
year_counts = df["year"].value_counts().sort_index()

fig = px.line(x=year_counts.index,y=year_counts.values)
fig.update_layout(
    title="Number of UFO Sightings by Year",
    xaxis_title="Year",
    yaxis_title="Y-axis"
)
fig.show()
"""

country_sightings=df.country.value_counts()
country_fig = go.Figure(data=[go.Pie(labels=country_sightings.index,values=country_sightings.values)])
country_fig.show()

state_counts = df["state"].value_counts()
state_percentages = state_counts / state_counts.sum() * 100
state_data = pd.DataFrame({"state": state_percentages.index, "Percentage": state_percentages.values})
state_data = state_data.sort_values("Percentage", ascending=False)
fig= px.bar(state_data, x="state", y="Percentage", labels={"Percentage": "Percentage (%)"})

fig.update_layout(
    title="Percentage of UFO Sightings by State",
    xaxis_title="State",
    yaxis_title="Percentage",
    hovermode="closest"
)
fig.show()