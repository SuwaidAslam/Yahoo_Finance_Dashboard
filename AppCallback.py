from cmath import e
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from plotly.subplots import make_subplots
from datetime import date
from dateutil.relativedelta import relativedelta
from indicators import *



class AppCallback:
    def __init__(self, app, data):
        self.app = app
        self.data = data
        self.indicators = data.getIndicators()

        self.app.callback(
        [Output('candlestickGraph', 'figure')],
        [
        Input('interval-component', "n_intervals"),
        Input('stock_dropdown', 'value'),
        Input('indicator_dropdown', 'value'),
        Input('start_date_picker', 'date'),
        Input('end_date_picker', 'date')
        ]
        )(self.renderGraph)



    # helper method to apply indicators based on the user selection and price or volume graphs
    def applyIndicator(self, df, indicator_value):
        # here p for is price and v for is volume and s for seprate
        price_vol_ind = 'p'
        indicators_list = self.indicators
        if indicator_value == indicators_list[0]:
            df_ = ema(df)
        elif indicator_value == indicators_list[1]:
            df_ = macd(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[2]:
            df_ = acc_dist(df)
            price_vol_ind = 'v'
        elif indicator_value == indicators_list[3]:
            df_ = on_balance_volume(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[4]:
            df_ = price_volume_trend(df)
            price_vol_ind = 'v'
        elif indicator_value == indicators_list[5]:
            df_ = average_true_range(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[6]:
            df_ = bollinger_bands(df)
        elif indicator_value == indicators_list[7]:
            df_ = chaikin_oscillator(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[8]:
            df_ = typical_price(df)
        elif indicator_value == indicators_list[9]:
            df_ = ease_of_movement(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[10]:
            df_ = mass_index(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[11]:
            df_ = directional_movement_index(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[12]:
            df_ = money_flow_index(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[13]:
            df_ = negative_volume_index(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[14]:
            df_ = positive_volume_index(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[15]:
            df_ = momentum(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[16]:
            df_ = rsi(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[17]:
            df_ = chaikin_volatility(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[18]:
            df_ = williams_ad(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[19]:
            df_ = williams_r(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[20]:
            df_ = trix(df)
            price_vol_ind = 's'
        elif indicator_value == indicators_list[21]:
            df_ = ultimate_oscillator(df)
            price_vol_ind = 's'
        else:
            raise PreventUpdate
        return df_, price_vol_ind

    # callback method to update and render the Volume and Price graphs based on the user selection of Stocks and indicators
    def renderGraph(self, n_intervals, value, indicator_value, start_date, end_date):
        data_df = self.data.getData(start_date, end_date)
        df = data_df[value]
        df = df.dropna()
        df = df.reset_index()
        df, price_vol_ind = self.applyIndicator(df, indicator_value)
        # print(df)

        candlesticks = go.Candlestick(x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            showlegend=False,
            name='OHLC'
            )
        colors = ['#FF4136' if row['Open'] - row['Close'] >= 0
          else '#3D9970' for index, row in df.iterrows()]

        volume_bars = go.Bar(x=df['Date'], y=df['Volume'], 
                showlegend=False,
                marker_color=colors,
                name='Volume'
                )

        indicator_columns = df.columns[6:]
        # for indicators that has 2 columns
        if len(indicator_columns) == 2:
            indicator_columns = indicator_columns[:-1]
         # for indicators that has 3 columns
        elif len(indicator_columns) == 3:
            indicator_columns = indicator_columns[1:]
        # for indicators that has 5 columns
        elif len(indicator_columns) == 5:
            indicator_columns = [indicator_columns[-1]]

        # print(indicator_columns)

        indicator_lines = []
        for col in indicator_columns:
            indicator_line = go.Scatter(x=df['Date'], y=df[col],
                        showlegend=False,
                        # marker_color='yellow',
                        mode='lines',
                        name=col)
            indicator_lines.append(indicator_line)


        if price_vol_ind == 'p':
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, row_heights=[50, 50])
            for line in indicator_lines:
                fig.add_trace(line, row=1, col=1)
        elif price_vol_ind == 'v':
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, row_heights=[50, 50])
            for line in indicator_lines:
                fig.add_trace(line, row=2, col=1)
        else:
            fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.1, row_heights=[40, 30, 30])         
            for line in indicator_lines:
                fig.add_trace(line, row=3, col=1)

        fig.add_trace(candlesticks, row=1, col=1)
        fig.add_trace(volume_bars, row=2, col=1)
        fig.update(layout_xaxis_rangeslider_visible=False)

        # removing all empty dates
        # build complete timeline from start date to end date
        dt_all = pd.date_range(start=df['Date'].iloc[0],end=df['Date'].iloc[-1])
        # retrieve the dates that ARE in the original datset
        dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(df['Date'])]
        # define dates with missing values
        dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]
        
        fig.update_xaxes(
            type='date',
            tickformat = "%b %d, %Y",
            tickangle=0,
            autorange= True,
            showgrid= True,
            rangebreaks=[dict(values=dt_breaks)]
            )
        fig.update_yaxes(
            type= 'linear',
            autorange= True,
            fixedrange=False,
            showgrid= True)
        fig.update_layout(
            # uirevision= 'data', 
            hovermode="closest",
            font= dict(
            size=12,
            # color="#000000"
            color="#ffffff"
            ),
            # title='Stock Price',
            title_x=0.5,
            # template='seaborn',
            template='plotly_dark',
            yaxis1=dict(title="Price"),
            yaxis2=dict(title="Volume"),
        )
        fig['layout']['title']['font'] = dict(size=20)
        return [fig]
    