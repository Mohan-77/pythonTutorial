# COMPARISON OPERAOTRS
""" 
== - equals to
!= - not equals to
> - greater than
>= - greater than or equal to
< - less than
<= - less than or equal to
"""
num1 = 90
num2 = 90
if num1 == num2:
    print("Same")
else:
    print("Not same")

name1 = "ali"
name2 = "aden"
if len(name1) == len(name2):
    print("same letters")
else:
    print("not same letters")

# LOGICAL OPERAOTRS
# and operator
isFeesCleared = True
grade = "B"
if isFeesCleared and grade == "A":
    print("You are going to the trip")
else:
    print("Sorry, You are not going to the trip")


# or operator
if isFeesCleared or grade == "A":
    print("You are going to the trip")
else:
    print("Sorry, You are not going to the trip")