import dash
import dash_bootstrap_components as dbc
from dash import html


#importamos las áreas de trabajo
from .area_derecha.area_der1 import area_der1
from .area_derecha.area_der2 import area_der2

derecha = dbc.Container([
    dbc.Row([
        dbc.Col(area_der1,md=7,style={'background-color':'green'}),
        dbc.Col(area_der2,md=5,style={'background-color':'write'}),
    ])
])