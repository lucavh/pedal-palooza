import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot as plt
import datetime

import src.helper_functions as helper_functions

# -- SETTINGS ------------------------------------------------------------

sns.set_style("ticks")
plt.rcParams.update({"figure.dpi": 300})

st.set_page_config(layout="wide")

# -- DATA ------------------------------------------------------------

# Load and preprocess the generated dataset
availability_df = (
    pd.read_csv("./data/availability_dataset.csv")
    .assign(timestamp = lambda df: pd.to_datetime(df["timestamp"]))
    .pipe(helper_functions.compute_weighted_average)
)

# -- DASHBOARD HEADER ------------------------------------------------------------

# Streamlit app layout
st.title("🚲 Pedal Palooza Analysis")
st.markdown("This is a hobby project that explores data analysis and visualization using Python and Streamlit. The project focuses on analyzing mock data from a fictional sharable bicycle service called OV-Pedal. Please note that the data used in this project is entirely mock and simulated for educational purposes.")

# -- DASHBOARD SIDEBAR ------------------------------------------------------------

st.sidebar.subheader("Filters")

# Add a global time range filter

start_date = st.sidebar.date_input('Select start date', value=datetime.datetime(2023,6,2))
start_time = st.sidebar.time_input('Select start time', datetime.time(7, 00))
end_date = st.sidebar.date_input('Select end date', value=datetime.datetime(2023,6,2))
end_time = st.sidebar.time_input('Select end time', datetime.time(19, 00))

start_datetime = datetime.datetime.combine(start_date, start_time)
end_datetime = datetime.datetime.combine(end_date, end_time)

# Add a global location filter
all_locations = availability_df["location_name"].unique()
selected_locations = st.sidebar.multiselect("Select locations", all_locations, default=all_locations)
if len(selected_locations) == 0:
    selected_locations = all_locations

# Filter data
filtered_df = availability_df[
    (availability_df['timestamp'] >= start_datetime) & 
    (availability_df['timestamp'] <= end_datetime) & 
    (availability_df['location_name'].isin(selected_locations))
]
filtered_df_melted = filtered_df.melt(id_vars=['timestamp', 'location_name', 'weekday', 'weekday_name', 'is_weekend', 'hour', 'week'], var_name='type')


# -- DASHBOARD MAIN CONTENT ------------------------------------------------------------

# -- ROW 1 ------------------------------------------------------------

st.subheader("Sample of the dataset")

st.markdown("This dataset contains **{} locations**. \nThe locations that are included are {}.".format(
        len(all_locations), all_locations
))

st.dataframe(filtered_df.head(50))

# -- ROW 2 ------------------------------------------------------------

st.subheader("How many bikes are available over time?")

st.markdown(
    "This could be some additional text with interesting statistics, like the dataframe has **{} records and {} columns**.".format(
        filtered_df.shape[0], filtered_df.shape[1]
    )
)

tab1, tab2 = st.tabs(["📈 Plotly example", "🐚 Seaborn example"])

# -- ROW 2 - TAB 1 ----------------------------------------------------

fig = px.line(
    filtered_df_melted,
    x="timestamp",
    y="value",
    color="type",
    facet_row="location_name",
    labels=dict(timestamp="", value="Available Bicycles", location_name="Location"),
    height=800
)
fig.update_yaxes(title="")
for anno in fig['layout']['annotations']:
    anno['text']=''
tab1.plotly_chart(fig, theme="streamlit", use_container_width=True)

# -- ROW 2 - TAB 2 ---------------------------------------------------------

# Create a Seaborn plot
g = sns.FacetGrid(filtered_df_melted, row="location_name", aspect=5, height=2, hue="type")
g.map(sns.lineplot, "timestamp", "value")

# Display the plot in Streamlit
tab2.pyplot(g.fig)

# -- ROW 3 ------------------------------------------------------------

st.subheader("What is the typical daily availability pattern?")

fig = px.scatter(
    filtered_df,
    x="n_available",
    y="hour",
    color="location_name",
    facet_col="is_weekend",
    opacity=0.1,
    labels=dict(hour="Hour", n_available="Available Bicycles", location_name="Location", is_weekend="Is Weekend"),
)
fig.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        dtick = 2
    )
)
fig.update_yaxes(range=[-1, 24])
st.plotly_chart(fig, theme="streamlit", use_container_width=True)
