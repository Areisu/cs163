import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

layout = html.Div([
    html.H1('Project Objectives'),
    html.Div('Our main objective is find the factors that make advertisements the most effective.\
             We will analyze the most effective advertising elements that attract consumers to view, share, and engage with our products in order to increase demand for them'),


    html.H2('Test Header')
])
