import dash
import dash_bootstrap_components as dbc
from dash import html

from .estructuras.derecha import derecha
from .estructuras.izquierda import izquierda
from .estructuras.encabezado import encabezado

layout = dbc.Container([
    dbc.Row([
        dbc.Col("DISEÑO DE TUBERÍAS",md=12,style={'background-color':'#7CCD7C'}),
        dbc.Col(encabezado,md=12,style={'background-color':'#7CCD7C'}),
        dbc.Col("Modelo",md=12,style={'background-color':'#90EE90'}),
        # se insertara la imagen del modelo 
        dbc.Col(izquierda,md=6,style={'background-color':'#B0FFB0'}),
        dbc.Col(derecha,md=6,style={'background-color':'#B0FFB0'}),
    ])

])

# 7CCD7C La hidráulica es una rama de la ingeniería que se enfoca en el estudio y la aplicación de los fluidos en movimiento, particularmente el agua y otros líquidos. Esta disciplina se centra en el análisis del comportamiento de los fluidos y su interacción con estructuras y sistemas, con el objetivo de diseñar, construir y mantener una amplia gama de dispositivos y sistemas hidráulicos para diversas aplicaciones.