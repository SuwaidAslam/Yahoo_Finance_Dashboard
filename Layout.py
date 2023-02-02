from dash import dcc, html
import dash_bootstrap_components as dbc
from Data import Data
from datetime import date
from dateutil.relativedelta import relativedelta




data = Data()
indicators = data.getIndicators()

class AppLayout:
    def __init__(self):
        self.content =  self.generateContentLayout()
    
    
    # this method generates content Page Layout
    def generateContentLayout(self):
        stocks_list = data.getStocks()
        content = html.Div(id="content",
        children=[
            dcc.Interval(
                id='interval-component',
                interval=24*60*60*1000, # in milliseconds
                n_intervals=0,
                max_intervals=-1
            ),
            dbc.Row([
                dbc.Col(html.H4("Select Stocks"), style={'text-align' : 'center'}),
                dbc.Col(html.H4("Select Indicator"), style={'text-align' : 'center'}),
            ]),
            dbc.Row([
                dbc.Col(dcc.Dropdown(options=stocks_list, value=stocks_list[0], id='stock_dropdown', style={'color' : 'black'})),
                dbc.Col(dcc.Dropdown(options=indicators, value=indicators[0], id='indicator_dropdown', style={'color' : 'black'})),
            ]),
             dbc.Row([
                dbc.Col(html.H5("Start Date"), style={'text-align' : 'right'}),
                dbc.Col(html.H5("End Date"), style={'text-align' : 'left'}),
            ], style={'padding-top' : '10px'}),
            dbc.Row([
                    dbc.Col(dcc.DatePickerSingle(
                        id='start_date_picker',
                        min_date_allowed=date.today() - relativedelta(years=5),
                        max_date_allowed=date.today(),
                        date= date.today() - relativedelta(years=5),
                        display_format='YYYY-MM-DD',
                        style={'color' : 'black', 'padding-top' : '10px'}
                    ), style={'text-align' : 'right'}),
                    dbc.Col(dcc.DatePickerSingle(
                        id='end_date_picker',
                        min_date_allowed=date.today() - relativedelta(years=5),
                        max_date_allowed=date.today(),
                        date=date.today(),
                        display_format='YYYY-MM-DD',
                        style={'color' : 'black', 'padding-top' : '10px'}
                    ), style={'text-align' : 'left'})
            ]),
            dbc.Row([
                dbc.Col(dcc.Graph(id="candlestickGraph", style={'height' : '75vh', 'padding-top' : '10px'}, config={
                    "scrollZoom" : True,
                    "displaylogo": False,
                })),
            ])
        ],
        )
        return content
    
    # ------This method generates Overall App's Layout ---------
    def getAppLayout(self):
        layout = self.content
        return layout

    # ------------------ Layout Settings End --------------------