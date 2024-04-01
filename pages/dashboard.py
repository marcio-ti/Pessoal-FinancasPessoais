import dash
from dash import register_page, html, dcc
import dash_bootstrap_components as dbc



register_page(__name__, path="/", title="Dashboard")

layout = html.Div(
    children=[
        dcc.RadioItems(
            value=2024,
            inline=True,
            inputStyle={'margin-left':'5xp'},
            options=[2023,2024, 2025]
        ),
        dbc.Row(
            className='mt-3',
            children=[
                dbc.Col(
                    width=3,
                    children=[
                    dbc.Card(
                        children=[
                            dbc.CardHeader('Receitas'),
                            dbc.CardBody()
                    ])
                ]),
                
                dbc.Col(
                    width=3,
                    children=[
                    dbc.Card(
                        children=[
                            dbc.CardHeader('Despesas'),
                            dbc.CardBody()
                    ])
                ])
                
            ])
        
    ])