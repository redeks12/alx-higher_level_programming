#!/usr/bin/python3
def max_integer(my_list=[]):
        if my_list:
                b = my_list[0]
                for i in my_list:
                        if i >= b:
                                b = i
                return b
        else:
                return None
