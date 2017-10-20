'''
Created on 2017年9月26日

@author: Colin
'''

while True:
    txt = input('pls input a number:')
    if txt == 'stop':
        break
    elif not txt.isnumeric():
        print('your input is not a number')
        break
    else:
        num = int(txt)
        
        if num < 20:
            print('你输入的数值过小')
        elif num > 20:
            print('你输入的数值过大')
        else:
            print('congratulations!')
            break
        