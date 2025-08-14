# 1. Create and Print a Dictionary
# Create a dictionary representing a person with keys such as "name", "age", and "city".
person = {
    "name": "Alice",
    "age": 23,
    "city": "New York"
};
# Print the entire dictionary to the screen.
print(person);

# 2. Access Dictionary Elements
# Print the value associated with the key "name" using square brackets.
print(person["name"]);
print(person["age"]);
print(person["city"]);

# Use the get() method to safely retrieve the value for a key that might not exist (e.g., "email"), providing a default value.
print(person.get("name"));
print(person.get("age"));
print(person.get("city"));

# Print all keys, values, and items of the dictionary using keys(), values(), and items() methods.
print(person.keys());
print(person.values());
print(person.items());

# 3. Check for Key Existence
# Check if the key "age" exists in the dictionary using the in keyword.
print("age" in person);
print("address" not in person);

# 4. Change and Update Dictionary Elements
# Update the value associated with "city" directly by assignment.
person["name"] = "Mario";
print(person)



# Use the update() method to change multiple key-value pairs or add new ones (e.g., add "occupation": "Engineer").
person.update({"name": "Alice", "age": 26});
print(person)

# 5. Add New Items to the Dictionary
# Add a new key-value pair (e.g., "country": "USA") using direct assignment.
person["address"] = {
    "street": "Av Habana",
    "postalcode": 11111,
    "city": "New York"
}
print(person);

# Use update() to add another new key-value pair (e.g., "hobby": "cycling").
person.update({"hobby": "Traveling", "name": "Mario"});

# 6. Remove Items from the Dictionary
# Remove an item by key using pop() and print the removed value.
person.pop("hobby")
error_message = person.pop("hobby", "Not found")
print(person)
print(error_message)

# Use popitem() to remove the last inserted key-value pair, and print the pair removed.
person.popitem()
print(person);

# Delete a specific key-value pair using the del keyword.
del person["age"]
print(person)

# Clear the entire dictionary using clear() and print the empty dictionary.
# person.clear();
# print(person)

# 7. Copy a Dictionary
# Create a shallow copy of your dictionary using the copy() method or dict() constructor.
person_2 = person;
print(person_2)

person_3 = person.copy();
print(person_3)
# Modify the original dictionary and show that the copy remains unchanged.
person_3["name"] = "John";
print(person_3)
person_2["name"] = "Alice";
print(person_2)
print(person)

# 8. Using setdefault()
# Use setdefault() to retrieve the value of a key that exists, and then for a key that doesn’t exist, adding it with 
# a default value.
print(person.setdefault("name", "Unknown"))
print(person.setdefault("email", "Not provided"))

# Print the dictionary to observe changes.
print(person)
