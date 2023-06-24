import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.express import line

# Load the data from a CSV file
data = pd.read_csv('modified_data.csv')


# Create the Dash app
app = dash.Dash(__name__)

# Function to generate Line chart
def generate_figure(data):
    # create the visualization ( line chart based on the sent data)
    line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        paper_bgcolor="#4C638C",
        font_color= "#EEF0FB"
    )
    return line_chart

H = html.H1('Dash Application',  style= {
        "background-color": '#4C638C',
        "color": "#EEF0FB"}
    )
Title = html.Div(children='''      
Sales of "Pink Morsel"  by Date , to answer “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” 
    ''',     style={
        "background-color": '#4C638C',
        "color": "#EEF0FB",
    })
# filter = dcc.RadioItems(["north", "east", "south", "west", "all"], 'all', id='region', style={"color": "#EEF0FB",'display': 'inline-block', 'margin-right': '10px'})
filter = dcc.RadioItems(
    options=[
        {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'all'}
    ],
    value='all',
    id='region',
    style={
        'color': '#EEF0FB',
        'display': 'flex',
        'flexWrap': 'nowrap'
    }
)
visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

@app.callback(
    Output('visualization', 'figure'),
    Input('region', 'value')
    )
def update_figure(region):
    # filter the dataset
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == region]
    fig = generate_figure(filtered_data)
    return fig

# Define the layout of the app
app.layout = html.Div([
    H,
    Title,
    visualization ,
    filter
],  style={
        "textAlign": "center",
        "background-color": "#4C638C" 
    }
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)