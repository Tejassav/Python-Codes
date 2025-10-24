def greet():#defining the function
    print("hello world")
    print("good morning")
    
    
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
    
greet()#calling the method
result=add_sub(4,5)
print(result)