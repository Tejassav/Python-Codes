#anonymous functions used when we want to create a function of one line or one expression and we'll be using that function only once
#can be used wherever function objects are required, i.e they can be passed as arguments to higher order functions
#syntax: lambda arguments: expression, the expression is executed and the result is returned
#example: 
#defining a normal function
def add(a,b):
    return a+b
#defining a lambda function
f = lambda a,b : a+b  #anonymous function i.e they have no name , here f is just a reference to that function

result1=f(5,6)
print('result from lambda: ',result1)
result2=add(5,6)
print('result from normal function: ',result2)