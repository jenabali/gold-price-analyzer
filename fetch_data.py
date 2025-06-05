import os
from typing import Optional
import requests
import pandas as pd


def get_gold_data(api_key: Optional[str] = None) -> pd.DataFrame:
    """Fetches daily gold price data (XAU/USD) from Alpha Vantage."""
    api_key = api_key or os.getenv("ALPHA_VANTAGE_API_KEY", "demo")
    url = (
        "https://www.alphavantage.co/query"
        "?function=FX_DAILY&from_symbol=XAU&to_symbol=USD&outputsize=compact"
        f"&apikey={api_key}"
    )
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    print("Full API Response:", response.json())
    print("✅ درخواست انجام شد.")
    data = response.json().get("Time Series FX (Daily)", {})
    if not data:
        raise ValueError("No data returned from API")
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(list(data.keys())),
            "close": [float(v["4. close"]) for v in data.values()],
        }
    ).sort_values("date")
    df.set_index("date", inplace=True)
    return df
