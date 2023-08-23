# Pedal Palooza

This is a hobby project that explores data analysis and visualization using Python and Streamlit. The project focuses on analyzing mock data from a fictional sharable bicycle service called OV-Pedal. Please note that the data used in this project is entirely mock and simulated for educational purposes.

## Data Generation

The `scripts/generate_datasets.py` script generates two dummy datasets simulating the availability of shared bicycles and rental events for a period of 3 months. These datasets are used for analysis and visualization in the Streamlit app.

To generate the datasets, follow these steps:

1. Install the required libraries listed in `requirements.txt` using `pip install -r requirements.txt`.
2. Run the `generate_datasets.py` script.
3. The datasets will be saved in the `data/` directory.

## Streamlit App

The `scripts/app.py` script sets up a Streamlit app to visualize the generated data. It provides interactive visualizations and insights into bike availability and rental durations across different locations.

To run the Streamlit app, follow these steps:

1. Install Streamlit using `pip install streamlit`.
2. Install the required libraries listed in `requirements.txt` using `pip install -r requirements.txt`.
3. Run the app by executing `streamlit run app/app.py` in your terminal.
4. The app will open in your default web browser, allowing you to explore the data visualizations.

## Note on Data Authenticity

This project uses mock data and does not represent actual data. It is designed purely for educational and experimentation purposes.

## Code Generation

Part of the code, including data generation and Streamlit app setup, was generated using [ChatGPT](https://chat.openai.com/). In addition to playing around with Streamlit, I wanted to experiment with promt writing and iterative code development with the help of a tool likr ChatGPT. 

Feel free to explore, modify, and expand upon the code to learn and experiment further.

For any questions or suggestions, please feel free to reach out.
