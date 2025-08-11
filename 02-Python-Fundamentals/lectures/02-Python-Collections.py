fruits = ["apple", "banana", "cherry", "banana"]
vegetables = ["carrot", "broccoli", "spinach"]
# print(fruits);
# print(fruits[0]);
# print(fruits[1]);
# print(fruits[2]);
# print(fruits[-1]);  # Last item
# print(fruits[-2]);  # Second to last item

# print(len(fruits))

# fruits[0] = "orange"  # Modify the first item
# print(fruits)
# fruits[1:3] = ["kiwi", "mango"]  # Modify a slice of the list

# #Adding and modifying items in a list

# fruits.append("orange")  # Add an item to the end
# print(fruits)

# fruits.insert(1, "kiwi")  # Insert an item at index 1
# print(fruits)
# print(fruits[1])  # Check the item at index 1

# healthy_foods = fruits + vegetables  # Concatenate lists
# print(healthy_foods)

# fruits.extend(vegetables);  # Extend fruits with vegetables
# print(fruits)  # This will print the modified fruits list

# Removing items from a list
# fruits.remove("banana")  # Remove the first occurrence of "banana"
# print(fruits)

# for fruit in fruits:
#     if fruit == "banana":
#         fruits.remove(fruit)

# print(fruits)  # This will print the modified fruits list after removing "banana"

# fruits.pop()  # Remove the last item
# print(fruits)

# fruits.pop(1)  # Remove the item at index 1
# print(fruits)

# fruits.clear()  # Clear the list
# print(fruits)  # This will print an empty list

# TUPLES
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# colors = ("red", "green", "blue")
# print(colors)
# print(colors[0])

# more_colors = ("yellow", "purple", "orange")

# # Concatenating tuples
# all_colors = colors + more_colors
# print(all_colors)
# repeated_colors = colors * 2  # Repeating tuples
# print(repeated_colors)

# print(colors.count("red"))  # Count occurrences of "red"
# print(colors.index("green"))  # Find the index of "green"

# # Unpacking tuples
# red, green, blue = colors
# print(red)   # Output: red
# print(green) # Output: green
# print(blue)  # Output: blue

# first, *rest = more_colors
# print(first)  # Output: yellow
# print(rest)   # Output: ['purple', 'orange']

# start, second, *middle, previous, last = all_colors
# print(start)  # Output: red
# print(second) # Output: green
# print(middle) # Output: ['blue', 'yellow', 'purple']
# print(previous)  # Output: orange
# print(last)   # Output: orange

# SETS
# Sets are unordered collections of unique elements.
fruits_set = set(fruits);
print(fruits_set)

fruits = list(fruits_set);
print(fruits)

numbers_1 = {1, 2, 3, 4}
numbers_2 = {1, 2, 5, 6, 4}
# print(numbers_1.difference(numbers_2))
# print(numbers_1.symmetric_difference(numbers_2))

print(numbers_1.intersection(numbers_2))
num_union = numbers_1.union(numbers_2);
print(num_union)
print(numbers_1)

numbers_1.update(numbers_2)
print(numbers_1)

for num in numbers_1:
    if num == 3:
        print(num)

person = {
    "name": "Alice",
    "age": 36,
    "address": {
        "street": "Gartenstr.",
        "city": "Berlin"
    },
    "hobbies": ["Singing", "Traveling"]
}

print(person)
# print(person["address"]["city"])
# person["address"]["city"] = "Madrid"
# print(person["address"]["city"])
# person["address"]["postalcode"] = 11111;
# print(person["address"]["postalcode"])
print(person["hobbies"][0])
person["hobbies"][0] = "Reading";
print(person["hobbies"])
# print(person.get("name"))
# print(person.keys())
# print(person.values())


