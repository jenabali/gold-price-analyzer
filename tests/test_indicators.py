import pandas as pd
from indicators import rsi


def test_rsi_all_uptrend():
    prices = pd.Series(range(1, 16))
    r = rsi(prices)
    # After 14 periods of uptrend, RSI should be 100
    assert r.iloc[14] == 100
