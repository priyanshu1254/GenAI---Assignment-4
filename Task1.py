sales = [1200, 450, 980, 1500, 3000]
with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(f"{sale}\n")

print("--- Task 1: Contents of sales_data.txt ---")
with open("sales_data.txt", "r") as file:
    print(file.read())
with open("sales_data_comma.txt", "w") as file:
    file.write(", ".join(map(str, sales)))