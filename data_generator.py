import csv
import random
from datetime import datetime, timedelta

def generate_data():
    # 1. Setup the ingredients
    models = ["iPhone 15", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15 Pro Max"]
    filename = "iphone_prices.csv"
    
    # 2. Create the list of data
    rows = []
    headers = ["Date", "Model", "Price", "Monthly_Payment", "Value_Score"]
    
    print(f"🎲 Generating 20 rows of mock data...")

    for i in range(20):
        # Pick a random date within the last 30 days
        days_ago = random.randint(0, 30)
        date_obj = datetime.now() - timedelta(days=days_ago)
        date_str = date_obj.strftime("%Y-%m-%d")
        
        # Pick a random model
        model = random.choice(models)
        
        # Pick a random price (integer)
        price = random.randint(800, 1200)
        
        # Calculate monthly payment (Price / 24 months), rounded to 2 decimals
        monthly_payment = round(price / 24, 2)
        
        # Generate a random value score (1.0 to 10.0)
        value_score = round(random.uniform(1.0, 10.0), 1)
        
        rows.append([date_str, model, price, monthly_payment, value_score])

    # 3. Write it to a CSV file (The "Excel" sheet)
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers) # Write the top row
        writer.writerows(rows)   # Write the data

    print(f"✅ Data Generated! Check '{filename}' in your file list.")

if __name__ == "__main__":
    generate_data()