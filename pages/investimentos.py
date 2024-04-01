import dash
from dash import register_page, html



register_page(__name__, path="/investimentos", title="Investimentos")

layout = html.Div("Investimentos")