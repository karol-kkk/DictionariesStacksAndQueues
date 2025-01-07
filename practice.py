# 5.3
translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

# Prompt user to enter a word in English
word = input('Enter an English word: ').lower()

# Check if the word exists in the dictionary
if word in translations:
    print(f'Translation: {translations[word]}')
else:
    print('Translation not available.')

# 5.4
winter_semester = {
   "math": 60,
   "programming": 30,
   "history": 15
}

# Calculate the total number of hours
total_hours = sum(winter_semester.values())

# Print the total number of hours
print(f'The total number of hours in the winter semester is {total_hours}')

# 5.5
paragraph = "cat dog mouse cat rat cat mouse"

# Split the paragraph into individual words
words = paragraph.split()

# Initialize an empty dictionary to store word counts
word_count = {}

# Iterate over each word in the list of words
for word in words:
    # If the word is already in the dictionary, increment its count
    if word in word_count:
        word_count[word] += 1
    else:
        # If the word is not in the dictionary, add it with count 1
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f'{word}: {count}')

# 5.6
basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Combine the two dictionaries into a new dictionary
person = {**basic_data, **advanced_data}

# Print the contents of the 'person' dictionary
print(person)

# 5.7
# Function to return a list of hotel names separated by a comma
def hotel_list(hotels):
    return ', '.join([hotel['name'] for hotel in hotels])

# Function to calculate the average room price for a given list of hotels
def avg_price(hotels):
    total_price = sum(hotel['price'] for hotel in hotels)
    return round(total_price / len(hotels))

# Data for hotels in Krakow and Sopot
hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]

# Calculate and display the results
krakow_hotels = hotel_list(hotels_in_Krakow)
krakow_avg_price = avg_price(hotels_in_Krakow)

sopot_hotels = hotel_list(hotels_in_Sopot)
sopot_avg_price = avg_price(hotels_in_Sopot)

cheaper_hotels_in = []

# Determine which city has cheaper hotels
if krakow_avg_price < sopot_avg_price:
    cheaper_hotels_in.append("Krakow")
elif sopot_avg_price < krakow_avg_price:
    cheaper_hotels_in.append("Sopot")

# Print the results
print(f"Hotels in Krakow: {krakow_hotels}")
print(f"Average hotel price in Krakow: {krakow_avg_price}")
print(f"Hotels in Sopot: {sopot_hotels}")
print(f"Average hotel price in Sopot: {sopot_avg_price}")
print(f"Cheaper hotels in: {', '.join(cheaper_hotels_in)}")


# 5.8
# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total_cost = 0
for item, quantity in cart.items():
    if item in prices:
        total_cost += prices[item] * quantity

# Print the total cost
print(f"The total cost of the shopping cart is: ${total_cost:.2f}")


# 5.9
import csv
from collections import defaultdict

# File paths
vehicle_file = 'vehicle.txt'
province_file = 'province.csv'

# Step 1: Load province data into a dictionary
province_mapping = {}
with open(province_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        letter, name = row
        province_mapping[letter] = name

# Step 2: Initialize a dictionary to count vehicles per province
vehicle_count = defaultdict(int)

# Step 3: Process the vehicle registration numbers
with open(vehicle_file, 'r', encoding='utf-8') as file:
    for line in file:
        registration_number = line.strip()
        prefix = registration_number[0]  # Get the first letter
        if prefix in province_mapping:
            province = province_mapping[prefix]
            vehicle_count[province] += 1

# Step 4: Display the results
print("Vehicle count by province:")
for province, count in vehicle_count.items():
    print(f"{province}: {count}")

# 5.11
import json

# File name for voting data
file_name = 'voting.json'

# Read the contents of the JSON file
try:
    with open(file_name, 'r') as file:
        voting_data = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty dictionary
    voting_data = {}

# Vote for a person
person_name = input('Name of the person you are voting for: ')

# Increase the vote count for the person or add them if new
if person_name in voting_data:
    voting_data[person_name] += 1
else:
    voting_data[person_name] = 1

# Save voting data back to the JSON file
with open(file_name, 'w') as file:
    json.dump(voting_data, file, indent=4)

print(f"Vote recorded for {person_name}.")
print("Current voting results:", voting_data)

# 5.12
def reverse_string(text):
    # Initialize an empty stack
    stack = []
    
    # Push each character of the string onto the stack
    for char in text:
        stack.append(char)
    
    # Pop characters from the stack to form the reversed string
    reversed_text = ''
    while stack:
        reversed_text += stack.pop()
    
    return reversed_text

# Program to reverse any text entered from the keyboard
input_text = input("Enter the text to reverse: ")
reversed_text = reverse_string(input_text)
print(f"Reversed text: {reversed_text}")

# 5.16
import json

# Open the JSON file in read mode
with open('computer.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Print the computer data
for key, value in data.items():
    print(key, ':', value)

# 5.17
import json

# Open the JSON file in read mode
with open('cities.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    data = json.load(file)

# Print information about each city
for city in data:
    for key, value in city.items():
        print(key, ":", value)
    print()  # Print an empty line between cities

# 5.18
import json

# Open the JSON file in read mode
with open('dogs.json', 'r', encoding='utf-8') as file:
    # Load the data from the JSON file into a variable
    dogs = json.load(file)

# Print information about dogs younger than 5 years
for dog in dogs:
    if dog['age'] < 5:
        print(f"Name: {dog['name']}")
        print(f"Breed: {dog['breed']}")
        print(f"Age: {dog['age']}")
        print(f"Weight: {dog['weight_kg']} kg")
        print(f"Owner: {dog['owner']}")
        print(f"Vaccinated: {'Yes' if dog['vaccinated'] else 'No'}")
        print()  # Print an empty line between dogs

# 5.19
import json

# Function to load the reservation data from the JSON file
def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

# Function to calculate the number of rooms
def number_of_rooms(reservations):
    return len(reservations)

# Function to calculate the number of paid reservations
def number_of_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation['paid'])

# Function to calculate the number of unpaid reservations
def number_of_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation['paid'])

# Function to calculate the total value of paid reservations
def total_value_paid_reservations(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if reservation['paid'])

# Function to calculate the total value of unpaid reservations
def total_value_unpaid_reservations(reservations):
    return sum(reservation['nights'] * reservation['price_per_night'] for reservation in reservations if not reservation['paid'])

# Function to print the summary
def print_summary(reservations):
    print(f"Number of rooms: {number_of_rooms(reservations)}")
    print(f"Number of paid reservations: {number_of_paid_reservations(reservations)}")
    print(f"Number of unpaid reservations: {number_of_unpaid_reservations(reservations)}")
    print(f"Total value of paid reservations: ${total_value_paid_reservations(reservations):.2f}")
    print(f"Total value of unpaid reservations: ${total_value_unpaid_reservations(reservations):.2f}")

# Load the reservations data and print the summary
reservations = load_reservations('reservations.json')
print_summary(reservations)

#5.21
import json

# Create a dictionary describing the movie
favorite_movie = {
    "title": "Fast and Furious: Tokyo Drift",
    "release_year": 2006,
    "director": "Justin Lin",
    "genre": "Action, Crime, Drama",
    "main_cast": ["Lucas Black", "Bow Wow", "Nathalie Kelley"],
    "rating": 6.0
}

# Write the dictionary data to the favorite.json file
with open('favorite.json', 'w', encoding='utf-8') as file:
    json.dump(favorite_movie, file, ensure_ascii=False, indent=4)

print("Movie data has been written to favorite.json")

# 5.22
import json

# Dictionary to store product data
product = {}

# Read product data from the keyboard
product['name'] = input("Enter product name: ")
product['price'] = float(input("Enter product price (in format xx.xx): "))
paid_input = input("Has the product been paid for? (yes/no): ")

# Convert 'yes' or 'no' input to boolean
product['paid'] = True if paid_input.lower() == 'yes' else False

# Save product data to json file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, ensure_ascii=False, indent=4)

print("Product data has been saved to product.json")

# 5.23
import json

# Load the data from the euro.json file
with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Print the header
print("Date            Buying Rate     Selling Rate")
print("="*40)

# Iterate through the exchange rates and print the data
for rate in data['rates']:
    date = rate['effectiveDate']
    buying_rate = rate['mid']  
    selling_rate = rate['mid'] 
    print(f"{date}      {buying_rate:<15} {selling_rate}")




