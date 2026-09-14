########functions##########
def add_two(x,y):
    return x+y #or print x+y(no neeed to print)
a = int(input("enter a number: "))
b = int(input("enter a number: "))
total = add_two(a,b)
print(total)
######exercise########
def last_char(x):
    return(name[-1])
name = input("enter your name: ")
char = last_char(name)
print(f"Last character is {char}")
#########exercise#############
def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
number = int(input("enter a number: "))
check = odd_even(number)
print(check)
#######true false#############
def is_even(num):
    if num%2 ==0:
        return "True"
    else:
        return "False"
number = int(input("enter a number: "))
check = is_even(number)
print(check)
########another way############
def is_even(num):
    return num%2 == 0
print(is_even(21))
##########exercise###########
def big_num(a,b,c):
        if a >= b and a >= c:
                return a
        
        elif b >= a and b >= c:
                return b
        
        else:
                return c
        
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

check = big_num(x ,y ,z)
print(f"The biggest number is {check}")
#########exercise###########
def is_palindrom(word):
        if word == word[::-1]:
                return "True"
        return "False"
##or
        ## return word == word[::-1]
name = input("enter your name: ")
check = is_palindrom(name)
print(check)
##########default parameter###########
def user_info(first_name , last_name , age):
    print(f"Your first name is {first_name}. your last name is {last_name}. your age is {age}")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
user_info(first_name , last_name , age)
###########scope############
x = 5 ##global value
def func():
    global x ##change the global value to local
    x = 7 ##local value
    return x
print(x) ##before func call remain same to global (value remains 5)
print(func())
print(x) ##after func call it changes to local value (changes to 7)
