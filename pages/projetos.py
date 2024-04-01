import dash
from dash import register_page, html



register_page(__name__, path="/projetos", title="Projetos")

layout = html.Div("Projetos")