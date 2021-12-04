from dashboard.index import app

# importing and attaching all of the callbacks
from dashboard.layout.callbacks import Navigation

from dash import html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(dbc.Col(html.Div([html.Div(id='header-content')]))),
                dbc.Row(dbc.Col(html.Div([
                    dcc.Location(id='url', refresh=True),
                    html.Div(id='page-content')
                ])))
            ],
            fluid=True
        )
    ]
)
