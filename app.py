import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html
import math

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



from frontend.frontend import layout
from backend.velocidad import velocidad
from backend.caudal import caudal
from backend.Hf import Hf

app.layout = layout

@app.callback(
    Output('respuestaV', 'children'),
    Input('Díametro', 'value'),
    Input('Longitud', 'value'),
    Input('Rugosidad', 'value'),
    Input('Viscosidad', 'value'),
    Input('respuestaHF', 'value')
)

def OperacionVelocidad(Díametro, Longitud, Rugosidad, Viscosidad, respuestaHF):
    resultadoVelocidad = velocidad(Díametro, Longitud, Rugosidad, Viscosidad, respuestaHF)
    return float(resultadoVelocidad)

@app.callback(
    Output('respuestaQ', 'children'),
    Input('Díametro', 'value'),
    Input('respuestaV', 'children')
)

def OperacionCaudal(Díametro, respuestaV):
    resultadoCaudal = caudal(Díametro, respuestaV)
    return float(resultadoCaudal)

@app.callback(
    Output('respuestaPF', 'children'),
    Input('respuestaHF', 'value'),
)

def OperacionHf(respuestaHF):
    resultadoHf = Hf(respuestaHF)
    return float(resultadoHf)


if __name__ == '__main__':
    app.run_server(debug=True)





