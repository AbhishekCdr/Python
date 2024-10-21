# File Objects

f = open('sample.txt', 'r')


print(f.name) # print name of file
print(f.mode) # print the mode of the file

f.close() # important to close the file explicitly


# using context manager
# access of file inside a particular block of code and close the file as we move outside it

with open('sample.txt', 'r') as f:
    f_contents = f.read()
    # print(f_contents)
    f_readline = f.readline()
    # print(f_readline) # reads the first line
    f_readlines = f.readlines()
    print(f_readlines)



