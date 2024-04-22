import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_izq= dbc.Container([
    html.Div([
    html.Label('Díametro (m):   '),
    html.Label('________________', style={'color': '#90EE90'}),
    dcc.Input(id = 'Díametro', value = 0.32 , type = 'number', step=0.01),
    ]),
    html.Div([
    html.Label('Longitud tubería (m):   '),
    html.Label('________________', style={'color': '#90EE90'}),
    dcc.Input(id = 'Longitud', value = 314.9 , type = 'number', step=0.1),
    ]),
    html.Div([
    html.Label('Rugosidad (m):   '),
    html.Label('________________', style={'color': '#90EE90'}),
    dcc.Input(id = 'Rugosidad', value = 0.000028 , type = 'number', step=0.000001),
    ]),
    html.Div([
    html.Label('Viscosidad (m2/s):   '),
    html.Label('________________', style={'color': '#90EE90'}),
    dcc.Input(id = 'Viscosidad', value = 0.000001 , type = 'number', step=0.000001),
    ]),
    html.Div([
    html.Label('Pérdida de carga H (m):   '),
    html.Label('________________', style={'color': '#90EE90'}),
    dcc.Input(id = 'PérdidaCarga', value = 18 , type = 'number', step=0.1),
    ]),
    html.Div([
    html.Label('Ʃk:   '),
    html.Label('________________', style={'color': '#90EE90'}),
    dcc.Input(id = 'Ʃk', value = 2.7 , type = 'number', step=0.1),
    ]),


])


