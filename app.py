import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=720)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

st.title('Time Series Analysis - Stocks')

custom_stock = st.sidebar.text_input('Enter Stock Ticker Symbol:')
if custom_stock:
    custom_stock = custom_stock.upper()


    data = yf.download(custom_stock, 
                       start=start_date, 
                       end=end_date, 
                       progress=False)

    

    # Line plot
    fig_line = px.line(data, x=data.index, y="Close", title="Time Series Analysis (Line Plot)")
    st.plotly_chart(fig_line)

    # Candlestick chart
    fig_candlestick = go.Figure(data=[go.Candlestick(x=data.index,
                                                     open=data["Open"],
                                                     high=data["High"],
                                                     low=data["Low"],
                                                     close=data["Close"])])
    fig_candlestick.update_layout(title="Time Series Analysis (Candlestick Chart)", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_candlestick)

    # Bar plot
    fig_bar = px.bar(data, x=data.index, y="Close", title="Time Series Analysis (Bar Plot)")
    st.plotly_chart(fig_bar)

    # Candlestick chart with buttons and slider
    fig_slider = go.Figure(data=[go.Candlestick(x=data.index,
                                                open=data["Open"],
                                                high=data["High"],
                                                low=data["Low"],
                                                close=data["Close"])])
    fig_slider.update_layout(title="Time Series Analysis (Candlestick Chart with Buttons and Slider)")

    fig_slider.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ]),
            bgcolor='rgba(128, 128, 128, 0)',
            activecolor='rgba(0, 0, 0, 0)',
            font=dict(color='white')
        )
    )
    st.plotly_chart(fig_slider)
