import dash
from dash import Dash, html, dcc

from google.cloud import storage
import os
from io import StringIO

app = Dash(__name__, use_pages=True)

server = app.server

app.layout = html.Div([
    html.H1('Placeholder Template for "Optimizing Ad Impact"'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)