li = [9,1,8,2,7,5,4,8,9]

s_li = sorted(li) # not inplace

s_li = sorted(li, reverse=True) # reverse in desc

# print(s_li) # sorted


# li.sort() # inplace
# print('Sorted Variabel:\t', li)
'''
.sort() can be only used in list
'''

# Tuple
tup = (9,1,8,2,7,5,4,8)

tup_sorted = sorted(tup, reverse=True)

# print(tup_sorted) 

# Dictionary

di = {'anem': 'Corey', 'job': 'Programming', 'age': None, 'os': 'Mac'}

s_di = sorted(di) #sort all the keys

# print('Sorted dictionay', s_di)

# Key Parameter

li = [-6,-5,-3,0,2,4,5]

s_li = sorted(li, key=abs) # absolute values
# print(s_li)







