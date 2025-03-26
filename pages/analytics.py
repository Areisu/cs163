import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div([
    html.H1('Analytics and Visualizations'),
    html.Div('This is the analysis and visualizations of the data about advertising.')
])