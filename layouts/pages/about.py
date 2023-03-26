from dash import html, dcc
from layouts.pages import menu, header, footer


layout = html.Div([
    menu.layout,
    header.layout,
    html.Br(),
    html.Div([
        html.H1("Sobre", style={'text-align':'center'})
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        dcc.Markdown('''

No mundo atual é quase impossível fazer atividades cotidianas sem o uso das Redes de Comunicação Móvel, seja por dados de internet ou seja por voz. As tecnologias em relação ao funcionamento dessas redes têm uma evolução cada vez maior e mais rápida, sendo o fator principal de diferença entre cada uma delas a capacidade de fornecer serviços com maior eficiência. Dentre os aparelhos de comunicação móvel estão os dispositivos Android, cujo sistema operacional é de código aberto, esses dispositivos geram arquivos de texto, denominados de logs, que indicam quais eventos ocorreram no sistema em um determinado espaço de tempo. Atualmente, uma das funcionalidades do Engenheiro de Telecomunicações é analisar esse tipo de arquivo para poder identificar o funcionamento ou falhas que podem estar ocorrendo nas redes de comunicação móvel, entretanto esse trabalho é bastante manual e demorado. Sendo assim, essa ferramenta em linguagem de programação Python, do tipo Dashboard, pode ser usada para auxiliar nas análises e relatórios realizados pelos Engenheiros de Telecomunicações. 

        ''',
        style={
            'text-align': 'justify'
        })
    ], className='container'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    footer.layout
])
