#SETS:=
#sets are unordered collection of unique elements
#sets are mutable, meaning you can change their content without changing their identity.
#sets are defined using curly braces {} or the set() function.
#Creating a set
my_set = {1, 2, 3, 4, 5}
my_set=set()
my_set2={}
print(my_set,type(my_set),type(my_set2))

#SET METHODS:=
#1. add(): Adds an element to the set.
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
#2. remove(): Removes an element from the set. Raises a KeyError if the element is not found.
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
#3. discard(): Removes an element from the set if it is present. Does not raise an error if the element is not found.
my_set.discard(4)
print(my_set)  # Output: {1, 2, 5, 6}
#4. pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
my_set.pop()
print(my_set)  # Output: {2, 5, 6}
#5. clear(): Removes all elements from the set.
my_set.clear()
print(my_set)  # Output: set()
#6.copy(): Returns a shallow copy of the set.
my_set2 = {1, 2, 3}
print(my_set2.copy())  # Output: {1, 2, 3}


#SET OPERATIONS:=
#1. union(): Returns a new set with all elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
#2. intersection(): Returns a new set with elements that are common to both sets.
print(set1.intersection(set2))  # Output: {3}
#3. difference(): Returns a new set with elements that are in the first set but not in the second set.
print(set1.difference(set2))  # Output: {1, 2}
#4. symmetric_difference(): Returns a new set with elements that are in either of the sets but not in both.
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}
#5. issubset(): Returns True if all elements of the first set are in the second set.
print(set1.issubset(set2))  # Output: False
#6. issuperset(): Returns True if all elements of the second set are in the first set.
print(set1.issuperset(set2))  # Output: False
#7. isdisjoint(): Returns True if the two sets have no elements in common.
print(set1.isdisjoint(set2))  # Output: False
#8. len(): Returns the number of elements in the set.
print(len(set1))  # Output: 3







9