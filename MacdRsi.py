# <-- modules -->
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


def app3():
    # List Of Top 500 NSE companies by Market Cap
    ticker_list = ['RELIANCE.NS',
                   'TCS.NS',
                   'HINDUNILVR.NS',
                   'HDFCBANK.NS',
                   'HDFC.NS',
                   'INFY.NS',
                   'KOTAKBANK.NS',
                   'BHARTIARTL.NS',
                   'ITC.NS',
                   'ICICIBANK.NS',
                   'SBIN.NS',
                   'ASIANPAINT.NS',
                   'DMART.NS',
                   'BAJFINANCE.NS',
                   'MARUTI.NS',
                   'HCLTECH.NS',
                   'LT.NS',
                   'WIPRO.NS',
                   'AXISBANK.NS',
                   'ULTRACEMCO.NS',
                   'HDFCLIFE.NS',
                   'COALINDIA.NS',
                   'ONGC.NS',
                   'SUNPHARMA.NS',
                   'NTPC.NS',
                   'POWERGRID.NS',
                   'TITAN.NS',
                   'DABUR.NS',
                   'IOC.NS',
                   'BAJAJFINSV.NS',
                   'PIDILITIND.NS',
                   'BPCL.NS',
                   'HINDZINC.NS',
                   'BRITANNIA.NS',
                   'SBILIFE.NS',
                   'SHREECEM.NS',
                   'BAJAJ-AUTO.NS',
                   'SBICARD.NS',
                   'TECHM.NS',
                   'GODREJCP.NS',
                   'DIVISLAB.NS',
                   'DRREDDY.NS',
                   'ICICIPRULI.NS',
                   'ADANIPORTS.NS',
                   'ICICIGI.NS',
                   'BERGEPAINT.NS',
                   'HDFCAMC.NS',
                   'GSKCONS.NS',
                   'INDIGO.NS',
                   'SIEMENS.NS',
                   'EICHERMOT.NS',
                   'MARICO.NS',
                   'M&M.NS',
                   'JSWSTEEL.NS',
                   'MCDOWELL-N.NS',
                   'GAIL.NS',
                   'CIPLA.NS',
                   'COLPAL.NS',
                   'DLF.NS',
                   'TORNTPHARM.NS',
                   'PGHH.NS',
                   'BANDHANBNK.NS',
                   'BIOCON.NS',
                   'HEROMOTOCO.NS',
                   'GRASIM.NS',
                   'AMBUJACEM.NS',
                   'TATASTEEL.NS',
                   'HAVELLS.NS',
                   'PETRONET.NS',
                   'HINDPETRO.NS',
                   'YESBANK.NS',
                   'ALKEM.NS',
                   'BOSCHLTD.NS',
                   'CADILAHC.NS',
                   'IGL.NS',
                   'LUPIN.NS',
                   'UPL.NS',
                   'NAUKRI.NS',
                   'LTI.NS',
                   'BANKBARODA.NS',
                   'MRF.NS',
                   'MUTHOOTFIN.NS',
                   'NMDC.NS',
                   'INDUSINDBK.NS',
                   'UBL.NS',
                   'PFC.NS',
                   'AUROPHARMA.NS',
                   'VEDL.NS',
                   'ADANIGREEN.NS',
                   'WHIRLPOOL.NS',
                   'HONAUT.NS',
                   'TATAMOTORS.NS',
                   'PNB.NS',
                   'HINDALCO.NS',
                   'GLAXO.NS',
                   '3MINDIA.NS',
                   'PEL.NS',
                   'KANSAINER.NS',
                   'ADANITRANS.NS',
                   'CONCOR.NS',
                   'NHPC.NS',
                   'IDBI.NS',
                   'BAJAJHLDNG.NS',
                   'ABB.NS',
                   'JUBLFOOD.NS',
                   'MOTHERSUMI.NS',
                   'PAGEIND.NS',
                   'TATACONSUM.NS',
                   'NIACL.NS',
                   'GICRE.NS',
                   'PFIZER.NS',
                   'ACC.NS',
                   'BEL.NS',
                   'GILLETTE.NS',
                   'IPCALAB.NS',
                   'RECLTD.NS',
                   'HAL.NS',
                   'OFSS.NS',
                   'TRENT.NS',
                   'RAJESHEXPO.NS',
                   'PIIND.NS',
                   'SRF.NS',
                   'COROMANDEL.NS',
                   'GUJGASLTD.NS',
                   'APOLLOHOSP.NS',
                   'BATAINDIA.NS',
                   'VOLTAS.NS',
                   'IRCTC.NS',
                   'BALKRISIND.NS',
                   'VBL.NS',
                   'NAM-INDIA.NS',
                   'GODREJPROP.NS',
                   'ADANIENT.NS',
                   'SRTRANSFIN.NS',
                   'RELAXO.NS',
                   'AUBANK.NS',
                   'SANOFI.NS',
                   'TVSMOTOR.NS',
                   'ASTRAL.NS',
                   'MINDTREE.NS',
                   'TORNTPOWER.NS',
                   'SUNDARMFIN.NS',
                   'AARTIIND.NS',
                   'AIAENG.NS',
                   'CROMPTON.NS',
                   'ASHOKLEY.NS',
                   'MPHASIS.NS',
                   'LTTS.NS',
                   'RAMCOCEM.NS',
                   'OBEROIRLTY.NS',
                   'CHOLAFIN.NS',
                   'AJANTPHARM.NS',
                   'ZEEL.NS',
                   'LICHSGFIN.NS',
                   'ATUL.NS',
                   'ABFRL.NS',
                   'LALPATHLAB.NS',
                   'WABCOINDIA.NS',
                   'SCHAEFFLER.NS',
                   'SUNTV.NS',
                   'EXIDEIND.NS',
                   'POLYCAB.NS',
                   'SUPREMEIND.NS',
                   'BHARATFORG.NS',
                   'ADANIPOWER.NS',
                   'BANKINDIA.NS',
                   'MFSL.NS',
                   'L&TFH.NS',
                   'IDFCFIRSTB.NS',
                   'AKZOINDIA.NS',
                   'APLLTD.NS',
                   'GMRINFRA.NS',
                   'CASTROLIND.NS',
                   'UNIONBANK.NS',
                   'ABCAPITAL.NS',
                   'GSPL.NS',
                   'SYNGENE.NS',
                   'GODREJIND.NS',
                   'FORTIS.NS',
                   'SAIL.NS',
                   'ADANIGAS.NS',
                   'CUB.NS',
                   'DALBHARAT.NS',
                   'CANBK.NS',
                   'AAVAS.NS',
                   'SUMICHEM.NS',
                   'NATCOPHARM.NS',
                   'M&MFIN.NS',
                   'CRISIL.NS',
                   'CUMMINSIND.NS',
                   'OIL.NS',
                   'IDEA.NS',
                   'ISEC.NS',
                   'INDHOTEL.NS',
                   'TATAPOWER.NS',
                   'IOB.NS',
                   'THERMAX.NS',
                   'IIFLWAM.NS',
                   'PHOENIXLTD.NS',
                   'ENDURANCE.NS',
                   'JINDALSTEL.NS',
                   'HATSUN.NS',
                   'SOLARINDS.NS',
                   'FEDERALBNK.NS',
                   'AMARAJABAT.NS',
                   'SJVN.NS',
                   'ESCORTS.NS',
                   'MGL.NS',
                   'MANAPPURAM.NS',
                   'VINATIORGA.NS',
                   'UCOBANK.NS',
                   'EMAMILTD.NS',
                   'ZYDUSWELL.NS',
                   'MOTILALOFS.NS',
                   'SKFINDIA.NS',
                   'BHEL.NS',
                   'JKCEMENT.NS',
                   'NIITTECH.NS',
                   'GODREJAGRO.NS',
                   'JSWENERGY.NS',
                   'CENTRALBK.NS',
                   'RBLBANK.NS',
                   'HEXAWARE.NS',
                   'TTKPRESTIG.NS',
                   'PRESTIGE.NS',
                   'TATACOMM.NS',
                   'VGUARD.NS',
                   'METROPOLIS.NS',
                   'SIS.NS',
                   'MINDAIND.NS',
                   'SFL.NS',
                   'RITES.NS',
                   'SUNDRMFAST.NS',
                   'NLCINDIA.NS',
                   'PVR.NS',
                   'NAVINFLUOR.NS',
                   'PGHL.NS',
                   'ASTRAZEN.NS',
                   'KAJARIACER.NS',
                   'FINEORG.NS',
                   'JCHAC.NS',
                   'GLENMARK.NS',
                   'TIMKEN.NS',
                   'TATACHEM.NS',
                   'IBVENTURES.NS',
                   'ITI.NS',
                   'INDIAMART.NS',
                   'SYMPHONY.NS',
                   'JMFINANCIL.NS',
                   'CHOLAHLDNG.NS',
                   'NATIONALUM.NS',
                   'CESC.NS',
                   'DEEPAKNTR.NS',
                   'BLUEDART.NS',
                   'MAHABANK.NS',
                   'TIINDIA.NS',
                   'BBTC.NS',
                   'ERIS.NS',
                   'NH.NS',
                   'GRINDWELL.NS',
                   'SHRIRAMCIT.NS',
                   'ESSELPACK.NS',
                   'GODFRYPHLP.NS',
                   'FINPIPE.NS',
                   'BASF.NS',
                   'CREDITACC.NS',
                   'ASTERDM.NS',
                   'KEC.NS',
                   'AEGISCHEM.NS',
                   'UJJIVANSFB.NS',
                   'APOLLOTYRE.NS',
                   'CHAMBLFERT.NS',
                   'BLUESTARCO.NS',
                   'VSTIND.NS',
                   'RATNAMANI.NS',
                   'PERSISTENT.NS',
                   'CHALET.NS',
                   'CARBORUNIV.NS',
                   'GALAXYSURF.NS',
                   'ORIENTELEC.NS',
                   'DIXON.NS',
                   'LINDEINDIA.NS',
                   'IBULHSGFIN.NS',
                   'JBCHEPHARM.NS',
                   'MRPL.NS',
                   'AVANTIFEED.NS',
                   'HUDCO.NS',
                   'JUBILANT.NS',
                   'FRETAIL.NS',
                   'TATAELXSI.NS',
                   'AMBER.NS',
                   'IEX.NS',
                   'ASAHIINDIA.NS',
                   'ENGINERSIN.NS',
                   'SPANDANA.NS',
                   'EIHOTEL.NS',
                   'CANFINHOME.NS',
                   'KIOCL.NS',
                   'GMMPFAUDLR.NS',
                   'GRANULES.NS',
                   'VTL.NS',
                   'EDELWEISS.NS',
                   'IRCON.NS',
                   'RADICO.NS',
                   'COCHINSHIP.NS',
                   'LAURUSLABS.NS',
                   'NESCO.NS',
                   'RALLIS.NS',
                   'VIPIND.NS',
                   'BDL.NS',
                   'JYOTHYLAB.NS',
                   'DCMSHRIRAM.NS',
                   'TATAINVEST.NS',
                   'MIDHANI.NS',
                   'FDC.NS',
                   'CENTURYTEX.NS',
                   'INDIACEM.NS',
                   'HEIDELBERG.NS',
                   'CEATLTD.NS',
                   'BIRLACORPN.NS',
                   'GEPIL.NS',
                   'POWERINDIA.NS',
                   'KRBL.NS',
                   'QUESS.NS',
                   'FLUOROCHEM.NS',
                   'FINCABLES.NS',
                   'APLAPOLLO.NS',
                   'SUNTECK.NS',
                   'BAJAJELEC.NS',
                   'GESHIP.NS',
                   'SUNCLAYLTD.NS',
                   'CERA.NS',
                   'CGCL.NS',
                   'DCBBANK.NS',
                   'NBCC.NS',
                   'GPPL.NS',
                   'DBL.NS',
                   'STAR.NS',
                   'MASFIN.NS',
                   'KALPATPOWR.NS',
                   'STARCEMENT.NS',
                   'OMAXE.NS',
                   'TEAMLEASE.NS',
                   'KNRCON.NS',
                   'PNBHOUSING.NS',
                   'INOXLEISUR.NS',
                   'TV18BRDCST.NS',
                   'REDINGTON.NS',
                   'RVNL.NS',
                   'BRIGADE.NS',
                   'INDIANB.NS',
                   'THYROCARE.NS',
                   'TECHNOE.NS',
                   'MAHINDCIE.NS',
                   'VMART.NS',
                   'GULFOILLUB.NS',
                   'SUDARSCHEM.NS',
                   'STRTECH.NS',
                   'AFFLE.NS',
                   'SUVENPHAR.NS',
                   'SPARC.NS',
                   'CYIENT.NS',
                   'GRAPHITE.NS',
                   'VAIBHAVGBL.NS',
                   'CENTURYPLY.NS',
                   'SWANENERGY.NS',
                   'EIDPARRY.NS',
                   'LAXMIMACH.NS',
                   'ALKYLAMINE.NS',
                   'MOIL.NS',
                   'PNCINFRA.NS',
                   'KEI.NS',
                   'LUXIND.NS',
                   'HATHWAY.NS',
                   'FLFL.NS',
                   'IIFL.NS',
                   'IDFC.NS',
                   'CCL.NS',
                   'GARFIBRES.NS',
                   'MAHSCOOTER.NS',
                   'KPRMILL.NS',
                   'JKLAKSHMI.NS',
                   'TASTYBITE.NS',
                   'INDOSTAR.NS',
                   'BALRAMCHIN.NS',
                   'INFIBEAM.NS',
                   'CDSL.NS',
                   'BHARATRAS.NS',
                   'WELSPUNIND.NS',
                   'RESPONIND.NS',
                   'TRIDENT.NS',
                   'KSCL.NS',
                   'CAPLIPOINT.NS',
                   'VAKRANGEE.NS',
                   'TCIEXP.NS',
                   'ICRA.NS',
                   'POLYMED.NS',
                   'CSBBANK.NS',
                   'TCNSBRANDS.NS',
                   'SHILPAMED.NS',
                   'ZENSARTECH.NS',
                   'HINDCOPPER.NS',
                   'BAJAJCON.NS',
                   'INGERRAND.NS',
                   'INDOCO.NS',
                   'NETWORK18.NS',
                   'SEQUENT.NS',
                   'WOCKPHARMA.NS',
                   'JUSTDIAL.NS',
                   'FSL.NS',
                   'TRITURBINE.NS',
                   'BEML.NS',
                   'RAIN.NS',
                   'IRB.NS',
                   'HEG.NS',
                   'MHRIL.NS',
                   'IBREALEST.NS',
                   'MMTC.NS',
                   'GET&D.NS',
                   'UJJIVAN.NS',
                   'TATASTLBSL.NS',
                   'FMGOETZE.NS',
                   'GNFC.NS',
                   'ELGIEQUIP.NS',
                   'DELTACORP.NS',
                   'SCI.NS',
                   'LEMONTREE.NS',
                   'SONATSOFTW.NS',
                   'VARROC.NS',
                   'BSOFT.NS',
                   'SHOPERSTOP.NS',
                   'ESABINDIA.NS',
                   'VESUVIUS.NS',
                   'MAXINDIA.NS',
                   'GUJALKALI.NS',
                   'LAOPALA.NS',
                   'MAHLOG.NS',
                   'WELCORP.NS',
                   'FAIRCHEM.NS',
                   'KARURVYSYA.NS',
                   'GREAVESCOT.NS',
                   'JSWHL.NS',
                   'ADVENZYMES.NS',
                   'SUPRAJIT.NS',
                   'SCHNEIDER.NS',
                   'GRSE.NS',
                   'RCF.NS',
                   'DHANUKA.NS',
                   'PRSMJOHNSN.NS',
                   'NILKAMAL.NS',
                   'KSB.NS',
                   'NAVNETEDUL.NS',
                   'PAPERPROD.NS',
                   'JINDALSAW.NS',
                   'EQUITAS.NS',
                   'GSFC.NS',
                   'DEN.NS',
                   'TCI.NS',
                   'RAYMOND.NS',
                   'ALLCARGO.NS',
                   'ORIENTREF.NS',
                   'FCONSUMER.NS',
                   'VRLLOG.NS',
                   'DBCORP.NS',
                   'BALMLAWRIE.NS',
                   'ECLERX.NS',
                   'JAGRAN.NS',
                   'BSE.NS',
                   'JKPAPER.NS',
                   'MINDACORP.NS',
                   'KTKBANK.NS',
                   'MAHSEAMLES.NS',
                   'ACCELYA.NS',
                   'SOBHA.NS',
                   'KIRLOSENG.NS',
                   'SUPPETRO.NS',
                   'SWSOLAR.NS',
                   'HSCL.NS',
                   'GAEL.NS',
                   'GREENLAM.NS',
                   'VENKEYS.NS',
                   'JSL.NS',
                   'AARTIDRUGS.NS',
                   'PSPPROJECT.NS',
                   'DIAMONDYD.NS',
                   'NIITLTD.NS',
                   'HFCL.NS',
                   'ASHOKA.NS',
                   'SOLARA.NS',
                   'ARVINDFASN.NS',
                   'AHLUCONT.NS',
                   'PTC.NS',
                   'HGINFRA.NS',
                   'PRINCEPIPE.NS',
                   'NCC.NS',
                   'FACT.NS',
                   'TIDEWATER.NS',
                   'ITDC.NS',
                   'APARINDS.NS']

    st.header('Stock Selection Automation-')
    st.markdown(
        'These Automation functions are meant for *[swing trading](https://www.investopedia.com/trading/introduction-to-swing-trading/)* strategies.')

    st.subheader('MACD + RSI Trade Automation')
    st.markdown(
        '> This function automates the stock selection strategy for trading based on [MACD](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/macd) and [RSI](https://www.investopedia.com/terms/r/rsi.asp) Values.')

    st.text('')
    st.text('')
    st.text('')
    st.markdown('NOTE: This Feature is only applicable for **NSE** Stocks.')

    def add_macd_and_rsi(df, stock_list):
        # calculate macf and signal line indicators
        for stock in stock_list:
            # calculate short term ema
            shortEMA = df[stock, 'Close'].ewm(span=12).mean()
            # calculate long term ema
            longEMA = df[stock, 'Close'].ewm(span=26).mean()
            # MACD calculation
            df[stock, 'MACD'] = shortEMA - longEMA
            # calculate signal
            df[stock, 'Signal'] = df[stock, 'MACD'].ewm(span=9).mean()
            # calculate RSI
            delta = df[stock, 'Close'].diff(1)
            delta.dropna(inplace=True)
            positive = delta.copy()
            negative = delta.copy()
            positive[positive > 0] = 0
            negative[negative < 0] = 0
            average_gain = positive.rolling(window=7).mean()
            average_loss = negative.rolling(window=7).mean()
            relative_strength = average_gain/average_loss
            df[stock, 'RSI'] = 100.0 - (100.0/(1.0+relative_strength))
            df = df.sort_index(axis=1)
            df.dropna(inplace=True)
        return df

    def get_macd_signal(df, stock_list):
        for stock in stock_list:
            # MACD Trade-
            buy_macd = []
            sell_macd = []
            flag_macd = -1

            for i in range(0, len(df)):
                if(df[stock, 'MACD'][i] > df[stock, 'Signal'][i]):
                    sell_macd.append(np.nan)
                    if(flag_macd != 1):
                        buy_macd.append(df[stock, 'Close'][i])
                        flag_macd = 1
                    else:
                        buy_macd.append(np.nan)
                elif(df[stock, 'MACD'][i] < df[stock, 'Signal'][i]):
                    buy_macd.append(np.nan)
                    if(flag_macd != 0):
                        sell_macd.append(df[stock, 'Close'][i])
                        flag_macd = 0
                    else:
                        sell_macd.append(np.nan)
                else:
                    buy_macd.append(np.nan)
                    sell_macd.append(np.nan)

            df[stock, 'MACD Buy Signal'] = buy_macd
            df[stock, 'MACD Sell Signal'] = sell_macd
            df = df.sort_index(axis=1)

        return df

    def get_rsi_signal(df, stock_list):
        for stock in stock_list:
            buy_rsi = []
            sell_rsi = []
            # rsi trade
            for i in range(0, len(df[stock, 'RSI'])):
                if(df[stock, 'RSI'][i] > 80):
                    buy_rsi.append(np.nan)
                    sell_rsi.append(df[stock, 'Close'][i])
                elif(df[stock, 'RSI'][i] < 20):
                    buy_rsi.append(df[stock, 'Close'][i])
                    sell_rsi.append(np.nan)
                else:
                    buy_rsi.append(np.nan)
                    sell_rsi.append(np.nan)

            df[stock, 'RSI Buy Signal'] = buy_rsi
            df[stock, 'RSI Sell Signal'] = sell_rsi
            df = df.sort_index(axis=1)

        return df

    def getStockList(x):
        return ticker_list[:x]

    def getMultipleStockData(stock_list, timeframe):
        timeSpan = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h']

        if timeframe in timeSpan:
            p = '1mo'
        else:
            p = '2y'
        df = yf.download(stock_list, interval=timeframe,
                         period=p, group_by='tickers')
        df.dropna(inplace=True)
        df.index = pd.to_datetime(df.index)
        return df

    st.sidebar.markdown(
        'The range of stocks is set according to market-capital(2021)')
    x = st.sidebar.slider("Enter no. of Stocks you want to analyze?", 2, 200)
    timeframes = ['1m', '2m', '5m', '15m', '30m', '60m',
                  '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    timeframe = st.sidebar.selectbox("Select Timeframe", timeframes, index=3)

    if st.button("Automate Macd+Rsi Trade"):
        stock_list = getStockList(x)
        df = getMultipleStockData(stock_list, timeframe)
        df = add_macd_and_rsi(df, stock_list)

        df = get_macd_signal(df, stock_list)
        df = get_rsi_signal(df, stock_list)

        ticker_names = []
        entry_prices = []
        stop_losses = []
        targets = []

        for stock in stock_list:
            n = len(df)
            entry = False
            for i in range(n-5, n):
                if(np.isnan(df[stock, 'MACD Buy Signal'][i]) == False and np.isnan(df[stock, 'RSI Buy Signal'][i]) == False):
                    entry = True
                    break

            if(entry):
                ticker_names.append(stock)
                entry_prices.append(df[stock, 'Close'][n-1])

                stop_loss = min(df[stock, 'Low'][n-2], df[stock, 'Low'][n-3])
                stop_losses.append(stop_loss)

                difference = df[stock, 'Close'][n-1]-stop_loss

                target = df[stock, 'Close'][n-1] + (2*difference)
                targets.append(target)

        trade_df = pd.DataFrame(list(zip(ticker_names, entry_prices, stop_losses, targets)),
                                columns=['Ticker Name', 'Entry Price', 'Stop Loss', 'Target'])

        st.markdown('List of Stocks-')
        st.write(trade_df)
