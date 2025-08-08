# 1. Create and Print a List
# Create a list of 5 items (e.g., your favorite fruits, numbers, or any objects you like).
shopping_list = ["milk", "eggs", "apples", "oranges", "honey"]
# Print the list to the screen.
print(shopping_list);

# 2. Access Elements by Index and Negative Index
# Print the first item, the last item, and at least one item using a negative index (for example, my_list[-2]).
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[-2])

# 3. Slice a List
# Print a subset of the list (for example, items from index 1 to 3).
print(shopping_list[1:4])
# Print everything from the beginning up to index 2, and from index 2 to the end.
print(shopping_list[:3])
print(shopping_list[2:])

# 4. Check if an Item Exists
# Use the in keyword (for example, if "apple" in my_list:) to check if a certain item is in the list.
# Print a message indicating whether the item is found.
print("apple" in shopping_list);

if "apples" in shopping_list:
    print("Apple is in the shopping list.")

# 5. Add Items
# Use append() to add a new item to the end of the list.
shopping_list.append("sugar");
print(shopping_list)
# Use insert() to add an item at a specific index.
shopping_list.insert(2, "Kiwi")
print(shopping_list)

# 6. Change Items
# Update the value of a specific element by index.
shopping_list[1] = "Flour"
print(shopping_list)
# Change multiple items at once by assigning to a slice (for example, my_list[1:3] = ["new1", "new2"]).
shopping_list[1:3] = ["sugar", "milk"];
print(shopping_list)

# 7. Remove Items
# Remove a specific item by value using remove().
shopping_list.remove("sugar");
# for item in shopping_list:
#     if item == "sugar":
#         shopping_list.remove("sugar");
print(shopping_list)
# Remove an item at a specific index using pop().
shopping_list.pop();
print(shopping_list)

shopping_list.pop(2);
print(shopping_list)

# Clear the entire list with clear() (or demonstrate using a temporary list).
# shopping_list.clear()
# print(shopping_list)

# 8. Copy a List
# Create a copy of your list using list.copy() or slicing ([:]).
groceries = shopping_list.copy();
print(groceries)

partial_shopping_list = shopping_list[1:];
print(partial_shopping_list)

shopping = shopping_list;
print(shopping)

# Modify the original list afterward, then print both lists to verify they are independent.
partial_shopping_list.append("oranges")
print("partial: ", partial_shopping_list)
groceries.append("apples")
print("groceries: ",groceries)
shopping_list.append("sugar")
print("original: ",shopping_list)
print("shopping: ", shopping)
# 9. Concatenate and Extend
# Create two separate lists and join them in different ways:
a = [1,2,3];
b = [4,5,6];

# Using the + operator (e.g., list_a + list_b).
c = a + b
print(c)
# Using extend() (e.g., list_a.extend(list_b)).
b.extend(a);
print(b)

# 10. Sort and Reverse
# Sort the list using sort().
b.sort()
print(b);
# Reverse the sorted list using reverse().
b.reverse();
print(b)

# b.sort(reverse=True)

# sorted() - reversed() - list()

sorte_a = sorted(a)
print(sorte_a)
reversed_a = list(reversed(a))
print("reversed_a", reversed_a)
print("a", a)

# 11. Count and Index
# Use count() to find how many times a particular value appears in the list.
print("Count of sugar:", shopping_list.count("sugar"))
print("Count of milk:", shopping_list.count("milk"))
# Use index() to find the position of a specific value in the list.
print("Index of milk:", shopping_list.index("milk"))


# 12. List Comprehension (Bonus)
# Create a new list that transforms or filters your existing list (for example, convert strings to uppercase if they meet a certain condition).
groceries_2 = [item.upper() for item in shopping_list];
print(groceries_2)

# Use the syntax [expression for item in my_list if condition]
groceries_3 = [item.upper() for item in shopping_list if "s" in item];
print(groceries_3)