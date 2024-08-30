import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the time series data
confirmed_df = pd.read_csv('time_series_19-covid-Confirmed_archived_0325.csv')
deaths_df = pd.read_csv('time_series_19-covid-Deaths_archived_0325.csv')

# Melt the data to make it suitable for plotting
confirmed_df = confirmed_df.melt(id_vars=["Country/Region"], 
                                 var_name="Date", 
                                 value_name="Confirmed")
deaths_df = deaths_df.melt(id_vars=["Country/Region"], 
                           var_name="Date", 
                           value_name="Deaths")

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("COVID-19 Dashboard"),
    
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} 
                     for country in confirmed_df['Country/Region'].unique()],
            value='India'
        )
    ]),

    html.Div([
        dcc.Graph(id='cases-graph')
    ]),

    html.Div([
        dcc.Graph(id='deaths-graph')
    ])
])

# Callback for updating graphs based on selected country
@app.callback(
    [Output('cases-graph', 'figure'),
     Output('deaths-graph', 'figure')],
    [Input('country-dropdown', 'value')]
)
def update_graphs(selected_country):
    country_cases = confirmed_df[confirmed_df['Country/Region'] == selected_country]
    country_deaths = deaths_df[deaths_df['Country/Region'] == selected_country]
    
    cases_fig = px.line(country_cases, x='Date', y='Confirmed', 
                        title=f"Cumulative COVID-19 Cases in {selected_country}")
    
    deaths_fig = px.line(country_deaths, x='Date', y='Deaths', 
                         title=f"Cumulative COVID-19 Deaths in {selected_country}")
    
    return cases_fig, deaths_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)