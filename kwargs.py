#keyword arguments are used to pass the variable length of arguments to a function,
#in this we use ** before the parameter name to pass the variable length of arguments
#the keyword arguments are stored in the form of dictionary and it should be the last parameter of the function
#anything after the keyword arguments will give an error
#if we have variavle length positional arguments and variable length keyword arguments in a function then
#the variable length positional arguments should be placed before the variable length keyword arguments

def person(name,**data):
    print('name', name)
    for i,j in data.items():
        print(i,j)
    
person("tejassav",age=18,gender="male",ph_number=8081389797)
