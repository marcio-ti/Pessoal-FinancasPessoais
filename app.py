import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, callback, page_container
import dash.exceptions


app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    use_pages=True,
    suppress_callback_exceptions=True,
)

app.layout = html.Div(
    children=[
        # Menu
        html.Div(
            id="menu",
            children=[
                dbc.Nav(
                    vertical="md",
                    pills=True,
                    children=[
                        html.Img(
                            src="assets/img/menu.png",
                            height=30,
                            width=30,
                            id="icon_menu",
                            n_clicks=0,
                            className="mb-5 mx-3",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/dashboard.png", height=27, width=27
                                )
                            ],
                            href="/",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/salary.png", height=27, width=27
                                )
                            ],
                            href="/receitas",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/payment.png", height=27, width=27
                                )
                            ],
                            href="/despesas",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(src="assets/img/bank.png", height=27, width=27)
                            ],
                            href="/contas",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/investment.png", height=27, width=27
                                )
                            ],
                            href="/investimentos",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/project.png", height=27, width=27
                                )
                            ],
                            href="/projetos",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/calendar.png", height=27, width=27
                                )
                            ],
                            href="/calendario",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(src="assets/img/todo.png", height=27, width=27)
                            ],
                            href="/tarefas",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/medicine.png", height=27, width=27
                                )
                            ],
                            href="/medicamentos",
                            active="exact",
                            className="mb-2",
                        ),
                        dbc.NavLink(
                            children=[
                                html.Img(
                                    src="assets/img/settings.png", height=27, width=27
                                )
                            ],
                            href="/configuracoes",
                            active="exact",
                            id="menu_configuracoes",
                        ),
                    ],
                )
            ],
        ),
        # Página
        html.Div(id="pagina", children=[page_container]),
    ]
)


# ! SERVIDOR
if __name__ == "__main__":
    app.run(
        debug=True,
        port="8050",
        dev_tools_ui=True,
        dev_tools_hot_reload=True,
        threaded=True,
    )
    # app.run(
    #    host="0.0.0.0",
    #    port="8080",
    #    threaded=True,
    # )
