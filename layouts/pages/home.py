#!/usr/bin/env python3

from dash import html, dcc
from layouts.pages import menu, header, footer


layout = html.Div([
    menu.layout,
    html.Br(),
    header.layout,
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div([
            html.H2("Anexe o Log",style={'text-align':'center'})
        ]),
    ], className='form-control container-fluid'),
    html.Br(),
    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arraste e solte ou ',
                html.A('Selecione um arquivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '8px',
                'textAlign': 'center',
                'margin': '10px'
            },
            multiple=False
        ),

        
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")
        ),
        html.Div([
            dcc.Loading(
                id="loading-2",
                children=[html.Div([html.Div(id='output-data-upload')])],
                type="graph",
            )]
        ),
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div([
        html.Button('Recomeçar', n_clicks=0, id='session-button'),
    ]),
    
    footer.layout
],className="container-fluid")
