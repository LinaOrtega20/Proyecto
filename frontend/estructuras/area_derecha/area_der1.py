import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der1= dbc.Container([
    html.Div([
        html.Label('Función objetivo:   '),
        html.Label(id = 'respuestaFO'),
    ]),

    html.Div([
        html.Label('Pérdida por fricción (hf):   '),
        html.Label(id = 'respuestaHF'),
    ]),
    
])