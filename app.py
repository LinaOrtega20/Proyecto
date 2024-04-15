import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



from frontend.frontend import layout
app.layout = layout


if __name__ == '__main__':
    app.run_server(debug=True)

    