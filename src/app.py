import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

# Load and preprocess the generated dataset
availability_df = pd.read_csv("./data/availability_dataset.csv")
availability_df["timestamp"] = pd.to_datetime(availability_df["timestamp"])  # Convert timestamp to datetime format
availability_df["weekday"] = availability_df["timestamp"].dt.day_of_week
availability_df["weekday_name"] = availability_df["timestamp"].dt.day_name()
availability_df["is_weekend"] = availability_df["weekday"] > 4
availability_df["hour"] = availability_df["timestamp"].dt.hour
availability_df["week"] = availability_df["timestamp"].dt.isocalendar().week

# Streamlit app layout
st.title("🚲 Pedal Palooza Analysis")
st.markdown("This is a hobby project that explores data analysis and visualization using Python and Streamlit. The project focuses on analyzing mock data from a fictional sharable bicycle service called OV-Pedal. Please note that the data used in this project is entirely mock and simulated for educational purposes.")
st.markdown("See [this link](https://observablehq.com/@observablehq/discovering-date-patterns?collection=@observablehq/analyzing-time-series-data#cell-1315) and [this link](https://observablehq.com/@observablehq/noaa-weather-data-by-major-u-s-city?collection=@observablehq/analyzing-time-series-data#cell-236) for inspiration.")

# -- SIDEBAR ------------------------------------------------------------

# Add a global time range filter
st.sidebar.subheader("Time Range Filter")
min_date = availability_df['timestamp'].min()
max_date = availability_df['timestamp'].max()
selected_min_date = st.sidebar.date_input("Select start date", min_date)
selected_max_date = st.sidebar.date_input("Select end date", max_date)

# Add a global location filter
selected_locations = st.sidebar.multiselect("Select locations", availability_df["location_name"].unique())
if len(selected_locations) == 0:
    selected_locations = availability_df["location_name"].unique()
        
filtered_df = availability_df[
    (availability_df['timestamp'].dt.date >= selected_min_date) & 
    (availability_df['timestamp'].dt.date <= selected_max_date) & 
    (availability_df['location_name'].isin(selected_locations))
]

# -- MAIN CONTENT ------------------------------------------------------------

# -- ROW 1 ------------------------------------------------------------

st.subheader("How many bikes are available over time?")

fig = px.line(
    filtered_df,
    x="timestamp",
    y="n_available",
    color="location_name",
    facet_row="location_name",
    labels=dict(timestamp="", n_available="", location_name="Location"),
)
for anno in fig['layout']['annotations']:
    anno['text']=''
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.markdown(
    "Some statistic like **{} records and {} columns**. And then describe the plot a bit more. For example, what the axes mean and which main patterns are visible in the plot. It's a great way to provide additional context and insights. ".format(
        filtered_df.shape[0], filtered_df.shape[1]
    )
)

# -- ROW 2 ------------------------------------------------------------

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

st.markdown(
    "Some statistic like **{} records and {} columns**. And then describe the plot a bit more. For example, what the axes mean and which main patterns are visible in the plot. It's a great way to provide additional context and insights. ".format(
        filtered_df.shape[0], filtered_df.shape[1]
    )
)

# -- ROW 3 ------------------------------------------------------------

st.subheader("What is the typical weekly availability pattern?")

fig = px.scatter(
    filtered_df,
    x="n_available",
    y="hour",
    color="location_name",
    facet_col="week",
    opacity=0.1,
    labels=dict(hour="Hour", n_available="Available Bicycles", location_name="Location", week="Weeknumber"),
)
fig.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        dtick = 2
    )
)
fig.update_yaxes(range=[-1, 24])
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.markdown(
    "Some statistic like **{} records and {} columns**. And then describe the plot a bit more. For example, what the axes mean and which main patterns are visible in the plot. It's a great way to provide additional context and insights. ".format(
        filtered_df.shape[0], filtered_df.shape[1]
    )
)

# Expander
# expander = st.expander("See explanation")
# expander.write("Some statistic like **{} locations with {} as max locations**. And then describe the plot a bit more.".format(
#         locations_df.shape[0], top_location
#     ))

# Tabs
# tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
# tab1.subheader("A tab with a chart")
# fig = px.scatter(
#     filtered_df,
#     x="n_available",
#     y="hour",
#     color="is_weekend"
# )
# fig.update_traces(
#     marker=dict(size=8, symbol="line-ns"),
#     selector=dict(mode="markers"),
#     opacity=0.5,
# )
# tab1.plotly_chart(fig, theme="streamlit", use_container_width=True)
# tab2.subheader("A tab with the data")
# tab2.write(filtered_df)