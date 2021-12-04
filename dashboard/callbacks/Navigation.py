import dash_bootstrap_components as dbc

from dash import no_update

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user

from dashboard.index import app
from dashboard.index import Users, Users_tbl, engine

from dashboard.layout import header as nav_header
from dashboard.layout import main_page
from dashboard.layout import lokalizacje as nav_lokalizacje
from dashboard.layout import grzyby as nav_grzyby
from dashboard.layout import profil as nav_profil
from dashboard.layout import logowanie as nav_logowanie

# ROUTING LOGOWANIA ------------------------------------------------------------
@app.callback(Output('url-rejestracja', 'pathname'),
              [Input('submit-val', 'n_clicks')],
              [State('username', 'value'),
               State('password', 'value'),
               State('useremail', 'value')])
def rejestracja_usera(n_clicks, un, pw, em):
    if un is not None and pw is not None and em is not None:
        hashed_pass = generate_password_hash(pw, method='sha256')
        ins = Users_tbl.insert().values(
                username=un,
                password=hashed_pass,
                email=em
        )
        conn = engine.connect()
        conn.execute(ins)
        conn.close()

        # przerzucic do strony logowania
        return "/profil-logowanie"

    raise PreventUpdate


@app.callback([Output('url_login', 'pathname'),
               Output('output-state', 'children')],
              [Input('login-button', 'n_clicks')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def pwd_check(n_clicks, un, pwd):
    if un is None or pwd is None:
        raise PreventUpdate
    user = Users.query.filter_by(username=un).first()
    if user:
        if check_password_hash(user.password, pwd):
            login_user(user)
            return "/lokalizacje-przegladaj#", no_update

    return no_update, dbc.Alert('Niewłaściwe hasło lub nazwa użytkownika', color='danger')

# ROUTING headera --------------------------------------------------------------
@app.callback(Output('header-content', 'children'),
              Input('url', 'pathname'))
def ustaw_header(url):
    if url == '/profil-wyloguj':
        return nav_header.navbar_niezalogowany

    if current_user.is_authenticated:
        return nav_header.navbar_zalogowany

    return nav_header.navbar_niezalogowany


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/index":
        return main_page.main_page
    elif pathname == '/profil-logowanie':
        return nav_logowanie.login
    elif pathname == '/profil-rejestracja':
        return nav_logowanie.create_account

    if not current_user.is_authenticated:
        return main_page.main_page
    elif pathname == '/profil-wyloguj':
        logout_user()
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
    elif pathname == '/profil-rejestracja':
        return nav_logowanie.create_account
    elif pathname == '/profil-logowanie':
        return nav_logowanie.login

    return main_page.main_page