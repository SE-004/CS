# 1. Create a Set
# Create a set named fruits containing at least 5 unique items (e.g., names of fruits).
fruits = {"apple", "banana", "cherry", "date", "orange"};

# Print the set.
print(fruits)

# 2. Check Membership
# Check if a specific item (e.g., "apple") is in fruits using the in keyword and print a message confirming its presence or absence.
print("apples" in fruits);
print("apple" in fruits);
print("apples" not in fruits);
print("apple" not in fruits);

# 3. Add and Update Items
# Add a new element to fruits using the add() method. Print the set after adding.
fruits.add("fig");
print(fruits)
# Create another set more_fruits with at least 3 unique items.
more_fruits = {"grape", "kiwi", "straberry"}

# Use the update() method to add elements from more_fruits to fruits. Print the updated set.
fruits.update(more_fruits);
print(fruits)

# 4. Remove Items
# Remove an element from fruits using remove(). Print the set after removal.
fruits.remove("grape");
print(fruits)

# Attempt to remove an element not in the set using discard() and observe that no error occurs.
fruits.discard("pinapple");
fruits.discard("apple");
print(fruits)

# Use pop() to remove and print an arbitrary element from fruits. Then print the set.
fruits.pop();
print(fruits)

# Use clear() to remove all elements from a copy of fruits and print the empty set.
# fruits.clear();
# print(fruits)

# 5. Set Operations
# 5.1. Create two sets:
# set_a with some overlapping items with fruits.
a = {"apple", "date", "orange"}

# set_b with some different items.
b = {"banana", "cherry", "date", "orange"}

# 5.2. Perform and print the result of the following operations:
# Union: Use union() to combine set_a and set_b.
all_fruits = a.union(b);
print(all_fruits)
print(a)
print(b)

# Intersection: Use intersection() to find common elements between set_a and set_b.
intersection_result = a.intersection(b);
print(intersection_result)

# Difference: Use difference() to find elements in set_a not in set_b.
difference_result_a = a.difference(b);
print(difference_result_a)

difference_result_b = b.difference(a);
print(difference_result_b)

# Symmetric Difference: Use symmetric_difference() to find items in either set_a or set_b but not in both.
symm_difference_result = a.symmetric_difference(b);
print(symm_difference_result)

# 6. In-place Set Operations
# Use difference_update() on a set to remove items that are also in another set. Print the result.
# a.difference_update(b);
# print(a)

# Use intersection_update() on a set to keep only items common with another set. Print the result.
# b.intersection_update(a);
# print(b)

# Use update() to add elements from another set to the current set. Print the result.
# a.update(b);
# print(a);

# 7.1. Relational Methods
# Create two sets small_set and large_set such that small_set is a subset of large_set.
small_subset = {"banana", "cherry"};
large_subset = {"banana", "cherry", "fig", "grape"};

# Use issubset() to verify that small_set is a subset of large_set and print the result.
is_subset = small_subset.issubset(large_subset);
print(is_subset);

# Use issuperset() to verify that large_set is a superset of small_set and print the result.
is_superset = large_subset.issuperset(small_subset)
print(is_superset);

# Check if two sets are disjoint using isdisjoint() and print the result.
are_disjoint = small_subset.isdisjoint(a);
print(are_disjoint);
