from dash import html

layout = html.Footer([
    html.Div([
        html.P(["2023 - Maria Gabriela Lima Damasceno -  mgld.eng18@uea.edu.br"]),
    ],className='footer'),
],
style={
        'position': 'relative',
        'bottom': '0',
        'width': '100%',
        'height': '60px',
        'text-align': 'center',
},
className='container-fluid')
