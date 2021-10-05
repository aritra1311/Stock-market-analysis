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
st.set_page_config(page_title='Stock Market Analysis',
                   layout='wide')

PAGES = {

    "MarketAnalysis": main,
    "PriceActionTradeAutomation": price,
    "MacdRsiTradeAutomation": MacdRsi,
    "StockPricePrediction" : predict



}


value = st.selectbox("Select option", options=list(PAGES.keys()))
page = PAGES[value]
if value == "MarketAnalysis":
    page.app1()
elif value == "PriceActionTradeAutomation":
    page.app2()
elif value == "MacdRsiTradeAutomation":
    page.app3()
elif value == "StockPricePrediction":
    page.app4()
