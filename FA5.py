# Ask the user to enter 5 travel destinations
print("Please enter your 5 travel destinations:")

destinations = []  # list to store the destinations

for i in range(5):
    destination = input(f"Destination {i + 1}: ")
    destinations.append(destination)

# Display the original travel itinerary
print("\nOriginal Travel Itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")

# Update the 2nd and 5th destinations
print("\nLet's update your 2nd and 5th destinations.")

new_second = input("Enter a new destination for position 2: ")
new_fifth = input("Enter a new destination for position 5: ")

# Update using array indices
destinations[1] = new_second
destinations[4] = new_fifth

# Display the updated travel itinerary
print("\nUpdated Travel Itinerary:")
for i in range(5):
    print(f"{i + 1}. {destinations[i]}")
