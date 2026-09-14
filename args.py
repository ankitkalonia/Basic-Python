# Making flexible functions

# *operators
# *args

# def total(a,b):
#     return a+b
# print(total(3,4))

#what if i want to enter multiple entry in function

# def all_total(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(all_total(1,2,3,4,5,6,7,8,9)) 

#*args with normal partameter ankiotr kalonia jangra

# def all_multiply(nums,*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total
# print(all_multiply(2,3,4)) #first will be parameter after that args

#args with list,tuples
# def all_multiply(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total
# nums = (2,3,4)
# print(all_multiply(*nums)) #by adding star before we can pass touple or list in function


#exercise

# def to_power(num, *args):
#     if args:
#         return[i**num for i in args]
#     else:
#         print("You didn't enter any numbers")

# numbers = (3,2,3,4,5,6)
# print(to_power(*numbers))


# **kwargs

def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func(first = "ankit", last = "kalonia")

