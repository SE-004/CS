# You have a string s composed only of the characters (, ), {, }, [ and ]. 
# Determine if the bracket arrangement in this string is valid. Specifically, 
# a valid string must meet the following criteria:

    # Each opening bracket has a corresponding closing bracket of the same type.
    # Brackets are closed in the correct order.
    # Every closing bracket matches an earlier opening bracket of the same type.

input1 = "()";
input2 = "() [] {}"
input3 = "([])";
input4 = "(]";

def isValid(string):
    stack = [];
    mapping = {")": "(", "]": "[", "}": "{"};
    for char in string:
        if char in mapping:
            top_element = stack.pop() if stack else "#";
            if mapping[char] != top_element:
                return False;
        else:
            stack.append(char);
    return not stack;

print(isValid(input1))
print(isValid(input2))
print(isValid(input3))
print(isValid(input4))

