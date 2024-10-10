"""
Comparision:

Equal: ==
Not Equal: !=
Greater Than: >
Less Than: <
Greater Equal: >=
Less Equal: <=
Object Idetity: is

"""

# if 

# if True:
#     print('Conditional was True')


 # if else

language = 'Java'

# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# else: 
#     print('No Match')



# Boolena operators
"""
and 
or
not

"""

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')



# not is used to check boolean
if not logged_in:
    print('Please Log In')



# Object identity
# differnt in memory allocations

a = [1,2,3]
b = [1,2,3]

print(a is b) # false check for ids
print(a == b) # true check for values

# -> get id of list
# print(id(a))
# print(id(b))


# False Values Evaluated by Python:
"""
 Flase
 None
 Zero of any numeric type
 Any empty sequence Eg: '', (), []
 Any empty mapping Eg: {}

"""

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
