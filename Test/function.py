'''
Created on 2017年10月10日

@author: Colin
'''

from functools import reduce
def f(x):
    return x*x

r = map(f,[1,2,3,4,5])
print(list(r))

def f1(x, y):
    return x+y
r1=reduce(f1,range(1,101))
print(r1)