# 1. Sum of List Elements
# Create a function sum_list(numbers) that takes a list of numbers and returns their sum.
# Use a loop to iterate through the list.
# Use a variable to accumulate the total and return it.
numbers=[1,2,3];

def sum_list(numbers):
    total=0;
    for num in numbers:
        total += num
    # print(total)
    return total


# 2. Repeated Greeting
# Write a function repeat_greeting(name, times) that prints a greeting to name a specified number of times.
# Use a loop to print the greeting repeatedly.
# Each greeting should be printed on a new line.
def repeat_greeting(name,times):
    for i in range(times):
        print(f"Hello {name}")

# repeat_greeting("Harry", 5);

# 3. Factorial Calculation
# Define a function factorial(n) that returns the factorial of a given number n.
# Use a loop (such as a for or while loop) to multiply numbers from 1 to n.
# Return the factorial result.
def factorial(n):
    result = 1;
    for i in range(1, n + 1):
        result *= i
    return result;

factorial_result = factorial(5);
print(factorial_result)

# 4. Fibonacci Sequence Generator
# Create a function fibonacci(n) that returns a list containing the first n numbers of the Fibonacci sequence.
# Use loops and conditionals to calculate each Fibonacci number.
# Start the sequence with 0 and 1, then build the sequence up to n terms.
def fibonacci(n):
    fib_sequence = [];
    a, b = 0, 1;
    for _ in range(n):
        fib_sequence.append(a);
        a, b = b, a + b;
    return fib_sequence;

print("fibonacci sequence", fibonacci(10));

# 5. Maximum of Two Numbers
# Write a function max_of_two(a, b) that returns the larger of two numbers.
# Use an if...else conditional to compare a and b.
# Return the greater value.
def max_of_two(a, b):
    if a > b:
        return a;
    elif b > a:
        return b;
    else:
        return f"{a} and {b} are equal."

print(max_of_two(6,6))
# 6. Print a Pattern with Nested Loops
# Design a function print_triangle(rows) that prints a right-angled triangle of asterisks (*) with a given number of rows.
# Use nested loops: an outer loop for rows and an inner loop for printing asterisks in each row.
# Each subsequent row should have one more asterisk than the previous row.
def print_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i);

print_triangle(5)
