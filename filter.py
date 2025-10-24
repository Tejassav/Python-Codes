#filter is a function in python and it filters out elements from a given collection based on some condition
#filter(function,collection), returns an iterator that is already filtered based on the function provided


#for example we want to filter even numbers from a given collection
from functools import reduce
nums=[1,2,4,7,4335,66,43,56,8]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
sum=reduce(lambda a,b:a+b,doubles)
print(evens)
print(doubles)
print(sum)