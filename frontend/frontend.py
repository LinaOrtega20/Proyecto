import dash
import dash_bootstrap_components as dbc
from dash import html

from .estructuras.derecha import derecha
from .estructuras.izquierda import izquierda

layout = dbc.Container([
    dbc.Row([
        dbc.Col("DISEÑO DE TUBERÍAS",md=12,style={'background-color':'green'}),
        dbc.Col("Modelo",md=12,style={'background-color':'#90EE90'}),
        # se insertara la imagen del modelo 
        dbc.Col(izquierda,md=6,style={'background-color':'write'}),
        dbc.Col(derecha,md=6,style={'background-color':'write'}),
    ])

])