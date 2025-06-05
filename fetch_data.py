import yfinance as yf
import pandas as pd

def get_gold_data() -> pd.DataFrame:
    """
    Fetches XAU/USD (gold) daily price data from Yahoo Finance.
    """
    df = yf.download("XAUUSD=X", period="6mo", interval="1d")
    df = df.rename(columns={"Close": "close"})
    df = df[["close"]]  # فقط ستون قیمت نهایی
    df.index.name = "date"
    return df
