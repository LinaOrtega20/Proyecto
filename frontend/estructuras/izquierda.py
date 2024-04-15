import dash
import dash_bootstrap_components as dbc
from dash import html


#importamos las áreas de trabajo
from .area_izquierda.area_izq import area_izq


izquierda = dbc.Container([
    dbc.Row([
        dbc.Col("Input",md=12,style={'background-color':'green'}),
        dbc.Col(area_izq,md=12,style={'background-color':'#90EE90'}),
        dbc.Col("Funcion Objetivo",md=12,style={'background-color':'green'}),
        # Luego se insertara imagen con la formula de la función 
    ])
])