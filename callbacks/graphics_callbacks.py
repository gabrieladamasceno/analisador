#!/usr/bin/env python3

from app import app
from dash.dependencies import Output, Input


@app.callback(
    Output('technology-data-graphic', 'figure'),
    Input('store', 'data'))
def update_data_technology(data):
    if not data:
        return {}
    return data['Tecnologia de Dados']
    
@app.callback(
    Output('technology-data-voice', 'figure'),
    Input('store', 'data'))
def update_voice_technology(data):
    if not data:
        return {}
    return data['Tecnologia de Voz']

@app.callback(
    Output('signal-lte', 'figure'),
    Input('store', 'data'))
def update_signal_lte(data):
    if not data:
        return {}
    return data['Potência do Sinal 4G']

@app.callback(
    Output('signal-rssi-lte', 'figure'),
    Input('store', 'data'))
def update_signal_rssi_lte(data):
    if not data:
        return {}
    return data['Intensidade do Sinal 4G']

@app.callback(
    Output('rsrq', 'figure'),
    Input('store', 'data'))
def update_signal_rsrq_lte(data):
    if not data:
        return {}
    return data['Qualidade 4G']

@app.callback(
    Output('signal-wcdma', 'figure'),
    Input('store', 'data'))
def update_signal_wcdma(data):
    if not data:
        return {}
    return data['Potência do Sinal 3G']

@app.callback(
    Output('sip', 'figure'),
    Input('store', 'data'))
def update_sip(data):
    if not data:
        return {}
    return data['Mensagem SIP']