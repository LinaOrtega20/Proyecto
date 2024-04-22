import dash
import dash_bootstrap_components as dbc
from dash import html, dcc


estilos = {
    'font-weight': 'normal'  # Establecer el peso de la fuente como normal (no negrita)
}

formulas = dbc.Container([
    html.H6('Formulas', style=estilos),
    html.Hr(),
    html.Img(src='formulas.png')
]),
