import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_der= dbc.Container([
    html.Div([
        html.Label('Función objetivo:   '),
        html.Label(id = 'salida_Valor_Función_Objetivo:'),
    ]),
 
])