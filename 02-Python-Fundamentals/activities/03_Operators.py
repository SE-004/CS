# 1. Arithmetic Operators:
# Create two variables: a and b, and assign them the values 15 and 4.
a = 15;
b = 4;

# Perform and print the result of each of the following operations: addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
print("Addition result: ", a + b)
print("Substraction result: ", a - b)
print("Multiplication result: ", a * b)
print("Division result: ", a / b)
print("Modulus result: ", a % b)
print("Floor divion result: ", a // b)
print("Exponentiation result: ", a ** b)

# 2. Assignment Operators:
# Start with a variable x = 10.
x = 10
print("Initial value of x: ", x)
# Use the +=, -=, *=, and /= operators to modify the value of x. Print the result after each operation.
x += 5
print("After += 5: ", x)
x -= 3
print("After -= 3: ", x)
x *= 2
print("After *= 2: ", x)
x /= 4
print("After /= 4: ", x)

# 3. Comparison Operators:
# Compare a and b using ==, !=, >, <, >=, and <=. Print the results of each comparison.
print("a == b: ", a == b)
print("a != b: ", a != b)
print("a > b: ", a > b)
print("a < b: ", a < b)
print("a >= b: ", a >= b)
print("a <= b: ", a <= b)

# 4. Logical Operators:
# Create two Boolean variables: is_python_fun = True and is_java_fun = False.
is_python_fun = True
is_java_fun = False

# Use the and, or, and not operators to combine or negate these values. Print the results.
# "", [], {}, None, 0 are considered False in Python

print("is_python_fun and is_java_fun: ", is_python_fun and is_java_fun)

print("is_python_fun and not is_java_fun: ", is_python_fun and not is_java_fun)

print("is_python_fun and not is_java_fun: ", is_python_fun and is_java_fun or not is_java_fun)

print("is_python_fun or is_java_fun: ", is_python_fun or is_java_fun)
print("not is_python_fun: ", not is_python_fun)
print("not is_java_fun: ", not is_java_fun)


# 5. Identity Operators:
# Create two lists: list1 = [1, 2, 3] and list2 = list1.
list1 = [1, 2, 3];
list2 = list1;

# Check if list1 is list2 and if list1 is not list2.
print("list1 is list2: ", list1 is list2)

# Create a third list list3 = [1, 2, 3]. Check if list1 is list3.
list3 = [1, 2, 3]
print("list1 is list3: ", list1 is list3)
print("list1 is not list3: ", list1 is not list3)

# 6. Membership Operators:
# Create a string text = "Python programming is fun!".
text = "Python programming is fun!"

# Check if the word "Python" is in the string.
print("Python in text: ", "Python" in text)

# Check if the word "Java" is not in the string.
print("Java in text: ", "Java" in text)
print("Java not in text: ", "Java" not in text)

# 7. Bitwise Operators (Bonus):
# Perform the following operations with a = 5 and b = 3:
a = 5;
b = 3;

# Bitwise AND (&)
print(a & b)
# Bitwise OR (|)
print(a | b)
# Bitwise XOR (^)
print(a ^ b)
# Bitwise left shift (<<) for a by 1
print ( a << 1)
# Bitwise right shift (>>) for b by 1
print (b >> 1)

# 8. Operator Precedence:
# Write an expression combining +, *, and ** operators. Use parentheses to change the order of operations.
expression_no_parenthesis = 2 + 3 * 4 ** 2;
expression_with_parenthesis = ((2 + 3) * 4) ** 2;
print(expression_no_parenthesis)
print(expression_with_parenthesis)
# Now add parentheses to change the precedence and print the result.

# Evaluate the expression with and without parentheses to see how precedence works.
