# csv_example.py

"""
📊 Tutorial 3: Working with CSV Files
This script shows how to write and read CSV data.
"""

import csv

# Step 1: Write CSV
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["Alice", 14, "A"])
    writer.writerow(["Bob", 15, "B+"])

print("✅ students.csv created!")

# Step 2: Read CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    print("\n📂 CSV content:")
    for row in reader:
        print(row)
