new_sales = [5000, 2500, 1700]

# Append new sales
with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(f"{sale}\n")

# Reopen and print updated file
print("--- Task 3: Updated sales_data.txt ---")
with open("sales_data.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)

# Extra (Optional): Count and print total lines
with open("sales_data.txt", "r") as file:
    line_count = len(file.readlines())
print(f"Total number of lines after appending: {line_count}")