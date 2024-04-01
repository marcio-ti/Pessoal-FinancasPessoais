import dash
from dash import register_page, html


register_page(__name__, path="/calendario", title="Calendário")

layout = html.Div("calendário")
