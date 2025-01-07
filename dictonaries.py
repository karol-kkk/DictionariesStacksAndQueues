## 1.3
mobile = {
    "Brand": "Samsung",
    "Model": "Galaxy S8",
    "OS": "Android",
    "Storage": "64 GB",
    "RAM": "4 GB",
    "Camera": "12 MP"
}

for key, value in mobile.items():
    print(f"{key} : {value}")

## 1.4
# Define the dictionary
person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming", "excursions"],
   "married": True,
   "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Display name
print(f"Name: {person['name']}")

# Display hobby
print(f"Hobby: {person['hobby']}")

# Display the entire contents of the dictionary
print("\nEntire dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Change surname to 'Nowak'
person["surname"] = "Nowak"

# Change person's marriage status
person["married"] = False

# Add gender: 'male'
person["gender"] = "male"

# Add a new hobby: 'bicycle'
person["hobby"].append("bicycle")

# Add work phone to existing phones: '313131444'
person["phone"]["work"] = "313131444"

# Display the entire contents of the dictionary again
print("\nUpdated dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")


## 1.5
# Define the list of dictionaries
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Italy", "population": 60000000},
    {"name": "Spain", "population": 47000000}
]

# Print the header
print("COUNTRY      POPULATION")

# Iterate over the list and print each country's name and population
for country in countries:
    print(f"{country['name']}   {country['population']}")

## 1.6
# Define the phone book
phone_book = {
   'John': '555-1234',
   'David': '555-5678',
   'Bob': '555-8765',
   'Charlie': '555-4321',
   'Diana': '555-9876',
   'Eve': '555-6543',
   'Frank': '555-3456',
   'Grace': '555-7890',
   'Hank': '555-1111',
   'Ivy': '555-2222',
   'Jack': '555-3333',
   'Daniel': '555-4444',
   'Liam': '555-5555',
   'Mia': '555-6666',
   'Nina': '555-7777',
   'Oscar': '555-8888',
   'Paul': '555-9999',
   'Dominic': '555-1010',
   'Rachel': '555-2020',
   'Sam': '555-3030'
}

# Iterate over the phone book and print details for names starting with 'D'
print("Details of people whose names start with 'D':")
for name, phone in phone_book.items():
    if name.startswith('D'):
        print(f"{name}: {phone}")

## 1.7
# Define the product data
store_inventory = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# Print the list of products and their quantities
print("List of products and quantities:")
for product, quantity in store_inventory.items():
    print(f"{product}: {quantity}")

# Calculate the total number of products in the store
total_products = sum(store_inventory.values())

# Print the total number of products
print(f"\nTotal number of products in the store: {total_products}")

## 1.8
# Define the price list
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

# Print the list of products and their prices before the discount
print("Products and prices before the discount:")
for product, price in price_list.items():
    print(f"{product}: ${price:.2f}")

# Calculate the total value of products before the discount
total_before_discount = sum(price_list.values())
print(f"\nTotal value of products before the discount: ${total_before_discount:.2f}")

# Apply the 10% discount and round prices to two decimal places
discounted_price_list = {product: round(price * 0.9, 2) for product, price in price_list.items()}

# Print the list of products and their prices after the 10% discount
print("\nProducts and prices after the 10% discount:")
for product, price in discounted_price_list.items():
    print(f"{product}: ${price:.2f}")

# Calculate the total value of products after the discount
total_after_discount = sum(discounted_price_list.values())
print(f"\nTotal value of products after the discount: ${total_after_discount:.2f}")


## 2.2
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
unique_emails = set(emails)  # Removes duplicates
print(unique_emails)

# 2.3
all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

absent_students = all_students - attended_students   #Difference
print(absent_students)

# 2.4
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = emails_received & spam_list  # Intersection
print("Spam emails:", spam_emails)

# 2.5
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = contacts_A | contacts_B  # Union
print("Merged contacts:", merged_contacts)

# 2.6
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = required_permissions.issubset(user_permissions)  # Check if required_permissions is a subset of user_permissions
print(has_permissions)  # Will return False because "execute" is missing.

# 3.3
import queue

def brackets_ok(expression):
    # Initialize an empty stack
    stack = queue.LifoQueue()

    # Define a dictionary for matching pairs
    matching_bracket = {')': '(', '}': '{', ']': '['}

    # Traverse through each character in the expression
    for char in expression:
        if char in "({[":
            # If it is an opening bracket, push it to the stack
            stack.put(char)
        elif char in ")}]":
            # If it is a closing bracket, check for matching opening bracket
            if stack.empty():
                # If the stack is empty, no opening bracket for the closing one
                return False
            top = stack.get()
            if top != matching_bracket[char]:
                # If the top of the stack doesn't match the closing bracket
                return False
    
    # If the stack is empty, all brackets are balanced; otherwise, they are not
    return stack.empty()

# Expressions to check
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

# Check each expression
if brackets_ok(expression1):
    print("Expression 1 brackets are ok")
else:
    print("Expression 1 brackets are not correct")

if brackets_ok(expression2):
    print("Expression 2 brackets are ok")
else:
    print("Expression 2 brackets are not correct")

if brackets_ok(expression3):
    print("Expression 3 brackets are ok")
else:
    print("Expression 3 brackets are not correct")

# 3.4
import queue

def convert_to_binary(number):
    # Create a stack to store remainders
    stack = queue.LifoQueue()
    
    # Perform the division and store remainders in the stack
    while number > 0:
        remainder = number % 2
        stack.put(remainder)
        number = number // 2
    
    # Pop elements from the stack to display the binary number
    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())
    
    return binary_number

# Sample result for number 18
number = 18
binary_result = convert_to_binary(number)

# Displaying the result
print(f"The binary representation of {number} is: {binary_result}")

# 4.2
import queue

# Creates a queue for files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')
    
    if menu == '1':
        file_name = input('Enter file name to print: ')
        # Add the new file to the end of the queue
        files_to_print.put(file_name)
        print(f'File {file_name} added to the print queue.')

    elif menu == '2':
        if not files_to_print.empty():
            # Print file from the front of the queue
            file_to_print = files_to_print.get()
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('No files in the queue to print.')

    elif menu == '0':
        break

    else:
        print('Invalid option. Please try again.')


