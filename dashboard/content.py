from dashboard.index import app
from dashboard.layout.callbacks import Navigation
from dashboard.layout.header import header
from dash import html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(dbc.Col(header)),
                dbc.Row(dbc.Col(html.Div([
                    dcc.Location(id='url', refresh=True),
                    html.Div(id='page-content')
                ])))
            ],
            fluid=True
        )
    ]
)
