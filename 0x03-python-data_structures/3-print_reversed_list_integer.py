#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
        b = len(my_list) - 1
        for i in my_list:
                print(my_list[b])
                b -= 1
                
                
                

my_list = [1,9 ,3,5,6,9,0,3,0,0,0,0,2, 3, 4, 5]
print_reversed_list_integer(my_list)