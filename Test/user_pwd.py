#coding = 'utf-8'
'''
Created on 2017/9/22
@author: Colin
'''

db = {'root':'123','colin':'123456'}

def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if db.__contains__(name):
            prompt = 'name taken, try another\n'
            continue
        else:
            break

    pwd = input('password: ')
    db[name] = pwd
    
def olduser():
    name = input('login: ')
    pwd = input('passwd: ')

    passwd = db.get(name)
    if passwd == pwd:
        print('welcome back {}'.format(name))
    else:
        print('login incorrect')

def showmenu():
    prompt = """

(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice:"""
    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except:
                choice = 'q'
            print('\nYou picked: [%s]\nSo that system quit' % choice)
            if choice not in 'neq':
                print('invalid option, try again')
            else:
                chosen = True

        if choice == 'q':done = True
        if choice == 'n':newuser()
        if choice == 'e':olduser()

if __name__ == '__main__':
    showmenu()
        
