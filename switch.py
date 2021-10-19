# <-- modules -->
import streamlit as st

# <-- files -->
import main
import price
import MacdRsi
import predict

st.set_page_config(page_title='Stock Market Analysis',
                   layout='wide')

st.title('TRADE AUTOMATOR')

st.markdown('##### Trade Automator is an app that automates stock selection based on some *selection strategies*, lets you *analyze stock data* and even uses *machine learning(BETA)* to predict stock prices for a given date of the month.')


PAGES = {

    "Market Analysis": main,
    "Price-Action Trade Automation": price,
    "Macd + Rsi Trade Automation": MacdRsi,
    "Stock Price Prediction": predict
}

st.markdown('***')
value = st.selectbox("Select a Functionality", options=list(PAGES.keys()))
page = PAGES[value]

if value == "Market Analysis":
    page.app1()
elif value == "Price-Action Trade Automation":
    page.app2()
elif value == "Macd + Rsi Trade Automation":
    page.app3()
elif value == "Stock Price Prediction":
    page.app4()

st.text('')
st.text('')
st.text('')
st.markdown('##### Disclaimer:')
st.markdown('Any opinions, chats, messages, news, research, analyses, prices, or other information contained on this Website are provided as general market information for educational and entertainment purposes only, and do not constitute investment advice. The Website should not be relied upon as a substitute for extensive independent market research before making your actual trading decisions. Opinions, market data, recommendations or any other content is subject to change at any time without notice. TradingView, Inc. will not accept liability for any loss or damage, including without limitation any loss of profit, which may arise directly or indirectly from use of or reliance on such information.')

st.markdown('We do not recommend the use of technical analysis as a sole means of trading decisions. We do not recommend making hurried trading decisions. You should always understand that PAST PERFORMANCE IS NOT NECESSARILY INDICATIVE OF FUTURE RESULTS.')
st.markdown('***')
st.markdown(
    'Developed with pride and caffeine by  [Adityaprava Sen](https://github.com/AdityapravaSen)  &  [Aritra Basu](https://github.com/aritra1311)')
