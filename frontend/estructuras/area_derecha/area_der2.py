import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der2= dbc.Container([
    html.Div([
        html.Label('Velocidad (m/s):   '),
        html.Label(id = 'respuestaV'), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante 
    ]),

    html.Div([
        html.Label('Caudal (m3/s):   '),
        html.Label(id = 'respuestaQ'), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante
    ]),

    html.Div([
        html.Label('Pérdida por fricción (Hf):   '),
        html.Label(id = 'respuestaHF'), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante
    ]),

    html.Div([
        html.Label('Pérdida local (Hl):   '),
        html.Label(id = 'respuestaHL'), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante
    ]),

    html.Div([
        html.Label('Coeficiente de fricción (f):   '),
        html.Label(id = 'respuestaF'), #Este resultado va con formulas complejas, por lo tanto se haran con un bakend más adelante
    ]),


    
])