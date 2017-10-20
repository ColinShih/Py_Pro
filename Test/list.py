'''
Created on 2017/9/22

@author: Colin
'''

fruits = ['apple', 'banana', 'orange', 'pineapple', 'watermelon']
print(fruits)
print(len(fruits))
print(fruits[1])

print(type(fruits))
print(dir(fruits))

# for item in fruits:
#     print(item)

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
