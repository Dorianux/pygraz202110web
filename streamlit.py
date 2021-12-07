# dummy example for streamlit
# .. just fetch some data and visualize (with minimal approach)

import streamlit as st
import pandas as pd
import numpy as np

from coinpaprika import client as Coinpaprika

client = Coinpaprika.Client()


# headline
st.title("Just a demo")


st.header("Coins available")
show_coins = st.checkbox("Show Top 10 coins")

if show_coins:
    coins = client.coins()
    data = pd.DataFrame(coins).values[:10]
    st.table(data=data)


# List some values and select
st.header("One coin")
coin = st.radio("Pick a coin", ("", "btc-bitcoin", "eth-ethereum", "ada-cardano"))

if coin:
    coindata = client.ticker(coin)


# Columns are available
col1, col2 = st.columns(2)

with col1:
    st.subheader("Show details")
    info = st.checkbox("show ?")

with col2:
    st.subheader("Resulting Data")
    if coin and info:
        st.write(coindata)


# charting
st.header("Todays Value")

diagram = st.checkbox("Show chart")

if diagram and coin:
    # getdata
    coin_hist = client.historical(coin, start="2021-12-01T00:00:00Z")

    # to np
    history = pd.DataFrame(
        coin_hist,
        columns=["timestamp", "price", "volume_24h", "market_cap"],
    ).values

    # rip off unwanted info
    history = history[:, 1]

    # chart
    st.line_chart(history)
