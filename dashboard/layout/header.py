import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Przeglądaj", href="lokalizacje-przegladaj#"),
                    dbc.DropdownMenuItem("Dodaj/Usuń lokalizacje", href="lokalizacje-modyfikuj#")
                ],
                nav=True,
                in_navbar=True,
                label="Lokalizacje",
        ),
        dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Przeglądaj", href="grzyby-przegladaj#")
                ],
                nav=True,
                in_navbar=True,
                label="Grzyby",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Szczegóły", href='profil-szczegoly#'),
                dbc.DropdownMenuItem("Znajomi", href="profil-znajomi#"),
                dbc.DropdownMenuItem("Zaloguj", href="profil-zaloguj#"),
                dbc.DropdownMenuItem("Wyloguj", href="profil-wyloguj#")
            ],
            nav=True,
            in_navbar=True,
            label="Mój Profil",
        ),
    ],
    brand="Atlas Grzybów",
    brand_href="index#",
    color="primary",
    dark=True,
    # fixed='top',
    fluid=True,
    links_left=True,
    expand='lg',
    sticky='top'
)

header = navbar