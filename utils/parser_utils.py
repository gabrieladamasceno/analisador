#!/usr/bin/env python3

import os
import pandas as pd
from plotly import express as px
import plotly.figure_factory as ff

# Constantes da Documentacao do Android
SIGNAL_TYPE = 'getRilDataRadioTechnology'
SIGNAL_VOICE = 'getRilVoiceRadioTechnology'
SIGNAL_STRENGTH_LTE = 'mLte=CellSignalStrengthLte'
SIGNAL_STRENGTH_WCDMA = 'mWcdma=CellSignalStrengthWcdma'
RSRP = 'rsrp'
RSCP = 'rscp'
RSSI = 'rssi'
RSRQ = 'rsrq'
SIPMSG1 = 'SIPMSG[1]: ['
SIPMSG0 = 'SIPMSG[0]: ['
TECH_X = 'Tempo'
TECH_Y = 'Tecnologia'
SIGNAL_X = 'Tempo'
SIGNAL_Y = 'Potência do Sinal (dBm)'
SIGNAL_Y_RSRQ = 'Qualidade do Sinal (dB)'
RADIO = 'radio'
PROCESS_1 = '10038'
PROCESS_2 = '1000'
MOBILE = 'MobileStatusTracker'
NETWORK_CONTROLLER = 'NetworkController.MobileSignalController'

#Valores para RSRP e RSCP
VERY_POOR = -95
POOR = -85
MODERATE = -75
GOOD = -60
#Valores para RSSI LTE
VERY_POOR_RSSI_LTE = -95
POOR_RSSI_LTE = -85
MODERATE_RSSI_LTE = -75
GOOD_RSSI_LTE = -65
#Valores para RSRQ LTE
VERY_POOR_RSRQ_LTE = -25
POOR_RSRQ_LTE = -20
MODERATE_RSRQ_LTE = -15
GOOD_RSRQ_LTE = -10

# Listas de Busca
key_words_list = []
usual_searchs = []


# Funcoes para encontrar palavras na linha
def find_index(splitted, searching):
    for word in splitted:
        if searching in word:
            return splitted.index(word)

# Funcoes para adicionar palavras encontradas na lista
def result_for_usual_searchs():
    search_result = ''
    for line in usual_searchs:
        search_result = search_result + line
    print(search_result)

#Listas Sinal LTE
def make_signal_lte(line):
    words = (MOBILE, NETWORK_CONTROLLER)
    for word in words:
        if word in line:
            splitted = line.split()
            idx = find_index(splitted, RSRP)
            if splitted[idx][5] == '-':
                signal_time_lte = splitted[0] + '#' + splitted[1]
                signal_lte = splitted[idx][5:]
                return signal_lte, signal_time_lte
    return (None,None)

#Listas Sinal RSSI LTE
def make_signal_rssi_lte(line):
    words = (MOBILE, NETWORK_CONTROLLER)
    for word in words:
        if word in line:
            splitted = line.split()
            idx = find_index(splitted, RSSI)
            if splitted[idx][5] == '-':
                signal_rssi_time_lte = splitted[0] + '#' + splitted[1]
                signal_rssi_lte = splitted[idx][5:]
                return signal_rssi_lte, signal_rssi_time_lte
    return (None,None)

#Listas Sinal RSRQ LTE
def make_signal_rsrq_lte(line):
    words = (MOBILE, NETWORK_CONTROLLER)
    for word in words:
        if word in line:
            splitted = line.split()
            idx = find_index(splitted, RSRQ)
            if splitted[idx][5] == '-':
                signal_rsrq_time_lte = splitted[0] + '#' + splitted[1]
                signal_rsrq_lte = splitted[idx][5:]
                return signal_rsrq_lte, signal_rsrq_time_lte
    return (None,None)

#Listas Sinal WCDMA
def make_signal_wcdma(line):
    words = (MOBILE, NETWORK_CONTROLLER)
    signal_wcdma = '0'
    signal_time_wcdma = '0'
    for word in words:
        if word in line:
            splitted = line.split()
            idx = find_index(splitted, RSCP)
            if splitted[idx][5] == '-':
                signal_time_wcdma = splitted[0] + '#' + splitted[1]
                signal_wcdma = splitted[idx][5:]
                return signal_wcdma, signal_time_wcdma
    return (None,None)

#Funcoes para leitura e busca de termos chaves
def search_in_log_file(user_input):
    data = {
        'tech': [],
        'tech_time': [],
        'tech_voice': [],
        'tech_time_voice': [],
        'signal_lte': [],
        'signal_time_lte': [],
        'signal_wcdma': [],
        'signal_time_wcdma': [],
        'signal_rssi_lte': [],
        'signal_rssi_time_lte': [],
        'signal_rsrq_lte': [],
        'signal_rsrq_time_lte': [],
        'sipmsg_left': [],
        'sipmsg_right': [],
        'sipmsg_time': [],
        'sipmsg_arrow': [],
        'sipmsg_info': []
    }
    # Algoritimo para procurar palavras chaves
    user_input = user_input.replace('\"', "")
    assert os.path.exists(user_input), "Não foi possível encontrar o arquivo:" + str(user_input)
    f = open(user_input, 'r', encoding="ISO-8859-1")
    for line in f:
        for key_word in (key_word for key_word in key_words_list if key_word in line):
            usual_searchs.append(line)
        if SIGNAL_TYPE in line:
            if RADIO in line:
                splitted = line.split()
                if splitted[2] == RADIO:
                    tech_time, tech = make_signal_radio_tech_line(line)
                    data['tech'].append(tech)
                    data['tech_time'].append(tech_time)
            if PROCESS_1 in line:
                splitted = line.split()
                if splitted[2] == PROCESS_1:
                    tech_time, tech = make_signal_radio_tech_line(line)
                    data['tech'].append(tech)
                    data['tech_time'].append(tech_time)
            if PROCESS_2 in line:
                splitted = line.split()
                if splitted[2] == PROCESS_2:
                    tech_time, tech = make_signal_radio_tech_line(line)
                    data['tech'].append(tech)
                    data['tech_time'].append(tech_time)
        if SIGNAL_VOICE in line:
            if RADIO in line:
                splitted_voice = line.split()
                if splitted_voice[2] == RADIO:
                    tech_time_voice, tech_voice = make_signal_voice_tech_line(line)
                    data['tech_voice'].append(tech_voice)
                    data['tech_time_voice'].append(tech_time_voice)
            if PROCESS_1 in line:
                splitted_voice = line.split()
                if splitted_voice[2] == PROCESS_1:
                    tech_time_voice, tech_voice = make_signal_voice_tech_line(line)
                    data['tech_voice'].append(tech_voice)
                    data['tech_time_voice'].append(tech_time_voice)
            if PROCESS_2 in line:
                splitted_voice = line.split()
                if splitted_voice[2] == PROCESS_2:
                    tech_time_voice, tech_voice = make_signal_voice_tech_line(line)
                    data['tech_voice'].append(tech_voice)
                    data['tech_time_voice'].append(tech_time_voice)
        if SIGNAL_STRENGTH_LTE in line:
            signal_lte, signal_time_lte = make_signal_lte(line)
            signal_rssi_lte, signal_rssi_time_lte = make_signal_rssi_lte(line)
            signal_rsrq_lte, signal_rsrq_time_lte = make_signal_rsrq_lte(line)
            if signal_lte:
                data['signal_lte'].append(signal_lte)
                data['signal_time_lte'].append(signal_time_lte)
            if signal_rssi_lte:
                data['signal_rssi_lte'].append(signal_rssi_lte)
                data['signal_rssi_time_lte'].append(signal_rssi_time_lte)
            if signal_rsrq_lte:
                data['signal_rsrq_lte'].append(signal_rsrq_lte)
                data['signal_rsrq_time_lte'].append(signal_rsrq_time_lte)
        if SIGNAL_STRENGTH_WCDMA in line:
            signal_wcdma, signal_time_wcdma = make_signal_wcdma(line)
            if signal_wcdma:
                data['signal_wcdma'].append(signal_wcdma)
                data['signal_time_wcdma'].append(signal_time_wcdma)
        if SIPMSG0 in line:
            sipmsg_time, sipmsg_left, sipmsg_arrow, sipmsg_right, sipmsg_info = make_sipmsg(line)
            data['sipmsg_left'].append(sipmsg_left)
            data['sipmsg_right'].append(sipmsg_right)
            data['sipmsg_time'].append(sipmsg_time)
            data['sipmsg_arrow'].append(sipmsg_arrow)
            data['sipmsg_info'].append(sipmsg_info)
        if SIPMSG1 in line:
            sipmsg_time, sipmsg_left, sipmsg_arrow, sipmsg_right, sipmsg_info = make_sipmsg(line)
            data['sipmsg_left'].append(sipmsg_left)
            data['sipmsg_right'].append(sipmsg_right)
            data['sipmsg_time'].append(sipmsg_time)
            data['sipmsg_arrow'].append(sipmsg_arrow)
            data['sipmsg_info'].append(sipmsg_info)
    f.close()
    if os.path.exists(user_input):
        os.remove(user_input)
    else:
        print("Arquivo não existe")
    return data

#Lista das Tecnologia de Dados
def make_signal_radio_tech_line(line: object) -> object:
    splitted = line.split()
    idx = find_index(splitted, SIGNAL_TYPE)
    tech_time = splitted[0] + '#' + splitted[1]
    tech = splitted[idx][26:].replace(',', '')
    return tech_time, tech

#Lista das Tecnologia de Voz
def make_signal_voice_tech_line(line: object) -> object:
    splitted_voice = line.split()
    idx = find_index(splitted_voice, SIGNAL_VOICE)
    tech_time_voice = splitted_voice[0] + '#' + splitted_voice[1]
    tech_voice = splitted_voice[idx][27:].replace(',', '')
    return tech_time_voice, tech_voice

#Lista das Mensagens SIP
def make_sipmsg(line: object) -> object:
    splitted = line.split()
    sipmsg_time = splitted[0] + '#' + splitted[1]
    if splitted[7] == '[-->]':
        sipmsg_left = '   ' + splitted[8]
        sipmsg_arrow = '------->'
        sipmsg_right = '        | '
        sipmsg_info = splitted[9] + ' ' + splitted[10]
    if splitted[7] == '[<--]':
        sipmsg_right = '   ' + splitted[8]
        sipmsg_arrow = '<-------'
        sipmsg_left = '         | '
        sipmsg_info = splitted[9] + ' ' + splitted[10]
    return sipmsg_time, sipmsg_left, sipmsg_arrow, sipmsg_right, sipmsg_info

#Plotar Tabela das Mensagens SIP
def df_table_sipmsg(sipmsg_time, sipmsg_left, sipmsg_arrow, sipmsg_right, sipmsg_info):
    sipmsg_table = [sipmsg_time, sipmsg_left, sipmsg_arrow, sipmsg_right, sipmsg_info]
    df_sipmsg = pd.DataFrame(sipmsg_table).transpose()
    df_sipmsg.columns = ['Tempo', 'UE', 'Direção', 'Rede', 'Info']
    df_sipmsg['  '] = '  '
    df_sipmsg['   '] = '   '
    df_sipmsg['    '] = '    '
    df_sipmsg['     '] = '     '
    df_sipmsg['      '] = '      '
    df_sipmsg['       '] = '       '
    fig = ff.create_table(df_sipmsg, colorscale=[[0, '#800080'], [.5, '#d8b1d4'], [1, '#ecd8e9']])
    return fig

#Plotar Grafico da Tecnologia de Dados
def df_chart_radio_techlogy(tech_time, tech):
    tech_table = [tech_time, tech]
    tech_dataframe = pd.DataFrame(tech_table).transpose()
    tech_dataframe.columns = [TECH_X, TECH_Y]
    tech_dataframe['Tecnologia de Dados'] = 1
    tech_chart = px.histogram(tech_dataframe, x=TECH_X, y='Tecnologia de Dados', color=TECH_Y,
                               title='Tempo x Tecnologia de Dados')
    tech_chart.update_xaxes(categoryorder='category ascending')
    tech_chart.update_yaxes(dtick=1, range=[0, 1])
    return tech_chart

#Plotar Grafico da Tecnologia de Voz
def df_chart_voice_techlogy(tech_time_voice, tech_voice):
    tech_table = [tech_time_voice, tech_voice]
    tech_dataframe = pd.DataFrame(tech_table).transpose()
    tech_dataframe.columns = [TECH_X, TECH_Y]
    tech_dataframe['Tecnologia de Voz'] = 1
    tech_chart = px.histogram(tech_dataframe, x=TECH_X, y='Tecnologia de Voz', color=TECH_Y,
                               title='Tempo x Tecnologia de Voz')
    tech_chart.update_xaxes(categoryorder='category ascending')
    tech_chart.update_yaxes(dtick=1, range=[0, 1])
    return tech_chart

#Plotar Grafico do RSRP
def df_chart_signal_lte(signal_lte, signal_time_lte):
    signal = list(map(int, signal_lte))
    if signal != []:
        signal_max = max(signal)
        signal_min = min(signal)

    signal_table = [signal_time_lte, signal]
    signal_dataframe = pd.DataFrame(signal_table).transpose()
    signal_dataframe.columns = [SIGNAL_X, SIGNAL_Y]
    signal_dataframe = signal_dataframe.sort_values(by=SIGNAL_X)

    if signal != []:
        signal_chart = px.line(signal_dataframe, x=SIGNAL_X, y=SIGNAL_Y,
                               title='Tempo x Potência do Sinal 4G (RSRP)')
        signal_chart.add_hrect(y0=GOOD, y1=GOOD + 60,
                               line_width=0, fillcolor="green", opacity=0.5)
        signal_chart.add_hrect(y0=MODERATE, y1=GOOD,
                               line_width=0, fillcolor="green", opacity=0.4)
        signal_chart.add_hrect(y0=POOR, y1=MODERATE,
                               line_width=0, fillcolor="yellow", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR, y1=POOR,
                               line_width=0, fillcolor="orange", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR - 30, y1=VERY_POOR,
                               line_width=0, fillcolor="red", opacity=0.4)
        signal_chart.update_yaxes(tick0=MODERATE, dtick=5,
                                  range=[signal_min - 1, signal_max + 1])
        return signal_chart

#Plotar Grafico do RSSI LTE
def df_chart_signal_rssi_lte(signal_rssi_lte, signal_rssi_time_lte):
    signal = list(map(int, signal_rssi_lte))
    if signal != []:
        signal_max = max(signal)
        signal_min = min(signal)

    signal_table = [signal_rssi_time_lte, signal]
    signal_dataframe = pd.DataFrame(signal_table).transpose()
    signal_dataframe.columns = [SIGNAL_X, SIGNAL_Y]
    signal_dataframe = signal_dataframe.sort_values(by=SIGNAL_X)

    if signal != []:
        signal_chart = px.line(signal_dataframe, x=SIGNAL_X, y=SIGNAL_Y,
                               title='Tempo x Intensidade 4G (RSSI)')
        signal_chart.add_hrect(y0=GOOD_RSSI_LTE, y1=GOOD_RSSI_LTE + 60,
                               line_width=0, fillcolor="green", opacity=0.5)
        signal_chart.add_hrect(y0=MODERATE_RSSI_LTE, y1=GOOD_RSSI_LTE,
                               line_width=0, fillcolor="green", opacity=0.4)
        signal_chart.add_hrect(y0=POOR_RSSI_LTE, y1=MODERATE_RSSI_LTE,
                               line_width=0, fillcolor="yellow", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR_RSSI_LTE, y1=POOR_RSSI_LTE,
                               line_width=0, fillcolor="orange", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR_RSSI_LTE - 30, y1=VERY_POOR_RSSI_LTE,
                               line_width=0, fillcolor="red", opacity=0.4)
        signal_chart.update_yaxes(tick0=MODERATE_RSSI_LTE, dtick=5,
                                  range=[signal_min - 1, signal_max + 1])
        return signal_chart

#Plotar Grafico do RSRQ LTE
def df_chart_signal_rsrq_lte(signal_rsrq_lte, signal_rsrq_time_lte):
    signal = list(map(int, signal_rsrq_lte))
    if signal != []:
        signal_max = max(signal)
        signal_min = min(signal)

    signal_table = [signal_rsrq_time_lte, signal]
    signal_dataframe = pd.DataFrame(signal_table).transpose()
    signal_dataframe.columns = [SIGNAL_X, SIGNAL_Y_RSRQ]
    signal_dataframe = signal_dataframe.sort_values(by=SIGNAL_X)

    if signal != []:
        signal_chart = px.line(signal_dataframe, x=SIGNAL_X, y=SIGNAL_Y_RSRQ,
                               title='Tempo x Qualidade do Sinal 4G (RSRQ)')
        signal_chart.add_hrect(y0=GOOD_RSRQ_LTE, y1=GOOD_RSRQ_LTE + 60,
                               line_width=0, fillcolor="green", opacity=0.5)
        signal_chart.add_hrect(y0=MODERATE_RSRQ_LTE, y1=GOOD_RSRQ_LTE,
                               line_width=0, fillcolor="green", opacity=0.4)
        signal_chart.add_hrect(y0=POOR_RSRQ_LTE, y1=MODERATE_RSRQ_LTE,
                               line_width=0, fillcolor="yellow", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR_RSRQ_LTE, y1=POOR_RSRQ_LTE,
                               line_width=0, fillcolor="orange", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR_RSRQ_LTE - 30, y1=VERY_POOR_RSRQ_LTE,
                               line_width=0, fillcolor="red", opacity=0.4)
        signal_chart.update_yaxes(tick0=MODERATE_RSRQ_LTE, dtick=5,
                                  range=[signal_min - 1, signal_max + 1])
        return signal_chart

#Plotar Grafico do RSCP
def df_chart_signal_wcdma(signal_wcdma, signal_time_wcdma):
    signal = list(map(int, signal_wcdma))
    if signal != []:
        signal_max = max(signal)
        signal_min = min(signal)

    signal_table = [signal_time_wcdma, signal]
    signal_dataframe = pd.DataFrame(signal_table).transpose()
    signal_dataframe.columns = [SIGNAL_X, SIGNAL_Y]
    signal_dataframe = signal_dataframe.sort_values(by=SIGNAL_X)

    if signal != []:
        signal_chart = px.line(signal_dataframe, x=SIGNAL_X, y=SIGNAL_Y,
                               title='Tempo x Potência do Sinal 3G (RSCP)')
        signal_chart.add_hrect(y0=GOOD, y1=GOOD + 60,
                               line_width=0, fillcolor="green", opacity=0.5)
        signal_chart.add_hrect(y0=MODERATE, y1=GOOD,
                               line_width=0, fillcolor="green", opacity=0.4)
        signal_chart.add_hrect(y0=POOR, y1=MODERATE,
                               line_width=0, fillcolor="yellow", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR, y1=POOR,
                               line_width=0, fillcolor="orange", opacity=0.4)
        signal_chart.add_hrect(y0=VERY_POOR - 30, y1=VERY_POOR,
                               line_width=0, fillcolor="red", opacity=0.4)
        signal_chart.update_yaxes(tick0=MODERATE, dtick=5,
                                  range=[signal_min - 1, signal_max + 1])
        return signal_chart

#Funcao para Geracao dos graficos
def generate_graphics():
    

    graphics = {
        'Tecnologia de Dados': {},
        'Tecnologia de Voz': {},
        'Potência do Sinal 4G': {},
        'Intensidade do Sinal 4G': {},
        'Qualidade 4G': {},
        'Potência do Sinal 3G': {},
        'Mensagem SIP': {}
    }
    path = os.path.join(os.path.abspath('.'),'data','redes_moveis.log')
    
    if os.path.exists(path):
        data = search_in_log_file(os.path.join(os.path.abspath('.'),'data','redes_moveis.log'))

        graphics['Tecnologia de Dados'] = df_chart_radio_techlogy(data['tech_time'],
                                                                  data['tech'])
        graphics['Tecnologia de Voz'] = df_chart_voice_techlogy(data['tech_time_voice'],
                                                                data['tech_voice'])
        graphics['Potência do Sinal 4G'] = df_chart_signal_lte(data['signal_lte'],
                                                               data['signal_time_lte'])
        graphics['Intensidade do Sinal 4G'] = df_chart_signal_rssi_lte(data['signal_rssi_lte'],
                                                                       data['signal_rssi_time_lte'])
        graphics['Qualidade 4G'] = df_chart_signal_rsrq_lte(data['signal_rsrq_lte'],
                                                            data['signal_rsrq_time_lte'])
        graphics['Potência do Sinal 3G'] = df_chart_signal_wcdma(data['signal_wcdma'],
                                                                 data['signal_time_wcdma'])
        graphics['Mensagem SIP'] = df_table_sipmsg(data['sipmsg_time'], data['sipmsg_left'],
                                                   data['sipmsg_arrow'], data['sipmsg_right'],
                                                   data['sipmsg_info'])
    return graphics