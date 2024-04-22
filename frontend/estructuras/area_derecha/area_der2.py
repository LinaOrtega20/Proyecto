import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der2= dbc.Container([
    html.Div([
        html.Label('Velocidad (m/s):   '),
        html.Label('________________', style={'color': '#90EE90'}),
        html.Label(id = 'respuestaV'), 
    ]),

    html.Div([
        html.Label('Caudal (m3/s):   '),
        html.Label('________________', style={'color': '#90EE90'}),
        html.Label(id = 'respuestaQ'),
    ]),

    html.Div([
        html.Label('Pérdida por fricción (Hf):   '),
        html.Label('________________', style={'color': '#90EE90'}),
        html.Label(id = 'respuestaPF'), 
    ]),

    html.Div([
        html.Label('Pérdida local (Hl):   '),
        html.Label('________________', style={'color': '#90EE90'}),
        html.Label(id = 'respuestaHL'), 
    ]),

    html.Div([
        html.Label('Coeficiente de fricción (f):   '),
        html.Label('________________', style={'color': '#90EE90'}),
        html.Label(id = 'respuestaF'), 
    ]),


    
])