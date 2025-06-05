import yfinance as yf
import pandas as pd

def get_gold_data() -> pd.DataFrame:
    """
    Fetches gold price data from Yahoo Finance (GC=F = Gold Futures).
    """
    df = yf.download("GC=F", period="6mo", interval="1d")
    if df.empty:
        print("❌ دریافت قیمت طلا با شکست مواجه شد.")
        return pd.DataFrame()
    
    df = df.rename(columns={"Close": "close"})
    df = df[["close"]]
    df.index.name = "date"
    return df
