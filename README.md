# Pedal Palooza

This is a hobby project that explores data analysis and visualization using Python and Streamlit. The project focuses on analyzing mock data from a fictional sharable bicycle service called OV-Pedal. Please note that the data in this project does not represent actual data. It is designed purely for educational and experimentation purposes.

## Developing using a Dev Container

This repo includes a [Dev Container](https://code.visualstudio.com/docs/devcontainers/containers). Dev Containers allow you to define a customized, container-based development environment inside Visual Studio Code. To set up the Dev Container, execute the following steps.

1. Install and configure [Docker](https://www.docker.com/get-started) for your operating system. Make sure Docker is running.
2. Install [VS Code](https://code.visualstudio.com/).
3. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in Visual Studio Code.
4. Clone this repository and open in VS Code.
5. You'll get a pop-up saying "Folder contains Dev Container configuration file. Reopen folder to develop in container". Click "Reopen in Container". If the pop-up doesn't show, you can open the Command Palette and select "Dev Containers: Open Folder in Container...".
6. You can now develop and run code in the Dev Container! Note that the repo does not contain any data yet, you can generate the data with the instructions in the next section.

## Data Generation

The `scripts/generate_datasets.py` script generates two dummy datasets simulating the availability of shared bicycles and rental events for a period of 3 months. These datasets are used for analysis and visualization in the Streamlit app.

To generate the datasets, follow these steps:

1. If you are **not** using the Dev Container: install the required libraries listed in `requirements.txt` using `pip install -r requirements.txt`.
2. Run the `generate_datasets.py` script: `python ./src/generate_datasets.py.
3. The datasets will be saved in the `data/` directory.

## Streamlit App

This repo contains a Streamlit app to visualize the generated data. It provides interactive visualizations and insights into bike availability and rental durations across different locations.

### Run the app locally 

To run the Streamlit app locally, follow these steps:

1. If you are **not** using the Dev Container: install the required libraries listed in `requirements.txt` using `pip install -r requirements.txt`.
3. Run the app by executing `streamlit run ./app.py` in your terminal.
4. Copy the URL from the terminal and open it in a web browser, allowing you to explore the data visualizations.

### Run the app in a Docker container

To run the Streamlit app in a Docker container, follow these steps:

1. Make sure your repository contains the generated data, see the section "Data Generation".
2. Install and configure [Docker](https://www.docker.com/get-started) for your operating system. Make sure Docker is running.
2. Open a terminal or command prompt in the directory of the repo and run the following command: `docker build -t pedal-palooza .`
3. After the image is built, run a container from the image with the following command: `docker run -p 8501:8501 pedal-palooza`
4. You can now view your Streamlit app in your browser: [http://0.0.0.0:8501](http://0.0.0.0:8501)

### Deploying the Streamlit app
You can deploy the Streamlit app on Azure using Docker by building the Docker image, pushing it to Azure Container Registry (ACR), and creating an Azure Web App for Containers to run the image. This setup allows you to host and access your Streamlit app on Azure's scalable cloud infrastructure.

## Note on Data Authenticity

This project uses mock data and does not represent actual data. It is designed purely for educational and experimentation purposes.

## Code Generation

Part of the code, including data generation and Streamlit app setup, was generated using [ChatGPT](https://chat.openai.com/). In addition to playing around with Streamlit, I wanted to experiment with promt writing and iterative code development with the help of a tool like ChatGPT.

Feel free to explore, modify, and expand upon the code to learn and experiment further.

For any questions or suggestions, please feel free to reach out.
