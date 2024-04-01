import dash
from dash import register_page, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from modulos.entrada_receitas import nova_receita_modal


register_page(__name__, path="/receitas", title="Receitas")

layout = html.Div(
    children=[
        dbc.Button("Nova Receita", id="open", n_clicks=0),
        
        
        
        # ------------------------------------------------------------------------------- #
        # MODAIS #
        # ------------------------------------------------------------------------------- #
        dbc.Modal(
            fade=True,
            size="lg",
            id="modal",
            is_open=False,
            children=[
                dbc.ModalHeader(dbc.ModalTitle("Inserir nova Receita")),
                dbc.ModalBody(nova_receita_modal),
                
            ],
           
        ),
])


@callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open