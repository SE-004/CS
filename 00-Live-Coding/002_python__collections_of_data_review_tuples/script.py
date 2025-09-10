# Write your code here
### Activity 1: Personal Information

# 1.  Create a tuple: `info = ("Alice", 28, "Paris")`
info = ("Alice", 28, "Paris")
# 2.  Unpack the tuple into 3 variables.
name, age, city = info
# 3.  Print: `"Alice is 28 and lives in Paris."`
print(f"{name} is {age} and lives in {city}")

# ### Activity 2: Immutable Test

# 1.  Try changing the age in the `info` tuple.
info = ("Alice", 25, "Paris");
print(info);

# info[1] = 26;
# print(info);

# 2.  Observe and write down the error message.
# TypeError: 'tuple' object does not support item assignment

# 3.  Convert the tuple to a list, change the value, and convert it back.
info_list = list(info)
info_list[1] = 26
print(info_list)
info = tuple(info_list)
print(info)

# ### Activity 3: Tuple of Coordinates

# 1.  Create a tuple representing the longitude of a point `lon = ('longitude', 10)`.
lon = ('longitude', 10)    
# 2.  Unpacked the values of `lon` and print them.
lon1, lon2 = lon
print(lon1, lon2)    
# 3.  Create a new tuple with the latitude named `lat`.
lat = (15, 'latitude')
# 4.  Unpack the values and print them. 
lat1, lat_label = lat
print(lat1, lat_label)
# 5.  Create a new tuple named `coordinates` and join the two tuples `lon` and `lat`.
coordinates = lat + lon 
print(coordinates)
# 6.  Unpack the `coordinates` tuple only into the necesary variables to form a multi-line sentence 
# like: `"The coordinates to my favorite place are:                               
#               longitude = [longitude value]   
#               latitude = [latitude value]`.
lat, *rest, lon = coordinates;



# 7.  Print the sentence.      
print(f"""The coordinates to my favorite place are:
    longitude = {lon}
    latitude = {lat} """)
print(rest)