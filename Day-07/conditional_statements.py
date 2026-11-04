#CONDITIONAL STATEMENTS:==
#key words to control the flow of a program based on certain conditions.
#used to make the decision based on the condition on True or False.
#TYPES OF CONDITIONAL STATEMENTS:
#1.if 
#2.elif
#3.else
#4.nested if

#1.if statement:==
#The if statement is used to test a specific condition. If the condition is true, the block of code inside the if statement is executed. If the condition is false, 
# the block of code is skipped.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    
#2.elif statement:==
#The elif statement is used to test multiple conditions. It stands for "else if" and allows you to check additional conditions if the previous ones are false.
# If the condition in the elif statement is true, the block of code inside it is executed.
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")

#3.else statement:==
#The else statement is used to define a block of code that will be executed if none of the previous conditions are true.
# It acts as a fallback option when all other conditions fail.
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age.")
else:
    print("valid age.")

#MARKS:
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >=75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


#Fizz Buzz Problem:==
#if num divisible by 3 and 5 print FizzBuzz, if divisible by 3 print Fizz, if divisible by 5 print Buzz, else print the number.
num = int(input("Enter a number: "))
if num % 3== 0 and num % 5==0:
    print("FizzBuzz")
elif num % 3==0:
    print("Fizz")
elif num % 5==0:
    print("Buzz")
else:
    print(num)

#we can not do this following:
if num % 3==0:
    print("Fizz")
elif num % 5==0:
    print("Buzz")                       #THIS IS WRONG BECAUSE IF THE NUMBER IS DIVISIBLE BY BOTH 3 AND 5, IT WILL PRINT FIZZ AND NOT FIZZBUZZ.
elif num % 3==0 and num % 5==0:
    print("FizzBuzz")


#4.Nested if statement:==
#A nested if statement is an if statement that is placed inside another if statement.
# It allows you to test additional conditions within the block of code of the outer if statement.
a= int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a > 0:
    if b > 0:
        print("Both numbers are positive.")
    else:
        print("The first number is positive, but the second number is not.")
else:
    print("The first number is not positive.")

#GREATEST AMONG THREE NUMBERS:==
#a= int(input("Enter a number: "))
#b=int(input("Enter another number: "))
#c= int(input("Enter another number: "))
a,b,c=map(int,input("enter three numbers:").split())
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")

x,y,z=(map(int,input("enter three numbers:").split(",")))
if x>y:
    if x>z:
        print("x is greatest")
    else:
        print("z is greatest")
elif y>z:
    if y>x:
        print("y is greatest")
    else:
        print("x is greatest")
elif z>x:
    if z>y:
        print("z is greatest")
    else:
        print("y is greatest")
else:
    print("all are equal")
