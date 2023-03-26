#!/usr/bin/env python3

from dash import Dash
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.QUARTZ]

app = Dash(
    __name__, suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets
)


app.title = 'Analisador de Logs'
