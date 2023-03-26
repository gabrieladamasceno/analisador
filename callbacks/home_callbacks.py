#!/usr/bin/env python3

from app import app
from dash.dependencies import Output, Input, State
from utils.file_utils import parse_contents
from utils.parser_utils import generate_graphics


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = parse_contents(list_of_contents, list_of_names, list_of_dates)
        return children


@app.callback(Output('store', 'clear_data'),
              Input('session-button', 'n_clicks'))
def clear_data(n_clicks):
    if n_clicks > 0:
        print("clear data")
        print(n_clicks)
        return True

@app.callback(Output('store', 'data'),
              Input('upload-data', 'contents'))
def update_store_data(contents):
    if contents:
        print("upload data")
        return generate_graphics()
