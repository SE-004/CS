# 1. Basic If Condition Write a block that checks if a number is positive, negative, 
# or zero using simple if, elif, and else. You must declare any necessary variable(s).
number = 0;
if number > 0:
    print("Positive");
elif number < 0:
    print("Negative");
else:
    print("Zero")

# 2. Grade Calculator Given a score between 0 and 100, use if, elif, and else to determine 
# and print the corresponding grade (A, B, C, D, or F).
score = 85;
grade = "";

if score >= 90:
    grade = "A";
elif score >= 80:
    grade = "B";
elif score >= 70:
    grade = "C";
elif score >= 60:
    grade = "D";
else:
    grade = "F";

# print(grade)

# 3. Ternary Operator Practice Use a ternary operator to set a variable status to "adult" 
# if age is 18 or older, and "minor" otherwise.
age = 23;
status = "adult" if age >= 18 else "minor";
# print(status)

# 4. For Loop over a List Iterate over a list of vehicles using a for loop and print an 
# f-string with each vehicle.
vehicles = ["car", "bike", "train"];
for item in vehicles:
    pass
    # print(f"Vehicle: {item}");

# 5. For Loop with Conditions Loop over numbers 1 to 10 using a for loop and print only the 
# even numbers, skipping the odds using continue.
for num in range(1,11):
    if num % 2 != 0:
        continue;
    # print(num);
    

# 6. While Loop Summation Use a while loop to sum all numbers from 1 to 100. 
# Print the total sum at the end.
total = 0;
i = 1;
while i <= 100:
    total += i
    i += 1

# print("Total amount", total)

# 7. Break out of a Loop Iterate over a list of words and break out of the loop as soon as 
# a word with more than 5 letters is found. 
# Print that word.
words = ["car", "train", "dog", "vehicle", "bus"];

for item in words:
    if len(item) > 5:
        print("Found word: ", item);
        break;

# 8. Nested Loops Create a list of people and a list of pets. 
# Loop over the lists in order to print all the possible combinations of persons and a respective pet.
people = ["Alice", "Jorge", "Sara"];
pets = ["dog", "cat", "rabbit"];
message = [];
for person in people:
    for pet in pets:
        message.append(f"{person} has a {pet}");

# print(message)

# 9. Loop with Else Clause Use a for loop to search for a specific value in a list. 
# If the value is found, print a success message and break out of the loop. 
# Otherwise, after the loop finishes, use an else clause to print that the value was not found.
values = [1,3,6,3,4,6];
search_for = 10;

for value in values:
    if value == search_for:
        print("Found: ", value);
        break;
else:
    print("Not found")

# 10. Pass Statement Usage Create an empty loop over a list of items using pass to practice 
# structure without executing any code.
for num in range(1, 11):
    pass;  

# 11. Pattern matching
# Create three lists: fruits, veggies, meat
# Add different food items to each list
# Create a match expression to determine if a given item in a variable item is a fruit, a 
# veggie, a meat product or anything else.
# Remember you can create guards with if statements.
fruits = ["apple", "banana", "cherry"];
veggies = ["carrot", "broccoli", "spinach"];
meats = ["chicken", "beef", "pork"];

item = "avocado";
message = "";

match item:
    case fruit if fruit in fruits:
        message = f"{item} is a fruit";
    case veggie if veggie in veggies:
        message = f"{item} is a veggie";
    case meat if meat in meats:
        message = f"{item} is a meat";
    case _:
        message = f"{item} is not a fruit nor a veggie nor meat";

print(message)
