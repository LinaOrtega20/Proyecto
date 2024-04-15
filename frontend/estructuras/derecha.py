import dash
import dash_bootstrap_components as dbc
from dash import html


#importamos las áreas de trabajo
from .area_derecha.area_der import area_der


derecha = dbc.Container([
    dbc.Row([
        dbc.Col("Iteración",md=12,style={'background-color':'green'}),
        dbc.Col(area_der,md=12,style={'background-color':'#90EE90'}),
        #dbc.Col(area_der,md=5,style={'background-color':'#90EE90'}),
    ])
])