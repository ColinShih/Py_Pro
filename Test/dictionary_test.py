'''
Created on 2017年9月26日

@author: Colin
'''

# 字典声明
students = {'name':'tom','sex':'male','job':'engineer','school':'middle'}
print(students)

book = dict(title='python book',author='tom',price=60.00)
print(book)
lst = [('title','python book'),('author','tom'),('price',60.00)]
book2 = dict(lst)
print(book2)
print(book==book2)

# 字典访问
keys = ['title','author','price']
book3 = dict.fromkeys(keys)
print(book3)

print(book.get('titled','key not found'))

for k in book.keys():
    print(k)
    
for v in book.values():
    print(v)
    
print(list(book.items()))

for (k,v) in book.items():
    print('{} -> {}'.format(k, v))
   
print(len(book))
    
# 字典操作
bk = book.copy()
print(bk)
# add new key
bk.update({'org':'shanghai'})
print(bk)

bk.pop('price','key not found')
print(bk)

print(bk.popitem()) #默认弹出最后一项
print(bk)


# 字典中可以有函数
def say_hello():
    print('hello python')
person = {'name':'tom','action':say_hello}   
# 执行字典中的函数 
person.get('action')()
