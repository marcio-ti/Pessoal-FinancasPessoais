import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from datetime import date


nova_receita_modal = html.Div(
    html.Form(
        children=[
            # DESCRIÇÃO
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Descrição: "),
                        dbc.Textarea(),
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # VALOR
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Valor: "),
                        dbc.Input(type="number", min=0),
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # DATA DE VENCIMENTO
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Data Vencimento: "),
                        dbc.Input(type="date"),
                    ],
                    className="mb-3",
                ), 
                # -------------------------------------------------------------------- #
                # ENTRADA RECORRENTE OU NÃO
                dbc.InputGroup(
                    children=[
                        dbc.Switch(
                            id="standalone-switch",
                            label="Recorrente",
                            value=False,
                        )
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # RECEITA EFETIVADA OU NÃO
                dbc.InputGroup(
                    children=[
                        dbc.Switch(
                            id="standalone-switch",
                            label="Receita Efetivada",
                            value=False,
                        )
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # DATA EFETIVAÇÃO
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Data Efetivação: "),
                        dbc.Input(type="date"),
                    ],
                    className="mb-3",
                ), 
                # -------------------------------------------------------------------- #
                # CATEGORIA
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Categoria: "),
                        dbc.Select()
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # SUB CATEGORIA
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Sub-categoria: "),
                        dbc.Select()
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # CONTA DE LANÇAMENTO
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Conta: "),
                        dbc.Select()
                    ],
                    className="mb-3",
                ),
                # -------------------------------------------------------------------- #
                # DATA LANÇAMENTO
                dbc.InputGroup(
                    children=[
                        dbc.InputGroupText("Data Lançamento: "),
                        dbc.Input(type="date", value=date.today()),
                    ],
                    className="mb-3",
                ), 
                
        ]
    )

)