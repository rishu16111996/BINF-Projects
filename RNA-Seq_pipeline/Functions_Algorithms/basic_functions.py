#!/usr/bin/env python3
# basic_functions

def multiply(a,b):
    '''Multiply Function returns a * b 
    '''
    return a * b

def hello_name(name="you"):
    '''hello_name function returns Hello and name which is passed as argument and should print "you" if no argument is passed
    '''
    return("Hello, {}!".format(name))

def less_than_ten(numb):
    '''This function returns list of numbers less then 10 in a list passed as argument
    '''
    final_list = []
    for i in numb:
        if i < 10:
            final_list.append(i)
            
    return(final_list)

#multiply(5, 10)
#hello_name("Akbar")
#hello_name()
#less_than_ten([1,5,81,10,8,2,102])

