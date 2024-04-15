import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

area_izq2= dbc.Container([
    dcc.Input(id = 'diametro', value = 0.5 , type = 'number', step=0.1),
    
])