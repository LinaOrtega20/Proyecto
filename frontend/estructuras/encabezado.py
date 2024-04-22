import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

estilos = {
    'font-weight': 'normal'  # Establecer el peso de la fuente como normal (no negrita)
}

encabezado = dbc.Container([
    html.Hr(),
    html.H6('La hidráulica es una rama de la ingeniería que se enfoca en el estudio y la aplicación de los fluidos en movimiento, particularmente el agua y otros líquidos. Esta disciplina se centra en el análisis del comportamiento de los fluidos y su interacción con estructuras y sistemas, con el objetivo de diseñar, construir y mantener una amplia gama de dispositivos y sistemas hidráulicos para diversas aplicaciones.', style=estilos),
    html.Hr()
]),

formulas = dbc.Container([
    html.H6('Formulas', style=estilos),
    html.Hr(),
    html.Img(src='formulas.png')
]),