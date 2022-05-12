# <-- modules -->
from numpy.core.fromnumeric import mean
import streamlit as st
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib import style
from streamlit.elements import markdown

import yfinance as yf
from sklearn.svm import SVR

style.use('ggplot')  # matplotib style


def app4():
    st.header('Stock/Crypto Price Prediction(BETA)')
    st.markdown(
        '> This function anazyles a stock/crypo data over a month and predicts the price for a day of the month, given by the use. The function uses the [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html) model to predict the future prices.')

    # train ML models

    def trainData(days, adj_close_prices):
        lin_svr = SVR(kernel='linear', C=1000.0)
        lin_svr.fit(days, adj_close_prices)

        poly_svr = SVR(kernel='poly', C=1000.0, degree=2)
        poly_svr.fit(days, adj_close_prices)

        rbf_svr = SVR(kernel='rbf', C=1000.0, gamma=0.85)
        rbf_svr.fit(days, adj_close_prices)

        return lin_svr, poly_svr, rbf_svr

    def plotModels(lin_svr, poly_svr, rbf_svr, days, adj_close_prices):
        plt.figure(figsize=(16, 8))
        plt.scatter(days, adj_close_prices, color='black', label='Data')
        plt.plot(days, rbf_svr.predict(days), color='green', label='RBF Model')
        plt.plot(days, poly_svr.predict(days),
                 color='orange', label='Polynomial Model')
        plt.plot(days, lin_svr.predict(days),
                 color='blue', label='Linear Model')

        plt.xlabel("Days")
        plt.ylabel("Adj Close Price")
        plt.legend()
        plt.title("ML Model Accuracy Chart")
        st.pyplot(plt)

    # get stockname
    st.text("")
    st.text("")

    st.markdown(
        'NOTE: Please Enter **Ticker Name** according to [Yahoo Finance](https://finance.yahoo.com/) Symbols.')
    st.markdown('Add  ```.NS```  for NSE Stocks and  ```.BS```  for BSE Stocks')
    stockName = st.text_input("Enter Stock/Cryptocurrency Name:")
    d = st.sidebar.slider("Select the day of the month:", min_value=1, max_value=31,value=dt.datetime.now().strftime("%d")+1)

    if st.button("Predict Stock/Crypto Prices"):
        # start and and date
        end = dt.date.today()

        start = end.replace(day=1)

        # download data
        df = yf.download(stockName, interval='1d', start=start, end=end)
        df.reset_index(inplace=True)

        # create empty lists
        days = list()
        adj_close_prices = list()

        # get only the dates and adjusted close prices
        df_days = df.loc[:, 'Date']

        df_adj_close = df.loc[:, 'Adj Close']

        # create independent dataSet(dates)
        for day in df_days:
            days.append([int(day.day)])

        # create independent dataSet(Adj Close)
        for adj_close_price in df_adj_close:
            adj_close_prices.append(float(adj_close_price))

        # create 3 models
        lin_svr, poly_svr, rbf_svr = trainData(days, adj_close_prices)

        # plot the models:
        plotModels(lin_svr, poly_svr, rbf_svr, days, adj_close_prices)

        # show the predicted price for a given date
        day = [[d]]
        rbf_pred = rbf_svr.predict(day)[0]
        lin_pred = lin_svr.predict(day)[0]
        poly_pred = poly_svr.predict(day)[0]

        avg_pred = (rbf_pred+lin_pred+poly_pred)/3

        st.write(f'Mean Predicted Price for day {d} is {round(avg_pred,2)}')
        st.write(f'Last Closing Price is {round(df.Close[len(df)-1],2)}')
        price_change = ((df.Close[len(df)-1]-avg_pred)/df.Close[len(df)-1])*100
        st.write(
            f'Expected Price change for day {d} is {round(price_change,2)}%')
