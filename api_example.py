# api_example.py

"""
🌐 Tutorial 5: Working with APIs in Python
This script shows beginners how to fetch data from a public API and handle JSON.
"""

import requests

# Step 1: Choose a public API (cat facts 🐱)
url = "https://catfact.ninja/fact"

# Step 2: Send a GET request
response = requests.get(url)

# Step 3: Check response status
if response.status_code == 200:
    print("✅ Successfully fetched data from API!")
    data = response.json()  # Parse JSON response

    # Step 4: Access values
    print("\n📂 Full API Response:")
    print(data)

    print(f"\n🐱 Fun Cat Fact: {data['fact']}")
else:
    print("❌ Failed to fetch data. Status code:", response.status_code)
