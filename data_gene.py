from random import *
import math
import string

def integer_generator(min_num, max_num, size, is_unique, is_nullable):
    #Checking if given size fits in length range
    if (is_unique and is_nullable and size>(-1*min_num)+max_num+2) or (is_unique and not(is_nullable) and size>(-1*min_num)+max_num+1):
        print("error - size exceeds for unique values")
        return []
    ele_array= []
    if not(is_unique):     
        if is_nullable:
            null_ele = int(size * 0.1)
            size = size - null_ele
            for i in range(null_ele):
                ele_array.append(None)
        dup_ele = int(size * 0.2)
        size = size - dup_ele
        if size%2==0:
            ele_array.extend(list(range(int(-size/2),0))+list(range(0,int(size/2))))
        else:
            ele_array.extend(list(range(int(-size/2),0))+list(range(0,int(size/2)+1)))
        for i in range(dup_ele):
            ele_array.append(choice(ele_array))
        shuffle(ele_array)
    else:
        if is_nullable:
            ele_array.append(None)
            size = size - 1
        if size%2==0:
            ele_array.extend(list(range(int(-size/2),0))+list(range(0,int(size/2))))
        else:
            ele_array.extend(list(range(int(-size/2),0))+list(range(0,int(size/2)+1)))
        shuffle(ele_array)
    return ele_array

#BigInt value range (8 Bytes) is -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
def dt_bigint_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = -9223372036854775808
    max_num = 9223372036854775807
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)    

#Integer value range (4 Bytes) is -2,147,483,648 to 2,147,483,647
def dt_int_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = -2147483648
    max_num = 2147483647
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)

#SmallInt value range (2 Bytes) is -32,768 to 32,767
def dt_smallint_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = -32768
    max_num = 32767
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)    

#TinyInt value range (1 Bytes) is 0 to 255
def dt_tinyint_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = 0
    max_num = 255
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)    

#######

def string_generator(size, length=None, is_unique=False, is_nullable=True):
    ele_array= []
    len_not_provided = False
    
    if (length!=None and is_unique and 52**length < size) or size==None:
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
        if not(is_unique==True and val in ele_array):
            ele_array.append(val)
            i = i+1
    return ele_array
#Nullable or NotNullable
#Negative numbers
#Char VarChar Text
#Binary Boolean
#Float Double Decimal
#Date Time TimeStamp DateTime
#Serial