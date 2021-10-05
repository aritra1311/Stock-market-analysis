import main
import price
import MacdRsi
import predict
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
def app4():
    st.markdown("** Stock Prediction **")
    #train ML models
    def trainData(days, adj_close_prices):
        lin_svr = SVR(kernel='linear', C=1000.0)
        lin_svr.fit(days,adj_close_prices)

        poly_svr = SVR(kernel='poly', C=1000.0, degree=2)
        poly_svr.fit(days,adj_close_prices)

        rbf_svr = SVR(kernel='rbf', C=1000.0, gamma=0.85)
        rbf_svr.fit(days,adj_close_prices)

        return lin_svr,poly_svr,rbf_svr
    def plotModels(lin_svr, poly_svr, rbf_svr,days, adj_close_prices):
        plt.figure(figsize=(16,8))
        plt.scatter(days,adj_close_prices,color='black',label='Data')
        plt.plot(days,rbf_svr.predict(days),color='green',label='RBF Model')
        plt.plot(days,poly_svr.predict(days),color='orange',label='Polynomial Model')
        plt.plot(days,lin_svr.predict(days),color='blue',label='Linear Model')

        plt.xlabel("Days")
        plt.ylabel("Adj Close Price")
        plt.legend()
        plt.title("ML Model Accuracy Chart")
        st.pyplot(plt)
     #get stockname
    stockName = st.text_input("Enter Stock Name(add .NS if NSE Stock):")
    d=st.sidebar.slider("Select the day of the month:",1,31)
    if st.button("Predict Stock Prices"):

         #start and and date
         end = dt.date.today()

         start = end.replace(day=1)

              #download data
         df=yf.download(stockName, interval='1d', start=start,end=end)
         df.reset_index(inplace=True)
              #get last row
              #actual_price=df.tail(1)
              #remove last row from dataset
              #df=df.head(len(df)-1)

              #create empty lists
         days=list()
         adj_close_prices=list()

              #get only the dates and adjusted close prices
         df_days=df.loc[:,'Date']

         df_adj_close=df.loc[:,'Adj Close']

              #create independent dataSet(dates)
         for day in df_days:
             days.append([int(day.day)])

              #create independent dataSet(Adj Close)
         for adj_close_price in df_adj_close:
             adj_close_prices.append(float(adj_close_price))

              #create 3 models
         lin_svr, poly_svr, rbf_svr = trainData(days, adj_close_prices)

              #plot the models:
         plotModels(lin_svr, poly_svr, rbf_svr,days, adj_close_prices)

              #show the predicted price for a given date

         day=[[d]]
         st.write(f'The RBF SVR Predicted price is {rbf_svr.predict(day)}')
         st.write(f'The Linear SVR Predicted price is {lin_svr.predict(day)}')
         st.write(f'The Polynomial SVR Predicted price is {poly_svr.predict(day)}')
