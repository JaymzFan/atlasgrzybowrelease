import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


main_page = dbc.Container([
    dbc.Row(dbc.Col(html.H1("main_page lokalizacje"), width='auto'))
])

manage = dbc.Container([
    dbc.Row(dbc.Col(html.H1("manage lokalizacje")))
])
