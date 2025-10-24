#using decorators you can add the extra features to an existing function
def div(a,b):#existing function
    print(a/b)
    
def smart_div(func):#decorator function, takes function as argument, adds extra functionality and returns a modified function
    
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)#calling the existing function with modified arguments
    return inner#returning the modified function, not calling it

div1=smart_div(div)

div1(2,4)

