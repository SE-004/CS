Project: Create a Profile Book
==============================

1.  #### Create a variable for:
    
    *   `person` - a list that stores the following items:
        
        *   A tuple that stores `"first name` and `"John"`.
            
        *   A tuple that stores `"last name"` and `"Doe"`.
        *   A tuple that stores `"birthdate"` and `"12-12-1986"`.
            
        *   A tuple that stores the string `"age"` and an integer number with the age of the person.
        *   A tuple that stores the `"favorite color"` and `"blue"`.
            
    *   `people` - an empty list. 
    *   `favorite_foods` - a tuple that stores:
        
        *   the string `"favorite foods"` 
            
        *   A list with the items `"hamburger"`, `"spaguetti carbonara"` and `"chicken alfredo"`.
            
    *   `hobbies` - a list that stores:
        
        *   the string `"hobbies"`
            
        *    A list that with the items `"traveling"` and `"reading"`.
            
    *   `movies` - a list that stores:
        
        *   the string `"favorite movies"`
        *   A list with the items `"Star Wars: Episode IV - A New Hope"` and `"Avengers: Endgame"`.
            
    *   `profile` - a dictionary with a key for each letter in the string `alphabet`. Each key should have an empty dictionary as its value.
2.  #### Update the list inside the `favorite_foods` tuple: 
    
    *   Add 2 more items to the list.
        
    *   Remove the item that is your less favorite of all the foods.
        
    *   Update the value of the last item to be your favorite food.
        
3.  #### Update the list inside the `hobbies` tuple: 
    
    *   Update the last hobby to be `"cooking"`.
        
    *   Add two more hobbies.
        
    *   Update the value of your first hobby to be the same as third item.
        
    *   Remove the last item.
        
4.  #### Update list insi the `movies`
    
    *   Remove the first item.
        
    *   Add two new item at the end.
        
    *   Update the last value to be `"The empire Strikes Back"`.
        
5.  #### Remove duplicates from our lists:
    
    *   Transform into a list:
        
        *   The tuple `favorite_foods`.
            
        *   The tuple `hobbies`.
            
    *   Update the nested lists of  `favorite_foods`  and `hobbies` by transforming them into sets to remove duplicated values.
        
    *   Transform back into lists both nested sets in `favorite_foods` and `hobbies`.
        
    *   Transform back the lists `favorite_foods` and `hobbies` into tuples.
        
6.  #### Store all the data in the `person` list:
    
    *   Add the `favorite_foods` tuple.
        
    *   Add the `hobbies` tuple.
    *   Add the `movies` tuple.
        
7.  #### Transform the `person` to be a dictionary.
    
8.  #### Store the person in the right entry of the profile:
    
    *   Loop through the `profile`.
        
    *   Check if the key is the same as the first letter of the `person`'s last name.
        
    *   If it is, create a new key inside it following the format `"Doe, John"`.
        
9.  #### Print:
    
    *   The `profile` key that has the same value as `"Doe, John"`.
        
    *   All the keys from `profile`.
        
    *   All the values from `profile`.
        
    *   All the keys inside the`"Doe, John"`.
        
    *   All the  values inside `"Doe, John"`.
10.  #### Create some more profiles:
    
    *   Update the `person` dictionary to have fresh new info in the keys:
        
        *   `"first name"`
            
        *   `"last name"`
            
        *   `"birthdate"`
            
        *   `"age"`
            
        *   `"favorite color"`
            
        *   `"favorite foods"`
            
        *   `"hobbies"`
            
        *   `"movies"`
            
    *   Add the `person`'s new data to the `people` list (be careful not to create a reference when adding the data).
        
    *   Repeat the last two steps for as many people you want.
11.  #### Add the new profiles to the Profile Book:
    
    *   Loop through both the `profile`'s keys and the `people` items ([nested loops](https://www.w3schools.com/python/gloss_python_for_nested.asp "Python Nested Loops")).
        
    *   Check if the key in profile is the same as the `"last name"`'s first letter of the people item.
        
    *   If it is, add a new key-value pair inside that dictionary key.
        
        *   The key should be in the format of `"Doe, John"` by using the first and last name o the item.
            
        *   The value should be the item if the `people`'s list.
            
12.  #### Print the final dictionary.
    

### Bonus

1.  Print with a loop all the `profile`'s keys that have a value ([bool()](https://www.w3schools.com/python/ref_func_bool.asp "Python bool() Function")).
2.  Print with a loop a message with an introduction of each one of the people added to the profile.
    
3.  Check if the hobby `"Hiking"` is included in any of the entries of the `profile` and print a message if it is.
    
4.  Print if there is a person named Laura in the `profile`.