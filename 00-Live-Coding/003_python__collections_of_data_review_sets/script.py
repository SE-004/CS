import random

groceries = ["milk", "eggs", "vinager", "milk", "apples", "potatos", "eggs"];

### Activity 1: Unique Words

# 1.  Convert the list `groceries` to a set to remove duplicates and store it in a new variabled named `shopping_list`.
shopping_list = set(groceries.copy())
# 2.  Print the set.
print(shopping_list)

# ### Activity 2: Add And Remove

# 1.  Add three new items to the set `shopping_list` and print it.
shopping_list.add("Mate") 
shopping_list.add("Beer") 
shopping_list.add("Juice") 
print(shopping_list)

# 2.  Remove the item `milk` from the `shopping_list` and print it.
shopping_list.remove("milk") 
print(shopping_list)

# 3.  Remove a random item from the `shopping_list` and print it.
shopping_list.pop()
print(shopping_list)
    
# 4.  Add `honey` to the `shopping_list`.
shopping_list.add("honey") 
print(shopping_list)   
# 5.  Remove with a loop 3 random values of the `shopping_list`.
for i in range(3):
    shopping_list.pop()

# 6.  Print the `shopping_list`.
print(shopping_list)    

# ### Activity 3: Set Operations

# 1.  Create two sets: `a = {1, 2, 3, 4, 5}` and `b = {3, 4, 5, 6, 7}`.
my_set_1 ={1,2,3,4,5}
my_set_2 = {3,4,5,6,7}  
# 2.  Create a new set called `union` and stored the joined values of `a` and `b`.
union = my_set_1.union(my_set_2)
# 3.  Print `union`.
print(union)

# 4.  Create the variable `intersection` and store the numbers that are inlcuded in `a` and `b`.
intersection_ab = my_set_1 & my_set_2;
intersection = my_set_1.intersection(my_set_2)
# 5.  Print `intersection`.
print(intersection_ab)
print(intersection)

# 6.  Create two new variable named `difference_a` and `difference_b` and store in each one the unique numbers in set `a` 
# and in set `b` respectively.
difference_a = my_set_1.difference(my_set_2)    
difference_b = my_set_2.difference(my_set_1)    
# 7.  Print both `difference_a` and `difference_b`.
print(difference_a)
print(difference_b)

# ### Activity 4: Set Membership

# 1.  Create a variable name `even` and use [range](https://www.w3schools.com/python/ref_func_range.asp "Range in Python")
#  to create a set of even numbers between 0 and 20 as its value.
even = set(range(0, 21, 2))
# 2.  Create a variable named `random_int` and use the random module to asign a random integer between 0 and 20.
random_int = random.randint(0, 20)
print(random_int);
# 3.  Check if `random_int` exists in the set `even`. 
# 4.  Print the result of the check.
if random_int in even:
    print("Yes it is even")
else:    
    print("no it not even")
    
# 5.  Run the code several times to see if the result of the check is different.