import dash
import dash_bootstrap_components as dbc
from dash import html
import math

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



from frontend.frontend import layout
app.layout = layout

@app.callback(
    Output('respuestaV', 'children'),
    Input('Díametro', 'value'),
    Input('Longitud', 'value'),
    Input('Rugosidad', 'value'),
    Input('Viscosidad', 'value'),
    Input('respuestaHF', 'value')
)

def operacionExterna(Díametro, Longitud, Rugosidad, Viscosidad, respuestaHF):
    resultado = Díametro+Longitud+Rugosidad+Viscosidad+respuestaHF
    return str(resultado)

if __name__ == '__main__':
    app.run_server(debug=True)





