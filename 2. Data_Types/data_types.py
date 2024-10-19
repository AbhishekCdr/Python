
# DATA TYPES:

# Strings

message = "Hello World"

"""
print(message)

# length of the message
print(len(message))

# access location
print("location at 0th index", message[4])

# access range 
print("hello from hello world: ", message[0:5])

# 6th index till last
print(message[6:])

# lower case 
print(message.lower())

# upper case
print(message.upper())

# count method
print(message.count('H'))
 
# find method
print(message.find('World'))
# -> return -1 of not found

# replace method
new_message = message.replace('World', 'Universe')
# not in-place method / saves it to new variable

print(new_message) 

# using placeholder for concatination
greeting = 'Hello'
name = 'Abhishek'

greet = '{}, {}. Welcome!'.format(greeting,name)

print(greet)

# using f string / support on python 3.6+

greetf = f'{greeting}, {name}. Welcome!'
print(greetf)

# find all attributes and methods available
print(dir(name))

# to get details insight 
print(help(str))

"""

# Integer and Float

"""

Arithematic Operations:

Addition: 3 + 2
Subtraction: 3 - 2
Multiplication: 3 * 2
Division: 3 / 2
Floor Division: 3 // 2
Exponent:  3 ** 2
Modulus: 3 % 2

"""

print(3/2)
print(3//2) #-> removes decimal

# incremanting values

num = 1

num += 1
num *= 2

print(num)

# absolute value
print(-10)

# round value
print(round(3.49, 1)) 
# -> second parameter is to round value upto decimal places

"""
Comparision Operators > Returns boolean

Equal: 3 == 2
Not Equal: 3 != 2
Greater Than: 3 > 2
Less Than: 3 < 2
Greater Than Equal: 3 >= 2
Less Than Equal: 3 <= 2

"""

# Type Casting

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) # text concatination

print(int(num_1) + int(num_2)) # correct value



# LISTS::

# lists are mutable


courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# len og list -> len(courses)

# get value in between
print(courses[0:2]) # 2 position is exclusive

# add item to the end
courses.append('Geography')

# insert item in between
courses.insert(0, 'Art')

# using extend method
courses_2 = ['Education', 'Library']

courses.extend(courses_2)

# remove method -> takes only one argument
courses.remove('Math')

popped = courses.pop() #removes last value // retunr the last value

print(courses)
# reverse the list
courses.reverse();

# sorting a list -> acending order // inplace
courses.sort()

# -> decending order
courses.sort(reverse=True)

# sort without altering the original list
sorted_course = sorted(courses)

print('sorted course:', sorted_course)

print(courses)

# min, max, sum
nums = [1,2,3,4,5]
print(sum(nums))

# find index of certain value
print(courses.index('Geography'))

# check for value in list > return boolean
print('Art' in courses)

# print each item using for loop

# for item in courses:
#     print(item)


# print index with value

# for index, course in enumerate(courses):
#     print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)


# join the list of values

course_str = ' - '.join(courses)
# print(course_str)

# split a str into a list // not in place
new_list = course_str.split(' - ')
print('new list', new_list)



# TUPLES::

"""
 tuples are immutable / cannot be changed

 only support accesing the data as we cannot change or update and delete the data from it

"""

tup = ("Abhishek","Abhishek", "Kumar", "Sanket", "Anshul", "Kapil")

print(tup)


# SETS::

"""
 sets don't care about order 
 sets get rid of duplicates
 sets are optimized for searching 

"""

cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {'History', 'Math', 'Art', 'Design'}

# print(cs_courses) # removes duplicates / follow no order
# print('Math' in cs_courses)


# intersection method // gives common values 
print(cs_courses.intersection(art_courses))


# difference method // gives not present values
print(cs_courses.difference(art_courses))

# union of two sets
print(cs_courses.union(art_courses))


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_sets =  {} # This isn't right! Its a dictionary
empty_sets = set()
























