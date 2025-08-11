# 1. Create a Tuple
# Create a variable named my_tuple and assign it a tuple containing at least 5 items (they can be strings, numbers, or a mix).
my_tuple = (1,2,3,4,5,2,3,2)
# 2. Print the Tuple
# Use the print() function to display the contents of my_tuple.
print(my_tuple)
# 3. Access Tuple Items
# Print the first item of the tuple using an index of 0.
print(my_tuple[0])
# Print the last item of the tuple using a negative index.
print(my_tuple[-1])

# 4. Slice the Tuple
# Print a slice of the tuple that includes some middle items
print(my_tuple[1:4])

# Print a slice that goes from the start of the tuple up to a certain index
print(my_tuple[:3])

# Print a slice that starts at a certain index and goes to the end
print(my_tuple[2:])

# 5.Check if an Item Exists
# Use the in keyword to check if a certain item exists in my_tuple.
print(2 in my_tuple)
print(6 in my_tuple)
# Print a message indicating whether the item is found.
if 2 in my_tuple:
    print("The number 2 is in the tuple")
    
if "banana" in my_tuple:
    print("The word banana is in the tuple")

# 6. Count and Index
# Use the count() method to find how many times a specific value appears in my_tuple.
print(my_tuple.count(2))
print(my_tuple.count(3))
print(my_tuple.count(1))
print(my_tuple.count(10))

# Use the index() method to find the position of the first occurrence of that value.
print(my_tuple.index(2))

# 7. Packing and Unpacking
# Packing: You’ve already packed the tuple by assigning multiple values to my_tuple.
print(len(my_tuple))
# Unpacking: Unpack my_tuple into separate variables so that each variable corresponds to an item in the tuple 
# num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8 = my_tuple;

# Use the asterisk (*) in another unpacking scenario 
num_1, num_2, *middle, num_7, num_8 = my_tuple;
print(num_1, num_2)

# 8. Joining Tuples
# Create another tuple named another_tuple with a few items.
another_tuple = (3,4,6,7,1,3)
# Concatenate my_tuple and another_tuple using the + operator. Print the result.
cocat_tuple = my_tuple + another_tuple;
print(cocat_tuple)
# Multiply one of your tuples by an integer and print the result to see the repeated items.
multi_tuple = my_tuple * 3;
print(multi_tuple)