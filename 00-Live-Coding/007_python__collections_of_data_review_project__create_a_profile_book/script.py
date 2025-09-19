alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
# ==============================
# Project: Create a Profile Book
# ==============================

# 1.  #### Create a variable for:
    
#     *   `person` - a list that stores the following items:
person = [("first name", "John"),("last name", "Doe"), ("birthdate", "12-12-1986"),("age", "38"),("favorite color","blue")]
#         *   A tuple that stores `"first name` and `"John"`.
            
#         *   A tuple that stores `"last name"` and `"Doe"`.
#         *   A tuple that stores `"birthdate"` and `"12-12-1986"`.
            
#         *   A tuple that stores the string `"age"` and an integer number with the age of the person.
#         *   A tuple that stores the `"favorite color"` and `"blue"`.
            
#     *   `people` - an empty list. 
people = []
#     *   `favorite_foods` - a tuple that stores:
#         *   the string `"favorite foods"` 
#         *   A list with the items `"hamburger"`, `"spaguetti carbonara"` and `"chicken alfredo"`.
favorite_foods = ('favorite foods', ["hamburger", "spaguetti carbonara", "chicken alfredo"])
            
            
#     *   `hobbies` - a tuple that stores:
#         *   the string `"hobbies"`
#         *    A list that with the items `"traveling"` and `"reading"`.
hobbies = ('hobbies', ["traveling", "reading"])           
            
#     *   `movies` - a tuple that stores:
#         *   the string `"favorite movies"`
#         *   A list with the items `"Star Wars: Episode IV - A New Hope"` and `"Avengers: Endgame"`.
movies = ("favorite movies", ["Star Wars: Episode IV - A new Hope", "Avengers: Endgame"])
            
#     *   `profile` - a dictionary with a key for each letter in the string `alphabet`. Each key should have an empty dictionary as its value.
profile = {letter: {} for letter in alphabet}

# 2.  #### Update the list inside the `favorite_foods` tuple: 
#     *   Add 2 more items to the list.
favorite_foods[-1].append("apples")
favorite_foods[-1].append("bananas")
# print(favorite_foods)

#     *   Remove the item that is your less favorite of all the foods.
favorite_foods[1].remove("hamburger")
#     *   Update the value of the last item to be your favorite food.
favorite_foods[1][1]= "quesaddillas"   
  
# 3.  #### Update the list inside the `hobbies` tuple: 
    
#     *   Update the last hobby to be `"cooking"`.
hobbies[1][-1] = "cooking"
#     *   Add two more hobbies.
hobbies[1].extend(["cycling","reading"])
#     *   Update the value of your first hobby to be the same as third item.
hobbies[1][0] = hobbies[1][2]
#     *   Remove the last item.
del hobbies[1][-1]
# 4.  #### Update list inside the `movies`
    
#     *   Remove the first item.
movies[1].pop(0)

#     *   Add two new item at the end.
movies[1].extend(["abc", "def"])     

#     *   Update the last value to be `"The empire Strikes Back"`.
movies[1][-1] = "The empire Strikes Back"
# print(movies)

# 5.  #### Remove duplicates from our lists:
    
#     *   Transform into a set the following lists:
#         *   The list inside the tuple `favorite_foods`.
#         *   The list inside the tuple`hobbies`.
#         *   The list inside the tuple`movies`.
#     *   Transform back into lists both sets in `favorite_foods`, `hobbies` adn `movies`.

favorite_foods = (favorite_foods[0], list(set(favorite_foods[1])))
hobbies = (hobbies[0], list(set(hobbies[1])))
movies = (movies[0], list(set(movies[1])))

# print(favorite_foods)
# print(hobbies)
# print(movies)
        
# 6.  #### Store all the data in the `person` list:
#     *   Add the `favorite_foods` tuple.
person.append(favorite_foods)
#     *   Add the `hobbies` tuple.
#     *   Add the `movies` tuple.
person.extend([hobbies, movies])

        
# 7.  #### Transform the `person` to be a dictionary.
person = dict(person)
# print(person)
    
# 8.  #### Store the person in the right entry of the profile:
    
#     *   Loop through the `profile`.
#     *   Check if the key is the same as the first letter of the `person`'s last name.
#     *   If it is, create a new key inside it following the format `"Doe, John"`.
def insert_person_to_profile(profile, person):
    last_name_init = person["last name"][0].upper()
    person_key = f"{person['last name']}, {person['first name']}"
    if last_name_init in profile:
        profile[last_name_init][person_key] = person.copy()

insert_person_to_profile(profile, person)
# last_name_init = person["last name"][0].upper()
# person_key = f"{person['last name']}, {person['first name']}"

# if last_name_init in profile:
#     profile[last_name_init][person_key] = person.copy()


# key = person["last name"][0].upper()
# if key == person["last name"][0].upper():
#     profile[key] = {f"{person['last name']}, {person['first name']}":person.copy()}

# for key in profile:
#     if key == person["last name"][0].upper():
#         profile[key][f"{person['last name']}, {person['first name']}"] = person.copy()
        
# 9.  #### Print:
    
#     *   The `profile` key that has the same value as `"Doe, John"`.
# print([profile["D"]["Doe, John"]])
#     *   All the keys from `profile`.
# for key in profile:
#     print(f"Key: {key}, Value: {profile[key]}")
# #     *   All the values from `profile`.
# for key, value in profile["D"]["Doe, John"].items():
#     print(f"Key: {key}, Value: {value}")
#     *   All the keys inside the`"Doe, John"`.
        
#     *   All the  values inside `"Doe, John"`.


# 10.  #### Create some more profiles:
    
#     *   Update the `person` dictionary to have fresh new info in the keys:
person.update({
    "first name": "Alice", 
    "last name": "Smith", 
    "birthdate": "01-01-1990", 
    "age": 35, 
    "favorite color": "green", 
    "favorite foods": ["Hamburger"], 
    "hobbies": [], 
    "favorite movies": []
               })        
# print(person)
#         *   `"first name"`

#         *   `"last name"`
            
#         *   `"birthdate"`
            
#         *   `"age"`

#         *   `"favorite color"`
            
#         *   `"favorite foods"`
            
#         *   `"hobbies"`
            
#         *   `"favorite movies"`

#     *   Add the `person`'s new data to the `people` list (be careful not to create a reference when adding the data).
# insert_person_to_profile(profile, person)
people.append(person.copy())
#     *   Repeat the last two steps for as many people you want.
person.update({
                "first name":"umi",
                "last name":"olo", 
                "birthdate":"06/08/1994", 
                "age":"31", 
                "favorite color":"pink", 
                "favorite foods":["meat"], 
                "hobbies":["rugby"],
                "favorite movies": []
               })
# insert_person_to_profile(profile, person)
people.append(person.copy())
# print(profile)

# 11.  #### Add the new profiles to the Profile Book:
    
#     *   Loop through both the `profile`'s keys and the `people` items ([nested loops](https://www.w3schools.com/python/gloss_python_for_nested.asp "Python Nested Loops")).
        
#     *   Check if the key in profile is the same as the `"last name"`'s first letter of the people item.
        
#     *   If it is, add a new key-value pair inside that dictionary key.
        
#         *   The key should be in the format of `"Doe, John"` by using the first and last name o the item.
            
#         *   The value should be the item if the `people`'s list.
print(people)

for person in people:
    insert_person_to_profile(profile, person)
# 12.  #### Print the final dictionary.
    

# ### Bonus

# 1.  Print with a loop all the `profile`'s keys that have a value ([bool()](https://www.w3schools.com/python/ref_func_bool.asp "Python bool() Function")).
# 2.  Print with a loop a message with an introduction of each one of the people added to the profile.
    
# 3.  Check if the hobby `"Hiking"` is included in any of the entries of the `profile` and print a message if it is.
    
# 4.  Print if there is a person named Laura in the `profile`.
















