#LIST:=
#a list is a ordered collection of items which can be of any data type.
# Lists are mutable, meaning that their contents can be changed after they are created. 
# Lists are defined using square brackets [] and can contain duplicate elements.
lst1=[1,2,3,4,5]
print(lst1)
print(lst1[0])
print(lst1[0:1])
print(lst1[2:4])
print(lst1[::-1])
#LIST METHODS
#1.append() method is used to add an element at the end of the list.
lst1.append(6)
print(lst1)
lst1.append([10,20,30])
print(lst1)
print(lst1[6][1])
#2.extend() method is used to add multiple elements at the end of the list.
lst1.extend([7,8,9])
print(lst1)
#3.insert() method is used to add an element at a specific index in the list.
lst1.insert(0,100)
print(lst1)
#4.REMOVING
#a.remove() method is used to remove the first occurrence of a specific element from the list.
lst1.remove(100)
print(lst1)
#if any number is not present in the list then it will give an error.we can use if condition to check whether the number is present in the list or not.
if 100 in lst1:
    lst1.remove(100)
    print(lst1)
lst4=[1,2,3,4,5,6,7,8,9]
#b.pop() method is used to remove an element at a specific index from the list.
lst4.pop(0)
print(lst4)
print(lst4.pop())#removes the last element from the list and returns it.
print(lst4.clear())#removes all the elements from the list.
lst5=[1,2,3,4,5]
del lst5[0]#deletes the element at index 0 from the list.
print(lst5)

#5.sorting:=
lst2=[12,56,73,45,85,23,45,67,89,90]
lst2.sort()#alters the original list and sorts it in ascending order.
print(lst2)
lst2.sort(reverse=True)
print(lst2)#displays the list in descending order.

sorted_lst=sorted(lst2)#sorted() function returns a new sorted list without modifying the original list.
print(sorted_lst)
#6.copying:=
l1=[1,2,3,4,[2,3,6]]
l2=l1.copy()#creates a shallow copy of the list.
print(l2)



