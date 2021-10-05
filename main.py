import main
import streamlit as st
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

import yfinance as yf


import plotly.graph_objects as go
import plotly.subplots as ms

from sklearn.svm import SVR

style.use('ggplot')  #matplotib style
def app1():
    st.markdown('*** Market Analysis ***')
    def stockDataset(timeframe):

        timeSpan=['1m','2m','5m','15m','30m','60m','90m','1h']

        if timeframe in timeSpan:
            p='7d'
        else:
            p='max'

        try:
            df = yf.download(stockName, interval=timeframe, period=p)
            df.index = pd.to_datetime(df.index)
            df.dropna(inplace=True)
        except:
            st.warning("Stock Name Wrong")

        return df
    #Adding Moving Average & Exponential Moving Average to Data
    def addIndicators(df):
      #adding 50day moving average
      df['50ma'] = df['Close'].rolling(window=50, min_periods=0).mean()
      df['21ma'] = df['Close'].rolling(window=21, min_periods=0).mean()

      #adding 5day expopential moving average
      df['5ema'] = df['Close'].ewm(span=5, adjust=False).mean()

      return df
    def get_buy_sell_list(data):
         buy_list=[]
         sell_list=[]

         flag_long=False
         flag_short=False
         for i in range(0,len(data)):
            if(data['21ma'][i] < data['50ma'][i] and data['5ema'][i] < data['21ma'][i] and flag_long==False and flag_short==False ):
              buy_list.append(data['Close'][i])
              sell_list.append(np.nan)
              flag_short=True
            elif(flag_short==True and data['5ema'][i] > data['21ma'][i]):
              sell_list.append(data['Close'][i])
              buy_list.append(np.nan)
              flag_short=False

            elif(data['21ma'][i] > data['50ma'][i] and data['5ema'][i] > data['21ma'][i] and flag_long==False and flag_short==False ):
              buy_list.append(data['Close'][i])
              sell_list.append(np.nan)
              flag_long=True
            elif(flag_long==True and data['5ema'][i] < data['21ma'][i]):
              sell_list.append(data['Close'][i])
              buy_list.append(np.nan)
              flag_long=False
            else:
              buy_list.append(np.nan)
              sell_list.append(np.nan)

         return (buy_list,sell_list)
    def candlestickChart(df):

      #interactive chart

      #candlestick plot
      figure =go.Figure(
          data =[
                go.Candlestick(
                    x=df.index,
                    low = df['Low'],
                    high = df['High'],
                    close = df['Close'],
                    open = df['Open'],
                    increasing_line_color = 'green',
                    decreasing_line_color = 'red',
                    opacity=0.8
                )
          ]
      )

      #50ma moving average
      figure.add_trace(
        go.Scatter(
            x=df.index,
            y=df['50ma'],
            name="50 Day Moving Avg",
            opacity=0.6)
      )

      #21ma moving average
      figure.add_trace(
        go.Scatter(
            x=df.index,
            y=df['21ma'],
            name="21 Day Moving Avg",
            opacity=0.6)
      )

      #5ema exponential moving average
      figure.add_trace(
        go.Scatter(
            x=df.index,
            y=df['5ema'],
            name="5 Day Exponential Moving Avg",
            opacity=0.6)
      )

      #buy scatter plot
      figure.add_trace(
          go.Scatter(
              x=df.index,
              y=df["Buy"],
              name="Buy Indication",
              opacity=1,
              marker=dict(
                color='green',
                symbol="triangle-up",
                size=10),
              mode='markers'
          )
      )

      #sell scatter plot
      figure.add_trace(
          go.Scatter(
              x=df.index,
              y=df["Sell"],
              name="Sell Indication",
              opacity=1,
              marker=dict(
                color='red',
                symbol='triangle-down',
                size=10),
              mode='markers'
          )
      )

      #plot layout
      figure.update_layout(
          xaxis_rangeslider_visible=False,
          title="Trading View",
          yaxis_title="Price",
          xaxis_title="Date",
          template="plotly_dark"
      )
      figure.show()
      st.plotly_chart(figure)
    stockName = st.text_input("Enter Stock Name(add .NS if NSE Stock):")
    timeframe1=['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']
    timeframe=st.sidebar.selectbox("Select Timeframe",timeframe1)
    if st.button("Analyze"):
        df= stockDataset(timeframe)
        df = addIndicators(df)


        df["Buy"]=get_buy_sell_list(df)[0]
        df["Sell"]=get_buy_sell_list(df)[1]

        candlestickChart(df)
