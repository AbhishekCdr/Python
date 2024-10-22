'''
LEGB abbreviation
Local, Enclosing, Global, Built-in
'''

x = 'global x'

def test():
    y = 'local y' 
    print(y)

# test()


# using global statement

def test1():
    global z # set z globally
    z = 'local z'
    print(z)

# test1()
# print(z) # only found when func test1 is called


# builtins
import builtins

# print(dir(builtins))

# def min(): #this will give error
#     pass

m = min([5,3,9,1])
print(m)


# Enclosing

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
