# US Foreign Aid Analysis - Interactive Dashboard

This repository contains a data analysis project on US Foreign Aid to Pakistan. Various aspects of aid are explored and visualized through interactive dashboards. The data spans from 2001 to 2023 and provides insights into how aid amounts have changed over time, the distribution of aid among different categories, and more.

## Data

The data used in this project comes from the US Foreign Aid website. It includes fields like the fiscal year, assistance category, value of aid, etc.

## Dashboard

The dashboard is built using Dash, a Python framework for building analytical web applications. It includes three interactive graphs:

1. A bar chart showing the top 5 categories of US aid to Pakistan for a selected year.
2. A treemap showing the top sectors receiving aid for a selected year.
3. A pie chart showing the distribution of aid among categories for a selected year.

Each graph has a dropdown menu for selecting the year.

## Running the Dashboard Locally

To run the dashboard locally, follow these steps:

1. Clone this repository.
2. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

3. Run the Dash app:

    ```
    python app.py
    ```

4. Open a web browser and go to `http://127.0.0.1:8050/`.

## Deploying the Dashboard

The dashboard can be deployed on a web server or a platform like Heroku. See the [Dash Deployment Guide](https://dash.plotly.com/deployment) for more information.
