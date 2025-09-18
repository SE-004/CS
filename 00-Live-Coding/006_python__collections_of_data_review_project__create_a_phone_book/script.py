# ============================
# Project: Create a Phone Book
# ============================

# 1.  #### Create the variables: 
    
#     *   `alphabet` - pass a string with all of the letters o the alphabet as its value.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     *   `phone_book` - an empty dictionary.
phonebook = {}

# 2.  #### Create an entry for each letter of the alphabet in the dictionary:
for letter in alphabet:
    phonebook[letter.capitalize()] = {}

#     *   The key should be named after the letter of the alphabet capitalize.
        
#     *   The value should be an empty dictionary.
        
# 3.  #### Print: 
    
#     *   The `phone_book`.
# print(phonebook)
#     *   All the keys in the `phone_book`.
# print(phonebook.keys())

# 4.  #### Add inside the key `"A"`: 
    
#     *   Three key-value pairs. 
        
#     *   Each key should be the name of a person.
        
#     *   Each value should be a phone number.
# phonebook["A"] = {"Albert":"1234", "Alberto":"3345", "Andreas":"9987"} 
phonebook["A"].update({"Albert":"1234", "Alberto":"3345", "Andreas":"9987"})
# phonebook["A"]["Albert"] = "1234"
# phonebook["A"]["Alberto"] = "3345"
# phonebook["A"]["Andreas"] = "9987"
       
# 5.  #### Print: 
    
#     *   All the names inside the `"A"` dictionary.
print(phonebook["A"].keys())

#     *   Print all the phones in the dictionary `"A"`.
print(phonebook["A"].values())        
#     *   The `"A"` dictionary.
print(phonebook["A"])    
     
# 6.  #### Repeat the last two step for the dictionaries inside `"C"`, `"M"` and `"P"`.
phonebook['C']['Charlie'] = '020-233343'
phonebook['C']['Ceaser'] = '010-23456'
phonebook['C']['Case'] = '123-45678'    

phonebook['M']['Max'] = '123-123-123'
phonebook['M']['Maria'] = '231-123-123'
phonebook['M']['Melvin'] = '231-123-121'

phonebook["P"]["pino"] = "012-345"
phonebook["P"]["pina"] = "0456-789"
phonebook["P"]["pini"] = "0876-543"


# 7.  #### Print all keys in the `phone_book`.
print(phonebook.keys())

# 8.  #### Print all values in the `phone_book`.
print(phonebook.values())    

# ### BONUS: Dictionary Lookup

# 1.  Create the `name` variable and give it a value.
name = "Mara"   
# 2.  Check if the `name` is in the corresponding entry in the `phone_book`.

# for letter, people in phonebook.items():
#     if name.lower() in people or name.capitalize() in people or name.upper() in people:
#         print("Name found")
#         break
# else:
#     print("Name not found")
name_found = False;

for letter in phonebook.keys():
    for person in phonebook[letter].keys():
        if name.lower() == person.lower():
            name_found = True
            print("Found name: ", person)
            break
if not name_found:
    print("Name not found")



# 3.  Create the `phone` variable and give it a value.

# 4.  Check if the `phone` is in any of the entries the `phone_book`.
    
# 5.  Print the name of the person that the `phone` belongs to if it is in the `phone_book`.
number_search = '231-123-111'   #Maria
found = False

for letter, people in phonebook.items():
    for name, number in people.items():
        if number_search in number:
           print("Found number for: ", name)
           found = True

if not found:
    print("Number not found")
