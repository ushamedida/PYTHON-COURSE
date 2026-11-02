
#Dictionaries in Python
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change their content without changing their identity.
## Creating a dictionary
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}
print(student)
#Accessing values in a dictionary
print(student["name"])  # Output: John Doe
print(student["age"])   # Output: 20
print(student["grade"]) # Output: A
#adding new key-value pairs
student["major"] = "Computer Science"
print(student)  # Output: {'name': 'John Doe', 'age': 20, 'grade': 'A', 'major': 'Computer Science'}
#Updating values in a dictionary
student["age"] = 21
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'grade': 'A', 'major': 'Computer Science'}
#removing key-value pairs
student.pop("grade")
print(student)  # Output: {'name': 'John Doe', 'age': 21}
student.popitem()
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'major': 'Computer Science'}
student.clear()
print(student)  # Output: {}
del student["grade"]
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'major': 'Computer Science'}
