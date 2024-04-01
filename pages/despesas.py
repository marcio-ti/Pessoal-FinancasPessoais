import dash
from dash import register_page, html



register_page(__name__, path="/despesas", title="Despesas")

layout = html.Div("Despesas")