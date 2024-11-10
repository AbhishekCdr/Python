# def keyword stands for definition 

# allow to repleat etask without repeating the code

def hello_function():
    print('Hello Function !')
    return 'Hello function Returned'

# hello_function()
# print(hello_function())


# Passing an argument

def hello_func(greeting, name = 'You'):   # greeting is scoped to function only
    return '{} Function, {}'.format(greeting, name)

print(hello_func('Hello'))

# *args/**kwargs is used for accepting an arbitary no. of positional or keyword values
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# student_info('Math', 'Art', name='Abhishek', age=22)

# ('Math', 'Art') -> tuples
# {'name': 'Abhishek', 'age': 22} -> dictionary

course = ['Math', 'Art']
info = {'name': 'Abhishek', 'age': 22}

student_info(*course, **info)




