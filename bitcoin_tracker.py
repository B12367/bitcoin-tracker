import os
import time
import random
from datetime import datetime

def generate_simulated_price(last_price):
    """Generates a realistic price fluctuation without using the internet."""
    # Mimics a tiny market move between -0.15% and +0.15%
    percent_move = random.uniform(-0.0015, 0.0015)
    new_price = last_price * (1 + percent_move)
    return round(new_price, 2)

def clear_screen():
    """Clears the terminal screen for a clean dashboard look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Starting price benchmark
    current_price = 92450.00 
    initial_price = current_price
    
    print("Initializing Offline Bitcoin Simulator Engine...")
    time.sleep(1)
    
    while True:
        clear_screen()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Calculate the total change since the script started
        total_change_pct = ((current_price - initial_price) / initial_price) * 100
        direction = "🔺" if total_change_pct >= 0 else "🔻"
        
        print("=" * 45)
        print(f" 🪙  OFFLINE BITCOIN SIMULATOR (SCHOOL SAFE)")
        print(f" Last Dynamic Tick: {current_time}")
        print("=" * 45)
        print(f" Current Price:  ${current_price:,.2f} USD")
        print(f" Session Change: {direction} {total_change_pct:+.4f}%")
        print("=" * 45)
        print(" 🔒 Connected via: Local Simulation Matrix")
        print(" Press Ctrl+C to exit. Ticking every 3s...")
        
        # Update price and wait 3 seconds before next tick
        current_price = generate_simulated_price(current_price)
        time.sleep(3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulator stopped safely. Happy Hacking!")
