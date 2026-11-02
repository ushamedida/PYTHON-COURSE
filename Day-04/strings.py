str1="My fav subject is Python Programming Language@123"
print(str1,type(str1))
#accessing
print(str1[0])
print(str1[1])
print(str1[-1])#retrieves the last character of the string.
#slicing
print(str1[0:3])
print(str1[ :4])
print(str1[2:])
print(str1[::-1])#reverses the string

print(str1.lower())#converts the string into lower case.
print(str1.upper())#converts the string into upper case.
print(str1.title())#converts the first character of each word to upper case.
print(str1.capitalize())#converts the first character of the string to upper case and the rest to lower case. 
print(str1.islower())#check whether the string is in lower case or not.
print(str1.isupper())#check whether the string is in upper case or not
print(str1.isalnum())#check whether the string is alphanumeric or not
print(str1.isalpha())#check whether the string is alphabetic or not.
print(str1.isdigit())#check whether the string is digit or not.
print("   ".isspace())#check the string contains only whitespace characters or not.
print("1343".isdigit())#check whether the string is digit or not.
print(str1.count("s"))#count the number of occurrences of a substring in the string.
print(str1.strip())#removes the leading and trailing whitespace characters from the string.
print(str1.lstrip())#removes the whitespace from left side
print(str1.rstrip())#removes the whitespace from right side
print(str1.split(" , "))#it converts string into list

words=str1.split()
print(len(words))

combined_string=" ".join(words)#it converts list into string.
print(combined_string)