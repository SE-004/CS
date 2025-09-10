# Write your code here
# Write your code here
### Activity 1: Build a Grocery List
# 1.  Create a list called `groceries` with 5 items.
groceries = ['apple', 'banana', 'bread', 'milk', 'sugar']
# 2.  Add one more item at the end of the list.
groceries.append("ClubMate")
# 3.  Remove an item using the value of said item.
groceries.remove("banana")    
# 4.  Print the list.
# print(groceries)

# ### Activity 2: Favorite Numbers

# 1.  Create a list with at least 7 numbers.
numbers = [1,2,3,4,5,6,7]
# 2.  Print:
# print(numbers)
#     *   First 3 numbers using slicing.
# print(numbers[
# :3])
#     *   The list sorted in reverse without modifying the original list.
reversed_list = list(reversed(numbers))
# print(reserved_list)
# print(numbers)
#     *   A copy of the list reversed using indexing.
reversed_list2 = reversed_list[:];  
print(reversed_list2)     
#     *   The bigger number of the list.
bigger = max(numbers)
print(bigger)
#     *   The smallest number of the list.
print(min(numbers))
#     *   A sum of all the numbers in the list.
sum_of_all = sum(numbers)
print(sum_of_all)

# ### Activity 3: Movie List Analyzer

# 1.  Create a `movies` variable and store a list of your favorite movies.
movies = ["intersteller", "Your name", "oldboy"]
# 2.  Create a copy of the list in a second variable named `favorite_movies` updating each item to have the first letter o each word capitalize.
movies2 = [movie.title() for movie in movies]
# 3.  Print the list `favorite_movies`.
print(movies2)    
# 4.  Sort the `movies` original list in descending order.
movies.sort(reverse=True);
# movies.reverse()

# 5.  Print `movies`.
print(movies)