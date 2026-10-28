# Read values and convert to integers
with open("sales_data.txt", "r") as file:
    sales_values = [int(line.strip()) for line in file if line.strip()]

# Calculate statistics
total_sales = sum(sales_values)
highest_sale = max(sales_values)
lowest_sale = min(sales_values)
average_sale = total_sales / len(sales_values)

# Print Summary Report
print("--- Task 4: Summary Report ---")
print(f"Total Sales: {total_sales}")
print(f"Highest Sale: {highest_sale}")
print(f"Lowest Sale: {lowest_sale}")
print(f"Average Sale: {average_sale:.2f}")