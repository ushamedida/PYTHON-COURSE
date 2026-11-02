#TUPLES:==
# A tuple is an ordered collection of items which can be of any data type.
#creating and accessing tuples:=
tup1=(1,2,3,4,5)
print(tup1)
print(tup1[0])
print(tup1[-3])
print(tup1[0:1])
print(tup1[::-1])

#1.concatenation:=
tup2=(6,7,8,9,10)
tup3=tup1+tup2
print(tup3)

#2.repeating:=
tup4=tup1*3
print(tup4)

#3.looping through tuples:=
for i in tup1:
    print(i)

#4.immutability:=
#tuples are immutable, meaning that their contents cannot be changed after they are created.
tup5=(1,2,3,4,5)
#tup5[0]=100#this will give an error because tuples are immutable.
print(tup5)

