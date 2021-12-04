from dash.dependencies import Input, Output

from dashboard.index import app
from dashboard.layout import main_page
from dashboard.layout import lokalizacje as nav_lokalizacje
from dashboard.layout import grzyby as nav_grzyby
from dashboard.layout import profil as nav_profil


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/index":
        return main_page.main_page
    elif pathname == '/lokalizacje-przegladaj':
        return nav_lokalizacje.main_page
    elif pathname == '/lokalizacje-modyfikuj':
        return nav_lokalizacje.manage
    elif pathname == '/grzyby-przegladaj':
        return nav_grzyby.main_page
    elif pathname == '/profil-szczegoly':
        return nav_profil.szczegoly
    elif pathname == '/profil-znajomi':
        return nav_profil.znajomi
    elif pathname == '/profil-zaloguj':
        return nav_profil.zaloguj

    return main_page.main_page