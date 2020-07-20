import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from Graphs import *
from Tables import *
from dash.exceptions import PreventUpdate


app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
app.title='COVID-19 India Tracker'
nav = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Cases Statewise", href='https://api.covid19india.org/csv/latest/state_wise.csv'),
                dbc.DropdownMenuItem("Cases Time Series",
                                     href="https://api.covid19india.org/csv/latest/case_time_series.csv"),
                dbc.DropdownMenuItem("Total Tests",
                                     href="https://api.covid19india.org/csv/latest/tested_numbers_icmr_data.csv"),
                dbc.DropdownMenuItem("Total Tests",
                                     href="https://github.com/ssb30/COVID-19-India-Tracker"),
            ],
            nav=True,
            in_navbar=True,
            label="Important Links",
            expand=True
        ),
    ],
    brand="COVID-19 India Tracker",
    color='rgb(128,128,128)',
    dark=True,
    loading_state=dict(is_loading='True'),
)
breaks = html.Div(
    children=[
        html.Br(),
        html.Br()
    ]
)
card_content1 = [

    dbc.CardBody(
        [
            html.H6("Confirmed", className="card-title"),
            html.P(confirmed_table,
                   className="card-text",
                   ),
        ]
    ),
]

card_content2 = [

    dbc.CardBody(
        [
            html.H6("Active", className="card-title"),
            html.P(active_table,
                   className="card-text",
                   ),
        ]
    ),
]

card_content3 = [

    dbc.CardBody(
        [
            html.H6("Recovered", className="card-title"),
            html.P(recovered_table,
                   className="card-text",
                   ),
        ]
    ),
]

card_content4 = [

    dbc.CardBody(
        [
            html.H6("Deaths", className="card-title"),
            html.P(deaths_table,
                   className="card-text",
                   ),
        ]
    ),
]

body = html.Div(className='row no-gutters',
                children=[
                    html.Div(className='col-md-6 no-gutters',
                             children=[
                                 html.Div(className='leftside',
                                          children=[
                                              html.Div(
                                                  [
                                                      dbc.Row(
                                                          [
                                                              dbc.Col(dbc.Card(card_content1, color="danger",
                                                                               inverse=True, style={"width": "9rem"})),
                                                              dbc.Col(
                                                                  dbc.Card(card_content2, color="info",
                                                                           inverse=True, style={"width": "9rem"})
                                                              ),
                                                              dbc.Col(
                                                                  dbc.Card(card_content3, color="success", inverse=True,
                                                                           style={"width": "9rem"})),
                                                              dbc.Col(
                                                                  dbc.Card(card_content4, color="dark", inverse=True,
                                                                           style={"width": "9rem"}))
                                                          ],
                                                          className="mb-4",
                                                      )
                                                  ]
                                              ),
                                              html.Br(),
                                              ### tables
                                              html.Div(
                                                  children=[
                                                      dbc.Table.from_dataframe(final_frame, className='table-active',
                                                                               responsive=True, hover=True,
                                                                               bordered=True)
                                                  ]
                                              )

                                          ])
                             ])
                    , html.Div(className='col-md-6 no-gutters',
                               children=[
                                   html.Div(className='rightside',
                                            children=[
                                                html.Br(),
                                                html.Br(),
                                                ##Graphs
                                                html.Div(
                                                    children=[
                                                        html.Div([
                                                            dbc.Row(
                                                                [
                                                                    dbc.Button('Cummulative',
                                                                               className='btn btn-outline-secondary',
                                                                               id='cummulative'),
                                                                    dbc.Button('Daily',
                                                                               className='btn btn-outline-secondary',
                                                                               id='Daily'),

                                                                ]
                                                                , justify="center", no_gutters=True),
                                                        ]),
                                                        html.Br(),
                                                        html.H3('CONFIRMED CUMMULATIVE', className='text-danger',
                                                                style={'text-align': 'center'}),
                                                        dcc.Graph(id='confirmed_cummulative'),
                                                        html.H3('CONFIRMED DAILY', className='text-danger',
                                                                style={'text-align': 'center'}),
                                                        dcc.Graph(id='confirmed_daily'),
                                                        html.H3('ACTIVE', className='text-info',
                                                                style={'text-align': 'center'}),
                                                        dcc.Graph(id='active_cummulative'),
                                                        dcc.Graph(id='active_daily'),
                                                        html.H3('RECOVERED', className="text-success",
                                                                style={'text-align': 'center'}),
                                                        dcc.Graph(id='recovered_cummulative'),
                                                        dcc.Graph(id='recovered_daily'),
                                                        html.H3('DEATHS', className="text-secondary",
                                                                style={'text-align': 'center'}),
                                                        dcc.Graph(id='deaths_cummulative'),
                                                        dcc.Graph(id='deaths_daily'),
                                                        html.H3('TESTED', className="text-muted",
                                                                style={'text-align': 'center'}),
                                                        dcc.Graph(id='tests_cummulative'),
                                                        dcc.Graph(id='tests_daily')
                                                    ]
                                                ),
                                            ]
                                            )
                               ])
                ])

app.layout = html.Div([nav, breaks, body])


@app.callback(
    Output(component_id='confirmed_cummulative', component_property='figure'),
    [Input(component_id='cummulative', component_property='n_clicks')]
)
def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_conf_final_cumm


@app.callback(
    Output(component_id='active_cummulative', component_property='figure'),
    [Input(component_id='cummulative', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_act_final_cumm


@app.callback(
    Output(component_id='recovered_cummulative', component_property='figure'),
    [Input(component_id='cummulative', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_rec_final_cumm


@app.callback(
    Output(component_id='deaths_cummulative', component_property='figure'),
    [Input(component_id='cummulative', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_dead_final_cumm


@app.callback(
    Output(component_id='tests_cummulative', component_property='figure'),
    [Input(component_id='cummulative', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_tests_final_cumm


@app.callback(
    Output(component_id='confirmed_daily', component_property='figure'),
    [Input(component_id='Daily', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_conf_final_daily


@app.callback(
    Output(component_id='active_daily', component_property='figure'),
    [Input(component_id='Daily', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_act_final_daily


@app.callback(
    Output(component_id='recovered_daily', component_property='figure'),
    [Input(component_id='Daily', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_rec_final_daily


@app.callback(
    Output(component_id='deaths_daily', component_property='figure'),
    [Input(component_id='Daily', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_dead_final_daily


@app.callback(
    Output(component_id='tests_daily', component_property='figure'),
    [Input(component_id='Daily', component_property='n_clicks')]
)
def update_output1(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return graph_test_final_daily


if __name__ == "__main__":
    app.run_server(debug=True)
