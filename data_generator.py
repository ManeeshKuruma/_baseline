from random import *
import string


### If length of string is not provided then by default we will generate a string from range of 5-10 length of string
### If size i.e., number of records is not mentioned we will throw an error
### If requested for a unique column value with size > max_generations, then we will throw an error

def string_generator(length=None, size=None, unique=False):
    ele_array= []
    len_not_provided = False
    
    if (length!=None and unique and 52**length < size) or size==None:
        print("error")
        return []
    
    if length==None:
        len_not_provided=True
    
    chars = string.ascii_uppercase + string.ascii_lowercase
    i=0
    while i<size:
        if len_not_provided:
            length = randint(5,10)
        val = ''.join(choice(chars) for _ in range(length))
        if not(unique==True and val in ele_array):
            ele_array.append(val)
            i = i+1
    return ele_array
 
def number_generator(length=0):
    return 0

print(string_generator(1, 15, True))