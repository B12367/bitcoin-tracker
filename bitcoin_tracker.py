import os
import time
import random
from datetime import datetime

def generate_simulated_price(last_price):
    """Generates a realistic price fluctuation."""
    percent_move = random.uniform(-0.002, 0.002)
    return round(last_price * (1 + percent_move), 2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Setup starting benchmarks
    current_price = 92450.00
    initial_price = current_price
    session_high = current_price
    session_low = current_price
    alert_price = 92550.00
    
    # FIX: Pre-populate history with data so the graph works instantly on launch!
    history = [current_price]
    for _ in range(5):
        history.append(generate_simulated_price(history[-1]))
    current_price = history[-1]
    
    while True:
        clear_screen()
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # 1. Update High / Low Tracking
        if current_price > session_high:
            session_high = current_price
        if current_price < session_low:
            session_low = current_price
            
        # 2. Track history for the visual sparkline chart (Keep last 10 ticks)
        history.append(current_price)
        if len(history) > 10:
            history.pop(0)
            
        # 3. Calculate Trends
        total_change_pct = ((current_price - initial_price) / initial_price) * 100
        direction = "🔺" if total_change_pct >= 0 else "🔻"
        
        # Build the visual sparkline string using arrows
        sparkline = ""
        for i in range(1, len(history)):
            if history[i] > history[i-1]:
                sparkline += "↗️ "
            else:
                sparkline += "↘️ "
        
        # Print the Upgraded Dashboard
        print("=" * 50)
        print(f" 🪙  PRO BITCOIN TRACKER & SIMULATOR")
        print(f" Time: {current_time} | Status: 🔒 Secure Local Mode")
        print("=" * 50)
        print(f" 💵 CURRENT PRICE:  ${current_price:,.2f} USD")
        print(f" 📊 Session Change: {direction} {total_change_pct:+.4f}%")
        print(f" 📈 Visual Trend:   {sparkline}")
        print("-" * 50)
        print(f" 🔼 Session High:   ${session_high:,.2f}")
        print(f" 🔽 Session Low:    ${session_low:,.2f}")
        print(f" 🎯 Alert Target:   ${alert_price:,.2f}")
        print("=" * 50)
        
        # 4. Trigger the Alert Check
        if current_price >= alert_price:
            print(" 🔥 🚨 ALERT: PRICE HAS SURPASSED TARGET PRICE! 🚨 🔥")
            print("=" * 50)
            
        print(" Press Ctrl+C to exit. Ticking every 2s...")
        
        # Step forward
        current_price = generate_simulated_price(current_price)
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTracker closed safely. Happy Hacking!")
