import os
import time
from datetime import datetime
import requests

def get_bitcoin_data():
    """Fetches live Bitcoin data from the Coingecko API."""
    url = "https://coingecko.com"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_last_updated_at": "true"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("bitcoin", {})
    except requests.exceptions.RequestException:
        return None

def clear_screen():
    """Clears the terminal screen for a clean dashboard look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Initializing Bitcoin Live Price Tracker...")
    
    while True:
        data = get_bitcoin_data()
        clear_screen()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("=" * 45)
        print(f" 🪙  LIVE BITCOIN PRICE TRACKER")
        print(f" Last Updated: {current_time}")
        print("=" * 45)
        
        if data:
            price = data.get("usd", 0.0)
            change_24h = data.get("usd_24h_change", 0.0)
            
            # Choose a directional arrow and format the percentage
            direction = "🔺" if change_24h >= 0 else "🔻"
            
            print(f" Current Price:  ${price:,.2f} USD")
            print(f" 24h Change:     {direction} {change_24h:+.2f}%")
        else:
            print(" ❌ Error: Unable to fetch live price data.")
            print("    Retrying in the next cycle...")
            
        print("=" * 45)
        print(" Press Ctrl+C to exit. Refreshing every 30s...")
        
        # Wait 30 seconds before the next API pull
        time.sleep(30)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTracker stopped. Happy Hacking!")
