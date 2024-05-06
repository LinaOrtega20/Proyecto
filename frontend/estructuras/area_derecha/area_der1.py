import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der1= dbc.Container([
    html.Div([
        html.Label('Función objetivo:    '),
        html.Label('________________', style={'color': '#90EE90'}),
        html.Label(id = 'respuestaFO'),
    ]),

    html.Div([
        html.Label('Pérdida por fricción (hf):   '),
        html.Label('________________', style={'color': '#90EE90'}),
        dcc.Input(id = 'respuestaHF', value = 14.8200 , type = 'number', step=0.0001),
    ]),
    
])
