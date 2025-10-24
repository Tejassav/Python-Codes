#variable created outside the function is called the global variable;
#variable created inside the function is called the local variable;
a=10
print(id(a))

def something():
    a=9
    
    x=globals()["a"] # the globals() function returns a dictionary representing the current global symbol table. or in simple words it allows you to access global variables inside a function.using their names as keys.
    print(id(x))
    print("in func",a)
    
    globals()['a']=15
    
    
something()
print(a)

#global keyword is used to declare that a variable inside a function is global variable or to make a global variable inside a local scope or function.
#or to change the value of a global variable inside a function.
