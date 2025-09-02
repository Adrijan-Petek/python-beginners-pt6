# json_example.py

"""
🗂️ Tutorial 4: Working with JSON in Python
This script shows beginners how to save and load data using JSON format.
"""

import json

# Step 1: Create a Python dictionary
student = {
    "name": "Alice",
    "age": 14,
    "grades": ["A", "B+", "A-"],
    "active": True
}

# Step 2: Write dictionary to a JSON file
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

print("✅ student.json created!")

# Step 3: Read JSON back into Python
with open("student.json", "r") as f:
    loaded_student = json.load(f)

print("\n📂 Loaded student.json:")
print(loaded_student)

# Step 4: Access specific values
print(f"\n🔎 {loaded_student['name']} is {loaded_student['age']} years old.")
print(f"Grades: {', '.join(loaded_student['grades'])}")
