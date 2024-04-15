import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der2= dbc.Container([
    html.Div([
        html.Label('Velocidad (m/s):   '),
        html.Label(id = 'respuestaV'),
    ]),

    html.Div([
        html.Label('Caudal (m3/s):   '),
        html.Label(id = 'respuestaQ'),
    ]),

    
])