# ************************************************************************** #
#                                                                            #
#    BIST Stock Analysis                                                     #
#                                                                            #
#    By: Yusuf Emre OZDEN | <yusufemreozdenn@gmail.com>                      #
#                                                                            #                                            
#    https://GitHub.com/yusufemreozden                                       #
#    https://linkedIn.com/in/yusufemreozden                                  #
#                                                                            #
# ************************************************************************** #

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# === Kullanıcı Girişi ===
ticker = input("Borsa İstanbul hisse senedi sembolünü girin (örnek: TUPRS): ").upper()
start = input("Veri için başlangıç tarihini girin (örnek: 2019-01-01): ")
end = input("Veri için bitiş tarihini girin (örnek: 2025-03-28): ")

# BIST için .IS kocu ekleme
if not ticker.endswith(".IS"):
    ticker += ".IS"

# === Veri Çekme ===
df = yf.download(ticker, start=start, end=end)

if df.empty:
    print("Veri alınamadı. Lütfen sembolü ve tarihleri kontrol edin.")
    exit()

# === Teknik Göstergeler ===

# RSI (65-40)
df["RSI"] = df["Close"].rolling(window=14).apply(
    lambda x: 100 - (100 / (1 + (x.diff().where(x.diff() > 0, 0).sum() / abs(x.diff().where(x.diff() < 0, 0).sum()))))
)

# EMA & SMA (13-50)
df["EMA13"] = df["Close"].ewm(span=13, adjust=False).mean()
df["SMA50"] = df["Close"].rolling(window=50).mean()

# MACD (manuel)
df["EMA12"] = df["Close"].ewm(span=12, adjust=False).mean()
df["EMA26"] = df["Close"].ewm(span=26, adjust=False).mean()
df["MACD"] = df["EMA12"] - df["EMA26"]
df["MACD_signal"] = df["MACD"].ewm(span=9, adjust=False).mean()


df.dropna(inplace=True)

# === Grafikler ===
plt.figure(figsize=(14, 10))

# Fiyat + EMA/SMA
plt.subplot(3, 1, 1)
plt.plot(df.index, df["Close"], label="Close", linewidth=1.5)
plt.plot(df.index, df["EMA13"], label="EMA13", color="orange", linestyle="--")
plt.plot(df.index, df["SMA50"], label="SMA50", color="green", linestyle="--")
plt.title(f"{ticker} Fiyat + EMA13 & SMA50")
plt.legend()

# RSI
plt.subplot(3, 1, 2)
plt.plot(df.index, df["RSI"], label="RSI", color="purple")
plt.axhline(65, color="red", linestyle="--")
plt.axhline(40, color="green", linestyle="--")
plt.title("RSI (14)")
plt.legend()

# MACD
plt.subplot(3, 1, 3)
plt.plot(df.index, df["MACD"], label="MACD", color="blue")
plt.plot(df.index, df["MACD_signal"], label="Signal", color="orange")
plt.title("MACD")
plt.legend()

plt.tight_layout()
plt.savefig("plot.png")
plt.show()