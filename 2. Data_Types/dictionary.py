"""
dictionary helps us to store in key-value pairs

key -> unique identifier

value -> can be any immutable data types
"""

student = {'name': 'Abhishek', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])

# print(student.get('phone')) # using this wont give error or No Key

# we can also pass the default value if not found
print(student.get('phone', 'nooo phooonnee'))


# deleting a key
# del student['age']

# pop method -> returns the popped value
# age = student.pop('age')

print(student)

# length of the dictionary
print(len(student))

# get only keys
print(student.keys())

# get only values
print(student.values())

# get in pairs
print(student.items())


# looping to get key and value

for key, value in student.items():
    print(key, value)





