# error_example.py

"""
⚠️ Tutorial 6: Error Handling in Python
This script shows beginners how to catch and handle errors using try/except.
"""

# Step 1: Division with error handling
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print(f"✅ Result: {x} / {y} = {result}")
except ValueError:
    print("❌ Please enter valid numbers!")
except ZeroDivisionError:
    print("❌ Division by zero is not allowed!")

# Step 2: File handling with error checking
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("📂 File not found. Creating it now...")
    with open("nonexistent.txt", "w") as f:
        f.write("Hello from Tutorial 6!")
    print("✅ nonexistent.txt created!")
