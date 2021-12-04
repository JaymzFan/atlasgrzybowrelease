import dash_bootstrap_components as dbc

from flask import Flask
from dash import Dash

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    dbc.themes.MORPH
]

server = Flask(__name__)
app = Dash(
        __name__,
        server=server,
        suppress_callback_exceptions=True,
        external_stylesheets=[external_stylesheets[0]]
)

app.title = "Atlas Grzybów"
