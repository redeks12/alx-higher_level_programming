#!/usr/bin/python3
def no_c(my_string):
        strn = ""
        for i in my_string:
                if (i == "c") or (i == "C"):
                        pass
                else: 
                        strn += i
        return strn                
        