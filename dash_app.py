import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv('filtered_US_aidpk.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("US Foreign Aid Analysis - Interactive Dashboard"),
    html.P("This repository contains a data analysis project on US Foreign Aid to Pakistan, in which various aspects of aid are explored and visualized through interactive dashboards. The data spans from 2001 to 2023 and provides insights into how aid amounts have changed over time, the distribution of aid among different categories, and more."),
    html.P("Data: The data used in this project comes from the US Foreign Aid website. It includes fields like the fiscal year, assistance category, value of aid, etc."),
    html.Div([
        html.Label('Select Year:'),
        dcc.Dropdown(
            id='year-dropdown-1',
            options=[{'label': i, 'value': i} for i in data['Fiscal Year'].unique()],
            value=data['Fiscal Year'].min(),
            style={'width': '50%', 'margin': '10px auto', 'maxWidth': '300px'}
        ),
        dcc.Graph(id='graph-output-1')
    ]),
    html.Div([
        html.Label('Select Year:'),
        dcc.Dropdown(
            id='year-dropdown-2',
            options=[{'label': i, 'value': i} for i in data['Fiscal Year'].unique()],
            value=data['Fiscal Year'].min(),
            style={'width': '50%', 'margin': '10px auto', 'maxWidth': '300px'}
        ),
        dcc.Graph(id='graph-output-2')
    ]),
    html.Div([
        html.Label('Select Year:'),
        dcc.Dropdown(
            id='year-dropdown-3',
            options=[{'label': i, 'value': i} for i in data['Fiscal Year'].unique()],
            value=data['Fiscal Year'].min(),
            style={'width': '50%', 'margin': '10px auto', 'maxWidth': '300px'}
        ),
        dcc.Graph(id='graph-output-3')
    ])
], style={'padding': '20px'})

# Define the callback to update the graphs
@app.callback(
    [Output('graph-output-1', 'figure'),
     Output('graph-output-2', 'figure'),
     Output('graph-output-3', 'figure')],
    [Input('year-dropdown-1', 'value'),
     Input('year-dropdown-2', 'value'),
     Input('year-dropdown-3', 'value')]
)
def update_graphs(selected_year_1, selected_year_2, selected_year_3):
    # Filter data for the selected year
    data_year_1 = data[data['Fiscal Year'] == selected_year_1]
    data_year_2 = data[data['Fiscal Year'] == selected_year_2]
    data_year_3 = data[data['Fiscal Year'] == selected_year_3]

    # Group by category and sum dollar amounts
    category_sums_1 = data_year_1.groupby('US Category Name')['Current Dollar Amount'].sum().nlargest(5)
    category_sums_2 = data_year_2.groupby('US Category Name')['Current Dollar Amount'].sum()
    category_sums_3 = data_year_3.groupby('US Category Name')['Current Dollar Amount'].sum()

    # Create bar chart
    fig1 = px.bar(category_sums_1, x=category_sums_1.index, y=category_sums_1.values, color=category_sums_1.values,
                  labels={'x': 'Category', 'y': 'Total Dollar Amount'},
                  title=f'Top 5 Categories of US-Aid to Pakistan in {selected_year_1}')

    # Create other figures
    fig2 = px.treemap(data_year_2, path=['US Sector Name'], values='Current Dollar Amount',
                      title=f'Top Sectors Receiving Aid in {selected_year_2}')
    fig3 = px.pie(data_year_3, names='US Category Name', values='Current Dollar Amount',
                  title=f'Distribution of Aid Among Categories in {selected_year_3}')

    return fig1, fig2, fig3

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
