# list comprehension
# using list comprihension we can create list in onle line of code

# list of square of numbers
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

# using list comprehension
# square2 = [i**2 for i in range(1,11)]
# print(square2)

# ex
# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# lc
# negative2 = [-i for i in range(1,11)]
# print(negative2)

# exercise
# old method
# def rev_list(l):
#     empty_list = []
#     for items in l:
#         empty_list.append(items[::-1])
#     return empty_list
# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# print(rev_list(numbers))


# using list comprehension
# def rev_list(l):
#     return[name[::-1] for name in l]
# numbers = [[1,2,3],[4,5,6],[7,8,9]]
# print(rev_list(numbers))

# List comprehension with if statements
# print list of even numbers
# numbers = [1,2,3,4,5,6,7,8,9]
# even_nums = [i for i in numbers if i%2 == 0]
# print(even_nums)

# list of odd numbers
# numbers = [1,2,3,4,5,6,7,8,9]
# odd_nums = [i for i in numbers if i%2 != 0]
# print(odd_nums)

#list comprehension with if else

# num = [1,2,3,4,5,6,7,8,9]
# output = odd = -i and even = i*2

# old method
# new_list = []
# for i in num:
#     if i % 2 != 0:
#         new_list.append(-i)
#     else:
#         new_list.append(i*2)
# print(new_list)

#using list comprehension
# new_list = [-i if (i%2!=0) else i*2 for i in num]
# print(new_list)

#list comprehension in nested lists
# example = [[1,2,3],[1,2,3],[1,2,3]]
# nested = [[i for i in range(1,4)] for j in range(3)]
# print(nested)