try:
    pass
except Exception:
    pass
else: # -> if try doesnot throw an exception then it will execute
    pass
finally: # -> not matter try and except this will run // prperly close the operation such as DB
    pass

# example
'''
try:
    f = open('test_file.txt')
except FileNotFoundError:
    print('Sorry This file does not exist')

'''



try:
    f = open('testfike.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else: # -> if try doesnot throws exceptiont hen else part will run
    print(f.read())




