import dash
import dash_bootstrap_components as dbc
from dash import html

from .estructuras.derecha import derecha
from .estructuras.izquierda import izquierda
from .estructuras.encabezado import encabezado
from .estructuras.formulas import formulas

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("DISEÑO DE TUBERÍAS", style={'font-weight': 'bold'}), md=12, style={'background-color': '#7CCD7C'}),
        dbc.Col(encabezado,md=12,style={'background-color':'#7CCD7C'}),
        dbc.Col("Modelo",md=12,style={'background-color':'#7CCD7C'}),
        # se insertara la imagen del modelo 
        dbc.Col(izquierda,md=6,style={'background-color':'#7CCD7C'}),
        dbc.Col(derecha,md=6,style={'background-color':'#7CCD7C'}),
        dbc.Col(formulas,md=12,style={'background-color':'#7CCD7C'}), 
    ])

])



