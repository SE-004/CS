# 1.Create variables:
# 1.1. Create a variable named name and assign your name as a string.
name = "Maria"
# 1.2. Create a variable named age and assign your age as a number.
age = 31
# 1.3. Create a variable named height and assign your height in meters as a float.
height = 1.61
# 2. Print the variables:
print("name:", name)
print("age:", age)
print("height:", height)
# 3. Check the type of the variables:
print("Type of name: ", type(name))
print("Type of age: ", type(age))
print("Type of height: ", type(height))
# 4. Casting:
# 4.1. Convert the age variable to a string and assign it to a new variable called age_str.
age_str = str(age)
# 4.2. Print a sentence that combines name and age_str. Example: "My name is Alice and I am 25 years old."
print("My name is " + name + " and I am " + age_str + " years old.")
print(f"My name is {name} and I am {age_str} years old.")

# 5. Global Variable (Bonus):
# 5.1. Create a variable named global_message outside a function and assign a message.
global_message = "Hello, World"
# 5.2. Inside a function, use the global keyword to modify the global_message variable.
def modify_global_message():
    global global_message
    global_message = "Hello, Python!"

    
# 5.3. Print the modified message after calling the function.
modify_global_message()
print("global message: ", global_message)