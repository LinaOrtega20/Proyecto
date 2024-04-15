import dash
import dash_bootstrap_components as dbc
from dash import html


#importamos las áreas de trabajo
from .area_izquierda.area_izq1 import area_izq1
from .area_izquierda.area_izq2 import area_izq2

izquierda = dbc.Container([
    dbc.Row([
        dbc.Col("Input",md=12,style={'background-color':'green'}),
        dbc.Col(area_izq1,md=7,style={'background-color':'#90EE90'}),
        dbc.Col(area_izq2,md=5,style={'background-color':'write'}),
    ])
])