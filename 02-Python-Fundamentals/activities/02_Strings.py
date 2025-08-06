# 1. Create Strings:
# 1.1. Create two strings: first_name and last_name with your first and last name.
first_name = "Alice"
last_name = "Smith"
# 1.2. Create a multi-line string called bio describing yourself in two sentences.
bio = """Hello, I"m Alice
I love programming Python"""

# 2. Access Characters and Slice Strings:
# 2.1. Print the first character of first_name and the last character of last_name.
print(first_name[0])
print(last_name[-1])
# 2.2. Slice bio to print only the first 10 characters.
print(bio[:10])
# 3. Loop Through a String:
# 3.1. Use a for loop to print each character in your first_name on a new line.
for item in first_name:
    print(item)

# 4. String Length:
# 4.1. Print the length of bio using the len() function.
print("Number of characters in bio: ",len(bio))

# 5. Check Substrings:
# 5.1. Check if the word "Python" is in the string bio and print the result.
print("Python" in bio)
print("Python" not in bio)
# 5.2. Check if the word "Java" is not in the string bio and print the result.
print("Java" not in bio)

# 6. Modify Strings:
# 6.1. Convert first_name to uppercase and last_name to lowercase.
print("First name upper:", first_name.upper())
print("Last name lower:", last_name.lower())
# 6.2.Remove extra spaces from bio and replace any occurrence of "Python" with "coding".
bio = bio.strip().replace("Python", "coding")
print(bio)
# 6.3. Split bio into a list of words and print the result.
print(bio.split())
print(bio.split(" "))

# 7. Concatenate Strings:
# 7.1. Combine first_name and last_name into a single string full_name with a space in between.
full_name_f = f"{first_name} {last_name}"
full_name_concat = first_name + " " + last_name
# 7.2. Print the full name.
print(full_name_f)
print(full_name_concat)

# 8. String Formatting:
# 8.1. Use an f-string to print:
# "Hello, my name is {full_name} and I love Python!"
print(f"Hello, my name is {full_name_f} and I love Python!")

# 8.2. Use the format() method to print:
# "My full name is {} and I am {} years old." where {} are placeholders for full_name and your age.
print("My full name is {} and I am {} years old.".format(full_name_f, 25))

# 9. Escape Characters:
# 9.1. Create a string that includes a double quote and a single quote. Example:
# He said, "Python's great!"
print('Python\'s great!')

# Bonus: Use string methods to display:
# The bio string centered within 50 characters.
print(bio.center(50))
# The count of the letter "a" in your full_name.
print(full_name_f.lower().count("a"))

