#!/usr/bin/env python3

from dash import html, dcc
from layouts.pages import menu, header, footer
#from utils.parser_utils import generate_graphics


layout = html.Div([
    menu.layout,
    header.layout,
    html.Div([
        html.Div([
            html.H2("Mensagens SIP",style={'text-align':'center'})
            ]),
    ], className='form-control container-fluid'),
    html.Br(),
    html.Div([
        dcc.Graph(
            id='sip',
            config={"displayModeBar": True}
        )
    ],
        style={
            'width': '100%'
        }
    ),
    footer.layout
],className="container-fluid")