# 📈 BIST Analyzer

Technical indicator-based analysis tool for Turkish BIST stocks using Python.

---

## 🚀 Features

- Pulls historical price data of BIST stocks via Yahoo Finance
- Calculates and visualizes:
  - EMA13 (Exponential Moving Average)
  - SMA50 (Simple Moving Average)
  - RSI(14) (Relative Strength Index)
  - MACD + Signal Line
- Generates visual output (`plot.png`)
- Handles missing data automatically
- User inputs symbol + date range dynamically

---

## 🛠️ Built With

- Python
- yfinance
- pandas
- matplotlib

---

## 📌 Notes

- BIST stock symbols must be in .IS format (e.g. FROTO → FROTO.IS)
- Works for any Yahoo Finance-supported Turkish stock
- Ideal for portfolio & technical signal demonstration

---

## ✨ Future Improvements

- Web interface with Streamlit
- Automated alerts and email notifications
- Additional indicators (e.g. Stochastic, Bollinger Bands)
