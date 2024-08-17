"""Module providing utils"""

import datetime as dt
import yfinance as yf
import pandas as pd


def get_stock_data(ticker, period="max", weekly=False, offset=12) -> pd.DataFrame:
    """get stock data from yfinance and add some technical indicators and other meta"""
    tick = yf.Ticker(ticker)
    df = tick.history(period=period, interval="1d" if not weekly else "1wk")
    if df.empty:
        raise Exception(f"No data found for ticker: {ticker}")
    df.index.name = "date"
    df = df.tz_localize(None)
    df.columns = [col.lower() for col in df.columns]
    df["ticker"] = ticker.upper()
    df["sma10"] = df["close"].rolling(10).mean()
    df["sma20"] = df["close"].rolling(20).mean()
    df["sma30"] = df["close"].rolling(30).mean()
    df["ema9"] = df["close"].ewm(span=9, adjust=False).mean()
    df["ema21"] = df["close"].ewm(span=21, adjust=False).mean()
    df["ema65"] = df["close"].ewm(span=65, adjust=False).mean()
    df["sma50"] = df["close"].rolling(50).mean()
    df["adr20"] = (df["high"] / df["low"] - 1).ewm(span=20, adjust=False).mean()
    df["volume_sma50"] = df["volume"].rolling(50).mean()
    df["volume_sma10"] = df["volume"].rolling(10).mean()
    df["rvol"] = df["volume"] / df["volume_sma50"]
    try:
        meta = tick.info
        df["short_name"] = meta["shortName"].replace(".", "")
        df["industry"] = meta["industry"]
        df["sector"] = meta["sector"]
    except:
        pass
    today = dt.datetime.now().date()
    start_date = today - pd.offsets.DateOffset(months=offset)
    df = df[(df.index >= start_date)]
    if df.empty or len(df) == 0:
        raise Exception(f"No data found for ticker: {ticker}")
    return df


def get_meta_yfinance(ticker: str) -> dict:
    """get stocke meta data from yfinance"""
    return yf.Ticker(ticker).info


if __name__ == "__main__":
    get_stock_data("NVDA")
