from dash import html, dcc

layout = html.Div([
    
    html.Ul([
        html.Li([
            dcc.Link('Home',
                     href='/',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Tecnologia de Dados',
                     href='/technology-data',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Tecnologia de Voz',
                     href='/technology-voice',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Potência do Sinal 4G',
                     href='signal-lte',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Intensidade do Sinal 4G',
                     href='signal-rssi-lte',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Qualidade do Sinal 4G',
                     href='rsrq',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Potência do Sinal 3G',
                     href='signal-wcdma',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Mensagens SIP',
                     href='sip',
                     className='nav-link')
        ], className='nav-item'),
        html.Li([
            dcc.Link('Sobre',
                     href='/about',
                     className='nav-link')
        ], className='nav-item'),
    ],className='nav nav-pills')
], className='container-fluid',)