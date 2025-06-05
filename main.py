import matplotlib.pyplot as plt
import pandas as pd

from fetch_data import get_gold_data
from indicators import ema, rsi


def plot_data(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['close'], label='Price')
    plt.plot(df.index, df['ema20'], label='EMA 20')
    plt.plot(df.index, df['ema50'], label='EMA 50')
    plt.title('XAU/USD')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.show()


def main() -> None:
    df = get_gold_data(api_key="N9VU8OJ7R2SB90JC")
    df['ema20'] = ema(df['close'], span=20)
    df['ema50'] = ema(df['close'], span=50)
    df['rsi'] = rsi(df['close'])

    latest_rsi = df['rsi'].iloc[-1]
    if latest_rsi < 30:
        print('خرید احتمالی')
    elif latest_rsi > 70:
        print('فروش احتمالی')
    else:
        print('سیگنال خنثی')

    plot_data(df)


if __name__ == '__main__':
    main()
