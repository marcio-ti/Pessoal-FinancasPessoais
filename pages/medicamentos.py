import dash
from dash import register_page, html



register_page(__name__, path="/medicamentos", title="Medicamntos")

layout = html.Div("Medicamentos")