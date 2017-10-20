'''
Created on 2017年9月26日

@author: Colin
'''

while True:
    txt = input('pls guess a number:')
    if txt == 'stop':
        break
    elif not txt.isnumeric():
        print('Your input is not a number')
        break
    else:
        num = int(txt)
        
        if num < 20:
            print('The number is too small')
        elif num > 20:
            print('The number is too large')
        else:
            print('congratulations!')
            break
        