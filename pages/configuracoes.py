import dash
from dash import register_page, html



register_page(__name__, path="/configuracoes", title="Configurações")

layout = html.Div("Configurações")