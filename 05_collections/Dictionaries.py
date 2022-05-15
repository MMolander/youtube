# Dictionaries in python are:
# Unordered
# Can be changed
# Acces values by keys
# - Sometimes called an associative arrau or hash table in other languages

# building a dictionary
customer_address = {
    "id"        : 23,
    "street"    : "123 Main street",
    "city"      : "Norrköping",
    "state"     : "Östergötland",
    "zip"       : "602 15",
    "is_active" : True,
}

# Acces a value by key
city = customer_address["city"]
is_active = customer_address["is_active"]
print(f"City: {city}, Active? {is_active}")

#new value
customer_address["city"] = "Sthlm"

#adding a key value pair to a dictionary
customer_address["phone"] = "555-555-1234"
print(customer_address["phone"])
print(customer_address["city"])

customer = {
    "name" : "Jane Doe",
    "age" : 60,
    "is employee" : True,
    "address": customer_address #dict value
}
print(customer["address"]["state"])