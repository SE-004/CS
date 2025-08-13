age = 12;

if age >= 100:
    print("Invalid age");
elif age >= 18:
    print("You are an adult!");
elif age > 12:
    print("You are a minor")
elif age >= 0:
    print("You are a child")
else:
    print("Invalid age.")

status = "Adult" if age >= 18 else "Minor";

print(status);

# match
grocery = ["milk", "eggs", "butter", "milk"];

 
# num = int(input("Guess what number I am thinking about? "))

# while num != 4:
#     num = int(input("Try again"));
#     print("Number from the user", num);


# for item in grocery:
#     print(item);

# for item in grocery:
#     if "milk" in grocery:
#         grocery.remove("milk");
#     else:
#         break;

# print(grocery.count("milk"));

# for i in range(grocery.count("milk")):
#     grocery.remove("milk");

# print(grocery)

# print(grocery.index("milk"));

# enumerate function
indexes = [];

# for index, value in enumerate(grocery):
#     if "milk" == value:
#         indexes.append(index);

# print(indexes);

numbers = [1,6,2,5,3,4];

# for num in numbers:
#     for j in numbers:
#         print(num * j);


person = {
    "name": "Alice",
    "age": 34,
    "address": {
        "city": "Berlin",
        "street": "Gartenstr",
        "postalcode": 11111
    }
}

for key in person.keys():
    if key == "address":
        for sub_key in person[key].keys():
            print(f"Sub Key: {sub_key}, Value: {person[key][sub_key]}");
    else:
        print(f"Key: {key}, Value: {person[key]}");
