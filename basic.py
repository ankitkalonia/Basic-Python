n1 = int(input("Enter your first number :"))
n2 = int(input("Enter your second number :"))
n3 = int(input("Enter your third number :"))
print(f"Your average is: ",int((n1 + n2 + n3)/3))
######################
# String Indexing

name= "ankit"

# positions(index numbers)
a=0, -5
n=1, -4
k=2, -3
i=3, -2
t=4, -1
print(name[2])
print(name[-4])
######################################
# slicing/ selecting sub sequences

name= ("ankit")
# syntax=[start argument : end argument]
print(name[1:5])

# syntax=[start argument : stop argument : step]
print(name[-1::-1])
######################################
# Exercise to reverse your name
name=input('enter your name: ')
print(f"Your reverse name is: {name[::-1]}")
#########################################
#string methods
name= "ANKIT Kalonia"
#1. len() function
print(len(name))
#2. lower() method
print(name.lower())
#3. upper() method
print(name.upper())
#4. Title() Method
print(name.title())
#5. count() method
print(name.count(" "))
s1= "The quick brown fox jumps over the lazy dog"
# 6. replace() Meathod
print(s1.replace(" ","_",3))
# 7. Find() method
print(s1.find("fox"))
# 8. centre method
n1= "Ankit"
print(n1.center(9,"#"))
# exersise
name=input("Enter your name: ")
char=len(name)
nos= int(input("Enter ther number of stars you want on both side of your name: "))
ns=(nos*2)
npd=(char + ns)
print(name.center(npd,"*"))
# M2#
name = input("Enter your name : ")
name = name.replace(" ","")
char_in_name = len(name)
num_of_stars = int(input("Enter number of starts : "))
name_with_stars = name.center(char_in_name + 2*num_of_stars, "*")
print(name_with_stars)
#######################################################
#########if condition################ 
age = int(input("Enter your age: "))
if age >= 14:
    print("Welcome, You are Eligible")
else:
    print("Sorry, You are Not Eligible")
############Guessing Game##############
win_num = 63
guess_num = int(input("Guess a numbner between 1 to 100: "))
if guess_num == win_num:
    print("you won")
else:
    if guess_num < win_num:
        print("too low")
    else:
        print("too high")
##############and operator##########
correct_user_name = "ankit"
correct_age = "21"
input_user_name = input("enter your name: ")
input_user_age = input("Enter your age: ")
input_user_name = input_user_name.lower().replace(" ","")
input("Verifying....Please press 'Enter' to continue")

if correct_user_name == input_user_name and correct_age == input_user_age:
    print("Identity verified succesfully, Welcome " + correct_user_name)

elif correct_user_name != input_user_name and correct_age == input_user_age:
    print("Wrong username.Please try again")

elif correct_user_name != input_user_name and correct_age != input_user_age:
    print("Wrong username and age. Try again")

else:
    print("Age mismatched, Try again")
###########Exercise##############
user_name = input("What is your name: ")
user_age = input("What is your age: ")
user_age = int(user_age)
name_first_letter = (user_name[0])
if user_age >= 10 and (name_first_letter == "a" or name_first_letter == "A"):
    print("welcome, You can watch coco") 
else:
    print("sorry you can't watch coco")
################exercise###############
user_age = input("Enter your age: ")
user_age = int(user_age)
if 1 >= user_age <= 4:
    print("Your ticket is free")
elif 5 <= user_age <=10:
    print("Your ticket price is ₹150")

elif 11 <= user_age <=60:
    print("Your ticket price is ₹250")

elif user_age >=61:
    print("Your ticket price is ₹200")
##########In Keyword############
####If with in########
name = "ankit"
if "a" in name:
    print("present")
else:
    print("not present")
#####check empty or not############
name = "abc"
if name: ##checking in string for anything.;. true if not empty
    print("not empty")
else:
    print("empty")
###exercise####
user_name = input("Enter your name: ")
user_name = user_name.replace(" ","")
if user_name:
    print("Welcome "+ user_name)
else:
    print("You did not enter any name")
##############Loops#############
###While loops and for loops############
## while loops
#print hello world 10 times
i = 1
while i<=10:
    print(f"{i} Hello world")
    i = i + 1
#sum of 1 to 20 
i = 1
sum = 0
while i <= 20:
    sum += +i
    i += + 1
print(sum)
##########exercise###########
number = input("Enter your number: ")
number = int(number)
i = 1
sum = 0
while i <= (number):
    sum += +i
    i += +1
print(sum)
##########exercise###########
name = input("Enter your name: ")
lenght = int(len(name))
counted = ""
i = 0
while i < lenght:
    if name[i] not in counted:
        counted += name[i]
        print(name[i] , name.count(name[i]))
    i = i + 1
##########for loop##############
for i in range(1,11):
    print(f"hello world : {i}")
#########exercise#############
num = input("Enter the number: ")
num = int(num)
total = 0
for i in range(1,num+1):
    total = total + i
print(total)
##########exercise###############
user_num = input("Enter your number:")
total = 0
for i in range(0,len(user_num)):
    total += int(user_num[i])
print(total)
###########exercise##############u
name = input("Input your name:")
temp = ""
for i in range (0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
    temp += name[i]
#########break and continue###########
########break#######(stop)
for i in range(1,11):
    if i == 5:
        break
    print(i)
#######continue#########(skip)
for i in range(1,11):
    if i == 5:
        continue
    print(i)
##########number guessing game###########
import random
winning_num = int(random.randint(1,100))
# print(winning_num)
guess_num = int(input("Guess the number between 0 to 100: "))
guesses = 1
game_over = False
while not game_over:
    if winning_num == guess_num:
        print(f"You won! you guess the number in {guesses} guesses")
        game_over = True
    else:
        if guess_num < winning_num:
            print("Too low")
        else:
            print("Too high")
    guess_num = int(input("guess again: "))
    guesses += 1
    ########step argument##########
for i in range(1,11,2):  #third is step argument 
    print(i)

for i in range (10,0,-1):
    print(i)

######for loop in strings in python###########
num = input("enter a number: ")
total = 0
for i in num:
    total += int(i)
print(total)
