import pandas as pd
import streamlit as st
import plotly.express as px

# Load the generated datasets
availability_df = pd.read_csv("./data/availability_dataset.csv")
availability_df['timestamp'] = pd.to_datetime(availability_df['timestamp'])  # Convert timestamp to datetime format

# Streamlit app layout
st.title("🚲 Pedal Palooza Analysis")

# Add a global time range filter
st.sidebar.subheader("Time Range Filter")
min_date = availability_df['timestamp'].min()
max_date = availability_df['timestamp'].max()
selected_min_date = st.sidebar.date_input("Select start date", min_date)
selected_max_date = st.sidebar.date_input("Select end date", max_date)

# Add a global location filter
selected_locations = st.sidebar.multiselect("Select locations", availability_df["location_name"].unique())

# Add "Apply Filter" button
apply_filter = st.sidebar.button("Apply Filter")

if apply_filter:
        
    filtered_df = availability_df[
        (availability_df['timestamp'].dt.date >= selected_min_date) & 
        (availability_df['timestamp'].dt.date <= selected_max_date) & 
        (availability_df['location_name'].isin(selected_locations))
    ]

    # Rest of the visualizations and controls
    # Line chart of bike availability for different locations
    st.subheader("Bike Availability Comparison")
    location_data = filtered_df[filtered_df["location_name"].isin(selected_locations)]
    st.line_chart(location_data.pivot(index="timestamp", columns="location_name", values="n_available"))

    # Bar chart of the lower quartile of bike availability for each location
    st.subheader("Lower Quartile of Bike Availability")
    lower_quartile = filtered_df.groupby("location_name")["n_available"].quantile(0.25)
    st.bar_chart(lower_quartile)

    # Bar chart of occurrences of 0 availability for each location
    st.subheader("Occurrences of 0 Availability")
    zeros_df = filtered_df[filtered_df["n_available"]==0].groupby("location_name").size()
    st.bar_chart(zeros_df)

    # Line chart of average bike availability over time
    st.subheader("Average Bike Availability Over Time")
    avg_availability = filtered_df.groupby("timestamp")["n_available"].mean()
    st.line_chart(avg_availability)

    # Stacked area chart of bike availability by location
    st.subheader("Stacked Availability by Location")
    stacked_location_data = location_data.groupby(["timestamp", "location_name"])["n_available"].sum().unstack()
    st.area_chart(stacked_location_data)

    # Histogram of bike availability distribution using Plotly
    st.subheader("Distribution of Bike Availability")
    fig = px.histogram(filtered_df, x="n_available", nbins=20, title="Distribution of Bike Availability")
    st.plotly_chart(fig)

    # Run the app using 'streamlit run app.py' command in your terminal
