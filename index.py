#!/usr/bin/env python3
import os
from dash import dcc, html
from dash.dependencies import Input, Output
from app import app
from layouts.pages import (
    home,
    technology_data,
    technology_voice,
    signal_lte,
    signal_rssi_lte,
    signal_rsrq_lte,
    signal_wcdma,
    sip,
    about
)
from callbacks import home_callbacks, graphics_callbacks

os.environ['PYTHONUTF8'] = '1'

app.layout = html.Div([
    dcc.Store(id='store',storage_type='local'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname in ('','/'):
        return home.layout
    if pathname == '/technology-data':
        return technology_data.layout
    if pathname == '/technology-voice':
        return technology_voice.layout
    if pathname == '/signal-lte':
        return signal_lte.layout
    if pathname == '/signal-rssi-lte':
        return signal_rssi_lte.layout
    if pathname == '/rsrq':
        return signal_rsrq_lte.layout
    if pathname == '/signal-wcdma':
        return signal_wcdma.layout
    if pathname == '/sip':
        return sip.layout
    elif pathname == '/about':
        return about.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
