#!/usr/bin/env python3

import base64
import datetime
import io
import os
import pandas as pd
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

#Funcao para abrir o arquivo de Log
def save_file(filename, filecontent):
    f = open(
        os.path.join(os.path.abspath('.'),'data',filename),
        "w")
    f.write(filecontent)
    f.close()

#Funcao para leitura do Arquivo de Log
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'log' in filename:
            # Confere se o arquivo e do tipo log
            df = decoded.decode('iso-8859-1')
            
        if 'txt' in filename:
            # Confere se o arquivo e do tipo txt
            df = decoded.decode('utf-8')

        save_file(filename="redes_moveis.log",filecontent=df)
    except Exception as e:
        print(e)
        return html.Div([
            'Houve um erro de processamento deste arquivo.'
        ])

    return html.Div([

        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date))
    ])
