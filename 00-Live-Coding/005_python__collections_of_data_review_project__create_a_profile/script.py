from datetime import datetime
# =========================
# Project: Create a Profile
# =========================

# 1.  #### Create a variable for:
    
#     *   `person` - a tuple that stores the name and age of a person.
person = ("John", 36)        
#     *   `favorite_foods` - a list with one item: your favorite food.
favorite_foods = ["Pizza"]        
#     *   `hobbies` - a list with one item: your favorite hobby.
hobbies = ["Programming"]        
#     *   `profile` - an empty dictionary.
profile = {}

# 2.  #### Update the `favorite_foods` list: 
    
#     *   Add at least 3 more items at the end of the list.
favorite_foods.extend(["Pasta","Potatoes","Popcorn"])
#     *   Remove the item that is your less favorite of all the foods.
favorite_foods.remove("Popcorn")     
#     *   Update the value of the last item to be your favorite food.
favorite_foods[-1]="Pizza"     
# print(favorite_foods)

# 3.  #### Update the `hobbies` list: 
    
#     *   Add 3 more hobbies to the list at any position you want in the list.
hobbies.insert(1, "swim")
hobbies.insert(2, "gym")
hobbies.insert(3, "jogging")
        
#     *   Remove the last item of the list.
hobbies.pop()
#     *   Update the value of your first hobby to be the same as the last value.
hobbies[0] = hobbies[-1]
#     *   Add a new hobby at the end of the list.
hobbies.append("dive")
# print(hobbies)


# 4.  #### Remove duplicates from our lists:
    
#     *   Transform the `favorite_foods` list in a set to remove any duplicated foods.
favorite_foods = set(favorite_foods)
      
#     *   Transform the `hobbies` list in a set to remove any duplicated hobbies.
hobbies = set(hobbies)

# 5.  #### Store all the data in the `profile` dictionary:
    
#     *   Add the key `name` to the `profile` and give it the name store in `person`'s tuple.
profile["name"] = person[0]
#     *   Add the key `age` and give it the number stored in the `person`'s tuple
profile["age"] = person[1]
#     *   Add the key `"hobbies"` and store the `hobbies` set transformed back into a list.
profile["hobbies"] = list(hobbies)
#     *   Add the key `"favorite foods"` and store the `favorite_foods` set transformed back into a list.
profile["favorite foods"] = list(favorite_foods)
print(profile)

# 6.  #### Print:

#     *   The `"name"` in `profile`.
print(profile["name"])        
#     *   The `"age"` in `profile`.
print(profile["age"])                
#     *   A string with all of the `"hobbies"` in `profile`.
myString = ", ".join(profile["hobbies"])
#myString = hobbies[0] + ", " + hobbies[1] + ", " + hobbies[2] + ", " + hobbies[3]
print(myString)
#     *   All the keys from `profile`.
print(profile.keys())        
#     *   All the values from `profile`.
print(profile.values())        
#     *   The entire `profile`.
print(profile)

# current_date = datetime.now()

# 7.  #### Update:
# profile = {'name': 'John', 'age': 36, 'hobbies': ['gym', 'swim', 'dive'], 'favorite foods': ['Pasta', 'Pizza']}
#     *   the `"name"` of the profile with your nickname.
print(profile['name'])     
profile['name'] = "Alice"  
#     *   the `"age"` to be the current year([datetime module](https://flexiple.com/python/python-get-current-year "Get current year")) minus the year you were born into. 
current_year = datetime.now().year
birthday = 1990
age = current_year - birthday
# print(f"Current year: {current_year}")
# print(f"Birthday: {birthday}")
# print(f"Your age is: {age}")
profile['age'] = age
print(profile)

# 8.  #### Add:
    
#     *   A new key named `"movies"` to the `profile`.
profile["movies"] = ["Matrix", "Minions", "Inception"]
#     *   3 movies to the `"movies"` key you just created.
#     *   A new hobby to the `"hobbies"` list.
profile["hobbies"].append("Gardening") 

# 9.  #### Update:
    
#     *   The last food in `"favorite foods"` to be `"Hamburger"`.
profile["favorite foods"][-1] = "Whopper"
profile["favorite foods"].sort()


#     *   The `"favorite foods"` to be sorted in an ascending manner.
        
# 10.  #### Print the final profile.
print(profile)