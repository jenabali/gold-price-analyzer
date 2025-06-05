import os
from typing import Optional
import requests
import pandas as pd

def get_gold_data(api_key: Optional[str] = None) -> pd.DataFrame:
    """Fetches daily gold price data (XAU/USD) from Alpha Vantage."""
    api_key = api_key or os.getenv("ALPHA_VANTAGE_API_KEY", "N9VU8OJ7R2SB90JC")
    url = (
        "https://www.alphavantage.co/query"
        "?function=FX_DAILY&from_symbol=XAU&to_symbol=USD&outputsize=compact"
        f"&apikey={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)
        raise

    raw_json = response.json()
    if "Time Series FX (Daily)" not in raw_json:
        print("⚠️ API response did not contain expected data:", raw_json)
        raise ValueError("No valid data in API response")
    else:
        print("✅ Data received successfully.")

    data = raw_json["Time Series FX (Daily)"]
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(list(data.keys())),
            "close": [float(v["4. close"]) for v in data.values()],
        }
    ).sort_values("date")
    df.set_index("date", inplace=True)
    return df
