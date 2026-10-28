print("--- Task 5: Product Entry ---")
products = []
for i in range(1, 4):
    name = input(f"Enter product {i} name: ")
    price = input(f"Enter product {i} price: ")
    products.append((name, price))
with open("products.txt", "w") as file:
    for name, price in products:
        file.write(f"{name} | {price}\n")
print("\n--- Contents of products.txt ---")
with open("products.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" | ")
        if len(parts) == 2:
            print(f"Product: {parts[0]:<15} Price: ${parts[1]}")