import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html
import math

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



from frontend.frontend import layout
from backend.velocidad import velocidad
from backend.caudal import caudal

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

if __name__ == '__main__':
    app.run_server(debug=True)





