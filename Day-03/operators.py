#OPERATORS:
#1.ARITHMETIC OPERATORS:=USED TO PERFORM ARITHMETIC OPERATIONS
#2.COMPARISON OPERATORS:=USED TO COMPARE VALUES
#3.LOGICAL OPERATORS:=USED TO COMBINE CONDITIONAL STATEMENTS
#4.ASSIGNMENT OPERATORS:=USED TO ASSIGN VALUES TO VARIABLES
#5.BITWISE OPERATORS:=USED TO PERFORM BITWISE OPERATIONS
#6.MEMBERSHIP OPERATORS:=USED TO TEST IF A SEQUENCE IS PRESENT IN AN OBJECT
#7.IDENTITY OPERATORS:=USED TO COMPARE OBJECTS, NOT IF THEY ARE EQUAL, BUT IF THEY ARE ACTUALLY THE SAME OBJECT,
#   WITH THE SAME MEMORY LOCATION

#1.ARITHMETIC OPERATORS:==+,-,*,/,%,**,//
a=10
b=20
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division
print(a%b) #modulus
print(a**b) #exponentiation
print(a//b) #floor division

#2. RELATIONAL or COMPARISON OPERATORS:==>,<,>=,<=,==,!=
a=10
b=20
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to
print(a==b) #equal to
print(a!=b) #not equal to

#3.LOGICAL OPERATORS:==and,or,not
a=10
b=20
print(a>5 and b>15) #and
print(a>5 or b>15) #or
print(not(a>5 and b>15)) #not

#4.ASSIGNMENT OPERATORS:===,+=,-=,*=,/=,%=,//=,**=
a=10
b=20
a+=b #a=a+b
print(a)
a-=b #a=a-b
print(a)
a*=b #a=a*b
print(a)
a/=b #a=a/b
print(a)
a%=b #a=a%b
print(a)
a//=b #a=a//b
print(a)
a**=b #a=a**b
print(a)
#5.BITWISE OPERATORS:==&,|,^,~,<<,>>
a=10
b=20
print(a&b) #bitwise and
print(a|b) #bitwise or
print(a^b) #bitwise xor
print(~a) #bitwise not or complement
print(a<<2) #left shift
print(a>>2) #right shift
#6.MEMBERSHIP OPERATORS:==in,not in
a=[10,20,30,40,50]
print(10 in a) #True
print(60 in a) #False
print(60 not in a) #True
s="hello"
print("H" in s)
#7.IDENTITY OPERATORS:==is,is not
a=10
b=10
print(a is b) #True
print(a is not b) #False
a=[10,20,30]
b=[10,20,30]
print(a is b)
print(a is not b)
x=[1,2,3]
y=x
print(x is y)



