
# str = "Hello how are you"
# print(str[0:5:1] , str[6:9:1],str[14:17:1])

# name = "sikandar"
# age = 21
# print(f"hi my name is {name} and my age is {age}")

# name = input("Please enter you name")
# age  = int(input("please enter your age"))

# if age >=18:
#     print(f"congrats {name} and age is {age} are a valid voter")
# elif age < 18 and age > 0 :
#  print(f"Sorry {name} and age is {age} you cannot vote")
# else:
#    print("Please enter a valid age ")
# sum = 0
# for i in range(1,6):
#     sum+= i

# print(sum)


computer = 67
tries = 1
i = int(input("enter the number:---"))

while i != computer:
    
    if i <=50:
        i = int(input("sorry guees the number grater then 50")) 
        tries = tries + 1
    elif i >= 75:
        i = int(input("You entered the wrong number guess the number below 75"))
        tries = tries + 1
    elif i > computer :
        i = int(input("guess the number little below")) 
        tries = tries + 1
    elif i < computer:
        i = int(input("guessthe number little above "))
        tries = tries + 1
      
    
print(f" congrats,you number is {i} and computer number is {computer} your tries num is {tries}")  