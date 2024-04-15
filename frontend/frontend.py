import dash
import dash_bootstrap_components as dbc
from dash import html

from .estructuras.izquierda import izquierda
from .estructuras.derecha import derecha

layout = dbc.Container([
    dbc.Row([
        dbc.Col(izquierda,md=8,style={'background-color':'red'}),
        dbc.Col(derecha,md=4,style={'background-color':'black'}),
    ])

])