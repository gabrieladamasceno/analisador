#!/usr/bin/env python3

from dash import html, dcc
from layouts.pages import menu, header, footer
#from utils.parser_utils import generate_graphics


layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.Div([
            html.H2("Tecnologia de Voz",style={'text-align':'center'})
        ]),
    ], className='form-control container-fluid'),
    html.Br(),
    html.Div([
        dcc.Graph(
            id='technology-data-voice',
            config={"displayModeBar": True},
        )
    ]),
    footer.layout
],className="container-fluid")
