import json
import webbrowser

# Taking input from user
source = input("Enter source: ")
destination = input("Enter destination: ")

# Creating JSON data
data = {
    "source": source,
    "destination": destination
}

# Convert Python dictionary to JSON
json_data = json.dumps(data, indent=4)

# Display JSON data
print("\nJSON Data:")
print(json_data)

# Create Google Maps routing URL
source_url = source.replace(" ", "+")
destination_url = destination.replace(" ", "+")

url = f"https://www.google.com/maps/dir/{source_url}/{destination_url}"

# Open Google Maps in browser
webbrowser.open(url)