print("--- Task 2.1: Read using .read() ---")
with open("sales_data.txt", "r") as file:
    content = file.read()
    print(content)

print("--- Task 2.2: Read first line using .readline() ---")
with open("sales_data.txt", "r") as file:
    first_line = file.readline()
    print("First line:", first_line.strip())

print("\n--- Task 2.3: Read all lines using .readlines() and convert to integer list ---")
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales_list = [int(line.strip()) for line in lines if line.strip()]

print("Converted Integer List:", sales_list)