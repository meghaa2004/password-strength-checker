import math
print("------------------------------------------------PASSWORD STRENGTH CHECKER---------------------------")
def count_character_types(input_string):
    
    count_digits = 0
    count_uppercase = 0
    count_lowercase = 0
    count_special = 0
      

    for char in input_string:
        if char.isdigit():
            count_digits += 1
        elif char.isupper():
            count_uppercase += 1
        elif char.islower():
            count_lowercase += 1
        else:
            count_special += 1
    
#_------------------------passwords with single datatype
    if( count_digits!=0 and count_uppercase==0 and count_lowercase==0 and count_special==0):
        print ("Password only contains numbers. IT IS WEAK")
        n= 10
    elif( count_digits==0 and count_uppercase!=0 and count_lowercase==0 and count_special==0):
        print ("Password only contains Uppercase alphabets. IT IS WEAK ")
        n=26
    elif( count_digits==0 and count_uppercase==0 and count_lowercase!=0 and count_special==0):
        print ("Password only contains Lowercase alphabets. IT IS WEAK ")
        n=26
    elif( count_digits==0 and count_uppercase==0 and count_lowercase==0 and count_special!=0):
        print ("Password only contains Uppercase alphabets. IT IS WEAK ")
        n=32
#------------------------passwords containing two datatypes
    elif( count_digits!=0 and count_uppercase!=0 and count_lowercase==0 and count_special==0):
        print ("Password contains Numbers and Uppercase alphabets. It's strenght is medium.")
        n=36
    
    elif( count_digits!=0 and count_uppercase==0 and count_lowercase!=0 and count_special==0):
        print ("Password contains Numbers and Lowercase alphabets. It's strenght is medium. ")
        n=36

    elif( count_digits!=0 and count_uppercase==0 and count_lowercase==0 and count_special!=0):
        print ("Password contains Numbers and special characters. It's strenght is medium. ")
        n=42

    elif( count_digits==0 and count_uppercase!=0 and count_lowercase!=0 and count_special==0):
        print ("Password contains  Lower and Uppercase alphabets. It's strenght is medium. ")
        n=52

    elif( count_digits==0 and count_uppercase!=0 and count_lowercase==0 and count_special!=0):
        print ("Password contains Uppercase alphabets and special charcters . It's strenght is medium.")
        n=58

    elif( count_digits==0 and count_uppercase==0 and count_lowercase!=0 and count_special!=0):
        print ("Password contains Lowercase alphabets and special characters . It's strenght is medium.")
        n=58
#-------------------------passwords containing three data types

    elif( count_digits!=0 and count_uppercase!=0 and count_lowercase!=0 and count_special==0):
        print ("Password does not contain special character. It is STRONG.")
        n=62
    elif( count_digits!=0 and count_uppercase!=0 and count_lowercase==0 and count_special!=0):
        print ("Password does not contain lowercase alphabet. It is STRONG.")
        n=68
    elif( count_digits==0 and count_uppercase!=0 and count_lowercase!=0 and count_special!=0):
        print ("Password does not contain numbers. It is STRONG.")
        n=84


    else:
        print ("Password contains all data types. It is VERY STRONG")
        n=94


#----------------------function to find all possible combinations------------------------

    def combi(password):
        r=len(password)
        numerator = math.factorial(n + r - 1)
        denominator = math.factorial(r) * math.factorial(n - 1)
        no_of_combi= numerator // denominator
        return no_of_combi
        
#---------------------function to find time -----------------------
#    def crack(combi):  
#       time = no_of_combi/10000
#       return time


    return {
        "digits": count_digits,
        "uppercase": count_uppercase,
        "lowercase": count_lowercase,
        "special": count_special,
        "possible combinations": combi(password),
#        "time taken in minutes": crack(combi)
    }


#-------------------------------INPUT PASSWORD----------------------
password = input(print("enter password:"))
result = count_character_types(password)
print(result) 










    
    
