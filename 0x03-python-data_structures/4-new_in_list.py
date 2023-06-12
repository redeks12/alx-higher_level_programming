#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        arr = []
        
        if (idx < 0) or (idx >= len(my_list)):
                return my_list
        for i in my_list:
                arr.append(i)
        arr[idx] = element
        return arr

