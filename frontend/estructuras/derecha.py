import dash
import dash_bootstrap_components as dbc
from dash import html


#importamos las áreas de trabajo
from .area_derecha.area1 import area1
from .area_derecha.area2 import area2

derecha = dbc.Container([
    dbc.Row([
        dbc.Col(area1,md=7,style={'background-color':'green'}),
        dbc.Col(area2,md=5,style={'background-color':'write'}),
    ])
])