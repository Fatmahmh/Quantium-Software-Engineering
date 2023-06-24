import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.express import line


# Load the data from a CSV file
data = pd.read_csv('modified_data.csv')



# create the visualization
line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1(children='Dash Application'),

    html.Div(children='''
        
Sales of "Pink Morsel"  by Date , to answer “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” 
    '''),

    visualization
])


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)