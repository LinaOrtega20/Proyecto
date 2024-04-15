import dash
import dash_bootstrap_components as dbc
from dash import html

from .estructuras.derecha import derecha
from .estructuras.izquierda import izquierda

layout = dbc.Container([
    dbc.Row([
        dbc.Col("DISEÑO DE TUBERÍAS",md=12,style={'background-color':'green'}),
        dbc.Col(izquierda,md=6,style={'background-color':'blue'}),
        dbc.Col(derecha,md=6,style={'background-color':'yellow'}),
    ])

])