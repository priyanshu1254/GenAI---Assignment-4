import os

print("--- Task 6: Safe File Reader ---")
filename = input("Enter the filename to open: ")

# Check if file exists using os.path.exists()
if os.path.exists(filename):
    with open(filename, "r") as file:
        print("\n--- File Contents ---")
        print(file.read())
else:
    print("File not found. Please check the filename.")