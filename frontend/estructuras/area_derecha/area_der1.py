import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der1= dbc.Container([
    html.Div([
        html.Label('Función objetivo:   '),
        dcc.Input(id = 'respuestaFO', value = 1 , type = 'number', step=0.1), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante
    ]),

    html.Div([
        html.Label('Pérdida por fricción (hf):   '),
        dcc.Input(id = 'respuestaHF', value = 14.82 , type = 'number', step=0.1), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante
    ]),
    
])