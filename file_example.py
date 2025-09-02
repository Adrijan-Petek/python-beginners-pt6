# file_example.py

"""
📂 Tutorial 2: Working with Files
This script shows how to write and read text files.
"""

# Write to a file
with open("hello.txt", "w") as f:
    f.write("Hello, file world!\n")

print("✅ hello.txt created!")

# Read from the file
with open("hello.txt", "r") as f:
    content = f.read()

print("\n📂 File content:")
print(content)
