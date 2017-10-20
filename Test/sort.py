#coding = 'utf-8'
'''
Created on 2017/9/22
@author: Colin
'''

def sort_list(the_list, sort_reversed=False):
    for i in range(0, len(the_list)):
        for j in range(i+1, len(the_list)):
            if sort_reversed:
                if the_list[i] < the_list[j]:
                    the_list[i], the_list[j] = the_list[j], the_list[i]
            elif the_list[i] > the_list[j]:
                the_list[i], the_list[j] = the_list[j], the_list[i]
    print(the_list)

if __name__ == '__main__':
    sort_list([10, 2, 3, 6, 18, 64, 7, 9], sort_reversed=False)
    
        
