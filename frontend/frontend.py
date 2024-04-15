import dash
import dash_bootstrap_components as dbc
from dash import html

from .estructuras.izquierda import izquierda
from .estructuras.derecha import derecha

layout = dbc.Container([
    dbc.Row([
        dbc.Col('Diseño de tuberías',md=12,style={'background-color':'red'}),
        dbc.Col(izquierda,md=6,style={'background-color':'red'}),
        dbc.Col(derecha,md=6,style={'background-color':'black'}),
    ])

])