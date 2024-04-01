import dash
from dash import register_page, html



register_page(__name__, path="/tarefas", title="Tarefas")

layout = html.Div("Tarefas")