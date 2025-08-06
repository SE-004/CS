name = "John Doe"
multi_line_string = """This is a string
that spans multiple lines."""
age = 30
is_student = True
f_string = f"My name is {name}, I am {age} years old, and it is {is_student} that I am a student."

# print(f_string, multi_line_string, "Hello, World!", sep="\n")
# print(type(name))

# print(name[0])  # First character
# print(name[-1])  # Last character
# print(name[2:4])  # Characters from index 2 to 3
# print(name[5:])  # Characters from index 5 to the end

# print(name.upper())
# print(name.lower())
# print(" maria ".strip())  # Remove leading and trailing spaces
# print(name.replace("Doe", "Smith"))  # Replace 'Doe' with 'Smith'

a = "1"
b = 1
c = 3
# print(a + str(b))  # Concatenation of string and integer
# print(b + c)  # Addition of integers

# # Operations on integers
# print(b - c)  # Subtraction of integers
# print(b * c)  # Multiplication of integers
# print(b / c)  # Division of integers
# print(b // c)  # Floor division of integers
# print(b % c)  # Modulus of integers
# print(b ** c)  # Exponentiation of integers

# b += c
# print("new value of b", b)  # Increment b by c

print(a == b)
print(a != b)
print(c >= b)
print(c < b)

print("Membership Operators", "a" in name, "a" not in name, sep="\n")
