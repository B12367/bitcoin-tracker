# 🪙 Bitcoin Live Price Tracker

A lightweight, terminal-based Python script that tracks the live price of Bitcoin in real-time. It fetches data directly from the free CoinGecko API and updates automatically every 30 seconds with a clean dashboard interface.

## ✨ Features
* **Live Prices:** Pulls current market prices in USD.
* **24-Hour Trends:** Displays price changes with directional visual indicators (🔺/🔻).
* **Automatic Refresh:** The dashboard updates on a continuous loop without manual input.
* **No API Keys Needed:** Uses open-source, public endpoints.

## 🚀 How to Run It Locally

### 1. Prerequisites
Make sure you have Python installed on your computer. You will also need to install the network requests library:
```bash
pip install requests
```

### 2. Execution
Run the script directly inside your terminal or command prompt:
```bash
python bitcoin_tracker.py
```

## 🛠️ Built With
* Python 3
* [CoinGecko API](https://coingecko.com) - Free crypto market data
* Requests Library - Elegant and simple HTTP requests for Python
