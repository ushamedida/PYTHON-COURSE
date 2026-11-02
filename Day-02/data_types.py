#DATA TYPES IN PYTHON:==

#1.NUMERIC DATE TYPES:==It stores the numerical values
number=100
print(number,type(number))
percentage=9.4
print(percentage,type(percentage))
c=2+3j
c2=complex(number)
print(c2,type(c2))
print(c,type(c))
name="hyderabad"
print(name,type(name))


#2.sequence data types:==is used to store the sequence of values

s="hyderabad"
lst=[10,20,30]
t=(1,3,2,4)
print(type(s),type(lst),type(t))

#3.boolean data type:==
#True /False
boole1=True
boole2=False
print(type(boole1))
print(boole1+boole2)

#4.MAPPING DATATYPE:=stores the data in key value pair
d={
    "name":"coadgnan",
    "location":"hyd",
    "branch":4
}
print(d,type(d))

#5.sets:==a set is a collection of unique elements, it does not allow duplicate values and it is unordered
s={10,20,30.4,"gfa",10}
print(s,type(s))


lst1=[] #list()
print(lst1)
t1=()   #tuple()
print(t1),type(t1)
str1=" "  #str()
print(str,type(str))
d1={}  #dic()
s1=set() #do not take {} both of the dict and set,if we take {} for set it will be consider as a dict
print(s1,type(s1))

#INPUT FROM USER:
num=int(input("enter the num"))
print(num)

#TYPE CASTING:==
#implicit type casting:==python automatically converts one data type to another data type
n=10
n1=2.5
c=n+n1
print(c,type(c))

#explicit type casting:manually converting
name=input()
print(name)
n2=int()
print(type(n2))

num1=100
num2=6.74
num3=num1+num2
print(type(num1),type(num2))
print(num3,type(num3))

srt1="nandini"
print(srt1)
lst2=list(srt1)
print(lst2,type(lst2))

set1=set(lst2)
print(set1,type(set1))


num=input()
s=input()
list1=list(map(int,input().split()))
tuple=tuple(map(int,input().split(",")))
set1=set(map(int,input().split(",")))
print(num)
print(s)
print(list1)
print(tuple)
print(set1)