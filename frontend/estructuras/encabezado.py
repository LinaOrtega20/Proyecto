import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

estilos = {
    'font-weight': 'normal'  # Establecer el peso de la fuente como normal (no negrita)
}

encabezado = dbc.Container([
    html.Hr(),
    html.H6('La hidráulica es una rama de la ingeniería que se enfoca en el estudio y la aplicación de los fluidos en movimiento, particularmente el agua y otros líquidos. Esta disciplina se centra en el análisis del comportamiento de los fluidos y su interacción con estructuras y sistemas, con el objetivo de diseñar, construir y mantener una amplia gama de dispositivos y sistemas hidráulicos para diversas aplicaciones.', style=estilos),
    html.H6('Para el diseño hidráulico de tuberías a presión en Colombia existe el Reglamento Técnico para el Sector de Agua Potable y Saneamiento Básico – RAS y la Resolución 0330 de 2017 expedida por el Ministerio de Vivienda, Ciudad y Territorio, esta normatividad establece los criterios hidráulicos necesarios para el desarrollo de proyectos hidráulicos en el país. Según el RAS  (pág. 166), para el diseño de tuberías a presión se debe implementar la ecuación Darcy-Weisbach y la ecuación de Colebrook-White . Incorporando la ecuación de la velocidad expresada en términos de la pérdida por fricción en la ecuación de la energía, considerando despreciable la presión atmosférica sobre el nivel del agua para ambos tanques y asumiendo que la velocidad en la superficie del agua tiende a cero.', style=estilos),
    html.Img(src='Ejemplo.png'),
    html.Hr()
]),
