prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask for discount percentage
discount_pct = float(input("Enter discount percentage (e.g., 10 for 10%): "))

discounted_prices = []

# Write report to file
with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")
    file.write("-" * 45 + "\n")
    
    for item, orig_price in prices.items():
        disc_price = orig_price * (1 - discount_pct / 100)
        discounted_prices.append(disc_price)
        file.write(f"{item} | {orig_price} | {disc_price:.2f}\n")
    
    # Extra (Optional): Summary at the bottom
    file.write("-" * 45 + "\n")
    file.write(f"Total Items: {len(prices)}\n")
    file.write(f"Average Discounted Price: {sum(discounted_prices)/len(discounted_prices):.2f}\n")

# Read and print to terminal
print("\n--- Task 7: Contents of discount_report.txt ---")
with open("discount_report.txt", "r") as file:
    print(file.read())