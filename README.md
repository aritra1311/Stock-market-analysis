# TRADE AUTOMATOR

## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


Trade Automator is an app that automates stock selection based on some *selection strategies*, lets you *analyze stock data* and even uses machine learning(BETA) to *predict stock prices* for a given date of the month.

The app has 3 main functionalities-
*   **Stock/Crypto Data Analysis**
*   **Stock Selection Automation**
    *   **44-Day MA Trade Automation**
    *   **MACD+RSI Trade Automation**
*   **Stock/Crypto Price Prediction**


## 1. Stock/Crypto Data Analysis-
> This function helps to analyze a particular stock or cryptocoin by providing an interactive candlestick chart with *3 moving averages* and a buy or sell indication marker if there are chances of the stock to rise or fall.

![NSEI Data screenshot](https://github.com/aritra1311/Stock-market-analysis/blob/main/images/ss1.png)


## 2. Stock Selection Automation-
These Automation functions are meant for *swing trading* strategies.
![Swing Trade Pic](https://www.investopedia.com/thmb/mNDwcKtDUpF5xrZjJiuKNGwYlq0=/660x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/dotdash_Final_Swing_Trading_Definition_and_Tactics_Sep_2020-01-4a6d22bec15342ed8ad60170afda74ca.jpg)

### 2.1 44-Day MA Trade Automation-
> This function automates the *Swing trade* stock selection strategy *green candle near rising 44-day moving average* and gives the user a dataset on entry-price, stoploss and target.
sample output for top *25 NSE Stocks accoring to market cap*-
![44day ma automation](https://github.com/aritra1311/Stock-market-analysis/blob/main/images/ss2.png)

### 2.2 MACD+RSI Trade Automation-
> This function automates the stock selection strategy for trading based on [MACD](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/macd) and [RSI](https://www.investopedia.com/terms/r/rsi.asp) Values.
sample output for top *25 NSE Stocks accoring to market cap*-
![macd+rsi automation](https://github.com/aritra1311/Stock-market-analysis/blob/main/images/ss3.png)


## 3. Stock/Crypto Price Prediction(BETA)-
This function anazyles a stock/crypo data over a month and predicts the price for a day of the month, given by the use. The function uses the [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html) model to predict the future prices.
sample output for *TCS.NS Stock*-
![sample prediction](https://github.com/aritra1311/Stock-market-analysis/blob/main/images/ss4.png)
  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Acknowledgements

 - [Investopedia](https://www.investopedia.com/)
 - [SIDDHARTH BHANUSHALI ](https://www.youtube.com/channel/UCoi7mlbUebBpQmDtB3L557A)
 - [Yahoo Finance](https://finance.yahoo.com/)
  
## Authors

- [Adityaprava Sen](https://github.com/AdityapravaSen)
- [Aritra Basu](https://github.com/aritra1311)

  
## Features

- Stock/Crypto Data Analysis
- Stock Selection Automation
  -  44-Day MA Trade Automation
  -  MACD+RSI Trade Automation
- Stock/Crypto Price Prediction

  
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Stock-market-analysis
```

Install dependencies

```bash
  pip install streamlit
  pip install pandas
  pip install matplotlib
  pip install numpy
  pip install yfinance
  pip install sklearn
  pip install plotly
  
```

Start the server

```bash
  streamlit run switch.py
```

  
## Deployment

To deploy this project install [Streamlit](https://streamlit.io/)

```bash
  streamlit run switch.py
```

  
## Support

For support, email [adityapravasen.0911@gmail.com](mailto:adityapravasen.0911@gmail.com) .

  
## Roadmap

![Roadmap](https://github.com/aritra1311/Stock-market-analysis/blob/main/images/ss5.png)


  
## Lessons Learned

As a student learning different investment strategies and the basics of stock trade and investment have always excited me. Also being a student leaning Machine learning and Data Science, I wondered what if I automate the Stock selection strategies that I have learnt using my knowlwge of Data Science. So me and my friend started working on this project.
  
## Optimizations

Further optimizations are neccessary for the Price Prediction model.
Adding more automated trading strategies is required.
optimizations required for clean code.

  
## Feedback

If you have any feedback, please reach out to us at [aritra.or.biddu@gmail.com ](mailto:aritra.or.biddu@gmail.com)
## 🔗 Links

#### Adityaprava Sen-

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://adityapravasen.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adityaprava-sen-0911/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/AdityapravaS)

#### Aritra Basu-

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aritra-basu-58057b192/)

## Disclaimer

Any opinions, chats, messages, news, research, analyses, prices, or other information contained on this Website are provided as general market information for educational and entertainment purposes only, and do not constitute investment advice. The Website should not be relied upon as a substitute for extensive independent market research before making your actual trading decisions. Opinions, market data, recommendations or any other content is subject to change at any time without notice. TradingView, Inc. will not accept liability for any loss or damage, including without limitation any loss of profit, which may arise directly or indirectly from use of or reliance on such information.

We do not recommend the use of technical analysis as a sole means of trading decisions. We do not recommend making hurried trading decisions. You should always understand that PAST PERFORMANCE IS NOT NECESSARILY INDICATIVE OF FUTURE RESULTS.
