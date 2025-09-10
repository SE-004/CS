Dictionaries
============

### Activity 1: Create a Book

1.  Create the dictionary `book` with two keys with its values: `title` and `year`. 
    
2.  Print the `book`.
3.  Add two more keys to `book` with its corresponding values: `summary` and `is_read`.
    
4.  Print the book.
5.  Update the title to ensure that the first letter of each word is capitalize.
    
6.  Print the book again to see the updated values.
    

### Activity 2: Access the Book Info

1.  Get the value of the `title` of the `book` using square notation.
    
2.  Get the value of the `year` using the corresponding dictionary method.
3.  Print all the names of the keys in `book`.
    
4.  Print all the values in `book`.
    
5.  Use a `for` loop to print for each item a string like: `"[key]: [title]"`. Make sure the first letter of each key is capitalize.
    

### Activity 3: Create a Reading List

1.  Create the `reading_list` variable:
    
    *   Its value should be a dictionary.
        
    *   It should have a key named `1`.
        
    *   Store the `book` dictionary inside key `1`.
        
2.  Print the `reading_list`.
3.  Add a new key-value pair:
    
    *   Name the key `2`.
        
    *   Store a dictionary inside with the keys: `title`, `year`, `summary` and `is_read`. 
        
    *   Add any values you want for each key.
4.  Print the `reading_list`.
    
5.  Repeat the previous 2 steps 1 more time, using `3` as the key name.
6.  Add a new key to each book inside your `reading_list`:
    
    *   Name the key `author`.
        
    *   Give the name of the author of the book as the value.
7.  Create a tuple named `new_book_item`.
    
    *   It should have 5 items stored inside.
        
    *   Each item should be a tuple with 2 items: a key name and a value.
        
    *    The keys have to represent the data of a book inside the `reading_list`: title, year, summary, is\_read and author.
        
8.  Add the `new_book_item` to the `reading_list`:
    
    *   Use the len() and the keys() to create the name of the new key: it shoud be the next number after the last key name.
        
    *   Store the `new_book_item` values inside the new key, but as a dictionary and not a list.
        
9.  Print all keys in the `reading_list`.
    
10.  Print all values in the `reading_list`.
    
11.  Print the `reading_list`.

### BONUS: Dictionary Lookup

1.  Create the `title` variable and give it a value.
    
2.  Check if the value of `title` is in the `reading_list` or in any of its nested dictionaries.
3.  Create the `release_year` variable and give it a value.
    
4.  Check if the value of `release_year` is in the `reading_list` or in any of its nested dictionaries.
    
5.  Check how many books in the `reading_list` were published in the same `release_year`.
6.  Print the `title` of the books that where released in the same `release_year`.