# import my_module as mm
# from my_module import find_index
from my_module import *

import os

print(os.__file__)

courses = ['History', 'Math', 'Physics', 'CompSci']

"""
index = my_module.find_index(courses, 'Physics')

print(index)

"""

# specify a name to the imported module and use that anywhere

# index = mm.find_index(courses, 'CompSci')

# print(index)


# import the whole function from my_module

# index = find_index(courses, 'Math')
# print(index)
