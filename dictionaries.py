# dictionaries intro
# Que. Why we use dictionaries?
# Ans. Because of limitation of lists, lists are not enough to represent real data.

# example
# List = ["ankit","21",["intersteller","fight club"]]
# this list contain user name age and fav movie
# this is also correct but this is not the right way to do that

# Que. what are dictioaries'
# ans. unordered collectionof data in key : value pair

# how to create dictionaries
# user = {"name" : "ankit", "age" : 21}
# print(user)
# second method to create dictionaries
# user1 = dict(name = "ankit", age = "21")
# print(user1)

# to access data in dict.
# print(user["name"])
# print(user["age"])

# which type of data can dict can store
# Ans. ANYTHING


# MOre clean way to create dictionaries
# user_info = {
#     "name" : "ankit",
#     "age" : "21",
#     "fav_movie" : ["fight club", "intersteller"]
# }
# print(user_info["name"])
# print(user_info["age"])
# print(user_info["fav_movie"])


# add data in dictionaries
# user = {}
# user["name"] = "ankit"
# user["age"] = 21
# print(user["name"])

# in keyword and iteration in dictionaries
# user_info = {
#      "name" : "ankit",
#      "age" : 21,
#     "fav_movie" : ["fight club", "intersteller"]
# }
# check  if key exist in dicionaries
# if "name" in user_info:
#     print("present")
# else:
#     print("Not Present")

# check if value present in dictionaries
# if "ankit" in user_info.values():
#     print("present")
# else:
#      print("Not Present")

# if 21 in user_info.values():
#     print("present")
# else:
#      print("Not Present")

# loops in dictionaries
# for keys
# for i in user_info:
#     print(i)

# #for values
# for i in user_info.values():
#     print(i)


# keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)

# values method
# user_info_values = user_info.values()
# print(user_info_values)

# item method
# user_info = user_info.items()
# print(user_info)


# for loop in items

# user_info = {
#      "name" : "ankit",
#      "age" : 21,
#     "fav_movie" : ["fight club", "intersteller"]
# }
# for key, value in user_info.items():
#     print(f"Your key is {key} and value is {value}")


# exercise
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# fav_movies = input("Enter your favourite movies (separate with commas): ").split(",")\

# user_info = {
#     "name": user_name,
#     "age": user_age,
#     "movie": [movie.strip() for movie in fav_movies]
# }

# question = (input("What do you want to know about user?(name, Age, movie) ")).lower()

# if question == "name":
#     print(f"User name is {user_info['name']}")
# elif question == "age":
#     print(f"User age is {user_info['age']}")    
# elif question == "movie":
#     print(f"User's favourite movies are {user_info['movie']}")
# else:
#     print("Invalid request")


# add data in dictionaries
# user_info = {}
# user_info["name"] = "ankit"
# user_info["age"] = 21
# user_info["height"] = 178
# print(user_info)

# pop method
# popped_item = user_info.pop("height")
# print(f"Popped item: {popped_item}")
# print(user_info)

# pop item method
# popped_item = user_info.popitem()
# print(f"Popped item: {popped_item}")
# print(user_info)


# update dictionaries
# user_info = {
#      "name" : "ankit",
#      "age" : 21,
#     "fav_movie" : ["fight club", "intersteller"]
# }

# other_info = {"state" : "haryana", "fav_songs" : ["sajjan razzi" , "tu jo na kaha"]}

# user_info.update(other_info)#update this dictionarie to selected dictionarie
# print(user_info)
# if two dictionaries has same key new one will replace old one


# from keys method
# d = dict.fromkeys(["name" , "age"], 'unknown')
# print(d)

# get method
# d = {"name" : "ankit", "age" : 21}
# print(d.get("name"))

# clear method
# d = {"name" : "ankit", "age" : 21}
# d = print(d.clear())

# copy method
# d = {"name" : "ankit", "age" : 21}
# d1 = d.copy()
# print(d1)

# exercise
# def cube_finder(n):
#    cube = {}
#    for i in range(1,n+1):
#       cube[i] = i**3
#    return cube

# num = int(input("Enter a number: "))
# print(cube_finder(num))
