'''
Created on 2017年10月3日

@author: Colin
'''

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + ' x ' + str(i) + ' = ' + str(i*j) + '\t', end=' ')
    print()