import os
import time
from datetime import datetime
import requests

def get_bitcoin_data():
    """Fetches live Bitcoin data from the trusted Coinbase API."""
    url = "https://coinbase.com"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Coinbase returns a nested dictionary with the raw price string
        price_str = data.get("data", {}).get("amount", "0.0")
        return {"usd": float(price_str)}
    except requests.exceptions.RequestException:
        return None

def clear_screen():
    """Clears the terminal screen for a clean dashboard look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Initializing Unblocked Bitcoin Live Price Tracker...")
    
    while True:
        data = get_bitcoin_data()
        clear_screen()
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("=" * 45)
        print(f" 🪙  LIVE BITCOIN PRICE TRACKER (COINBASE API)")
        print(f" Last Updated: {current_time}")
        print("=" * 45)
        
        if data:
            price = data.get("usd", 0.0)
            print(f" Current Price:  ${price:,.2f} USD")
        else:
            print(" ❌ Error: Still unable to fetch data.")
            print("    Checking terminal internet connection...")
            
        print("=" * 45)
        print(" Press Ctrl+C to exit. Refreshing every 10s...")
        
        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTracker stopped. Happy Hacking!")
