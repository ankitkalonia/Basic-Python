## data structures
###lists
## we can store items in lists
# numbers = [1,2,3]
# print(numbers)
# print(numbers[2]) ##to print selected item

# words = ["word1" ,"word2" ,"Word3"]
# print(words)
# print(words[:2]) ##slicing

# mixed = [1,2,3, "word",True , 3.14 ,None]
# print(mixed)
# print(mixed[-1])
# mixed[3] = "two" ##change item in lists
# print(mixed)

########add item to lists##########
####append method(add data in last of list)
# fruits = ["apple" , "mango"]
# fruits.append("grapes")
# print(fruits)
#####add data in empty lists
# fruits = []
# fruits.append("apple")
# fruits.append("mango")
# print(fruits)
##########to add data in list anywhere
# fruits1 = ["mango", "apple"]
# fruits1.insert(1,"grapes")###add item in that position
# print(fruits1)

##########join(concatenate) two lists
# fruits1 = ["apple", "mango"]
# fruits2 = ["grapes", "pineapple"]
# fruits3 = fruits1 + fruits2
# print(fruits3)

########extend method
# fruits1 = ["apple", "mango"]
# fruits2 = ["grapes", "pineapple"]
# fruits1.extend(fruits2)
# print(fruits1)

#############methods to deletes items in list
# fruits = ["apple", "mango", "grapes", "pineapple"]
###pop method
# fruits.pop() ###deletes last item in list
# fruits.pop(2)###to delete specific item in list
####del operator
# del fruits[1]
####remove method
# fruits.remove("apple")
# print(fruits)
#####count method
# print(fruits.count("apple"))
#######sort method (works with numbers and words)
# fruits.sort()
# print(fruits)
########clear method (empty the list)
# fruits.clear()
# print(fruits)
#####copy method
# copied = fruits.copy()
# print(copied)
######reverse method
# fruits.reverse()
# print(fruits)
#######in_list
# fruits = ["apple", "mango", "grapes", "pineapple"]
# if "pear" in fruits:
#     print("present")
# else:
#     print("not present")
##########compare lists
# fruits1 = ["apple", "mango", "grapes", "pineapple"]
# fruits2 = ["pear", "banana", "kiwi"]
# print(fruits1 == fruits2) ###checks the values
# print(fruits1 is fruits2) ###checks if objects is same memory

##########split and join
##spilt method
#converts string to list
# user_info = "ankit , 21"
# user_info = user_info.split(",")
# print(user_info)
###join method
# user_info = ["ankit", "21"]
# print(",".join(user_info))
#######Loop in lists
# fruits = ["apple", "mango", "grapes", "pineapple"]
####for loop
# for fruit in fruits:
#     print(fruit)
####while loop
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1
#####list inside list ## 2d list
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0])

# for sublist in matrix:
#     for i in sublist:
#         print(i)
##specific item in specific list inside list
# print(matrix[1][1])
#########index method #to find place of item in list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 6, 7, 8, 9]
# print(numbers.index(1))
##if more than one same item
# print(numbers.index(1,2,10))###1st num to find, second num where to start searching,third num where to end searching
###exercise
# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i*i)
#     return square
# numbers = list(range(1,11))
# print(square_list(numbers))
######exercise to reverse list
# def reverse_list(l):
#     empty_list = []
#     for i in range(len(l)):
#         del_item = l.pop()
#         empty_list.append(del_item)
#     return empty_list
# numbers = [1, 2, 3, 4, 5, "word1"]
# print(reverse_list(numbers))

#######exercise
# def rev_list(l):
#     empty_list = []
#     for i in range(len(l)):
#         del_item = l.pop()
#         empty_list.append(del_item)
#     return empty_list
# number = [[1 ,2, 3],[4, 5, 6],[7, 8, 9]]
# print(rev_list(number))

##method 2
# def rev_list(l):
#     return[name[::-1] for name in l]
# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# print(rev_list(numbers))
####exercise
# def odd_even(l):
#     odd_list = []
#     even_list = []
#     for i in range(len(l)):
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     return [odd_list,even_list]

# num = [1,2,3,4,5,6,7,8,9,0]            
# print(odd_even(num))
#####exercise to check commmon item in two lists
# def common_chk(l1,l2):
#     output = []
#     for i in l1:
#      if i in l2:
#         output.append(i)
#     return output
# list_1 = [1,3,5,7,9]
# list_2 = [1,2,3,4,5,6,7,8,9]
# print(common_chk(list_1,list_2))
#####min  and max function
# num = [2,6,9]
# print(min(num))
# print(max(num))
        
######exercise
# def max_min_diff(l):
#     return max(l) - min(l)
# num = [2,6,9]
# print(max_min_diff(num))
######exercise ##sublist counter
# def sublist_count(l):
#     sublist = 0
#     for i in l:
#         if type(i) == list:
#             sublist += 1
#     return sublist

# num = [1,2,3,[4,5,6],[7,8,9]]
# print(sublist_count(num))