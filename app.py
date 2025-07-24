
# app.py

import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="📈 Stock Market Analysis", layout="wide")

st.title("📊 Stock Market Analysis Dashboard")
st.markdown("Upload your CSV or analyze live data using Yahoo Finance API.")

# Option 1: Upload CSV file
uploaded_file = st.file_uploader("Upload Stock Market CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.write("### Data Preview", df.head())
    
    # Line Plot of Close Price
    if 'Close' in df.columns:
        st.write("### Closing Price Over Time")
        fig, ax = plt.subplots()
        ax.plot(df['Close'], label="Close Price")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)

# Option 2: Use Yahoo Finance live data
st.write("---")
st.subheader("📡 Or Analyze a Live Stock (via yfinance)")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, INFY):", "AAPL")

if st.button("Fetch Data"):
    data = yf.download(ticker, period="6mo", interval="1d")
    st.write(f"### {ticker} Stock Price (Last 6 Months)", data.tail())
    
    # Plotting
    st.line_chart(data['Close'])
    
    # Simple Moving Average
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    st.write("### Moving Averages (20 & 50 Days)")
    fig2, ax2 = plt.subplots()
    ax2.plot(data['Close'], label="Close Price")
    ax2.plot(data['SMA_20'], label="SMA 20", linestyle='--')
    ax2.plot(data['SMA_50'], label="SMA 50", linestyle='--')
    ax2.legend()
    st.pyplot(fig2)
