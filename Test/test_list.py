'''
Created on 2017年9月26日

@author: Colin
'''
from audioop import reverse

fruits = ['apple', 'banana', 'orange', 'pineapple','watermelon']
#         0      1         2         3            4            5
#         -5     -4        -3        -2           -1           0
          
print(fruits)
print('列表长度为：%d' %(len(fruits)))
print(fruits[-3:-1])
print(fruits[1::2])
print(fruits.index('watermelon'))
# 遍历所有列表元素， 方法1
print('遍历方法1，所有元素为：')
for l in fruits:
    print(l)
     
# 遍历所有列表元素，方法2   
print('遍历方法2，所有元素为：') 
for i in range(len(fruits)):
    print(fruits[i])
    
scores = [1,2 ,33 ,4 , 5, 5, 6 ]
print(sum(scores))
print(scores.count(51))
scores.append(88)
print(scores)

s = list(range(1,11))
print(s)

s[:5] = [88]
print(s)

s[:3] = [55,66,77]
print(s)

s[::2] = [1,1,1]
print(s)

# 序列删除操作
# s.remove(1)
# s.pop() #默认pop最后一个元素
s.pop(1)
print(s)

#序列插入操作
s.append([9,10])
s.extend([9,10])
print(s)

s.insert(0, 100)
print(s)

s1 = s.copy()
s1 = s[:]
print(s1)

s2 = s.copy()
s2.pop(-3)
s2.sort(reverse=True)
print(s2)
print(sorted(s2))

print(sorted(fruits, key=lambda n:n[1]))

