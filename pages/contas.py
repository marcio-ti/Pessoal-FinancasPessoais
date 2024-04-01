import dash
from dash import register_page, html



register_page(__name__, path="/contas", title="Contas")

layout = html.Div("Contas")