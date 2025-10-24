#generators give you iterators
#generators are written like regular functions but use the yield statement whenever they want to return data
#each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed)
#once the function terminates, StopIteration is raised automatically on further calls to next()
#generators are more memory efficient than normal functions that return a list because they yield items one at a time in a lazy manner, so they do not need to store the entire list in memory
#example of a generator that yields squares of numbers from 1 to 10

def topten():
    n=1
    
    while n<=10:
        sq=n*n
        yield sq#yield is like return, except that it returns a generator object to the caller and saves the state of the function
        n+=1
    
   
    
values=topten()#create generator object, this statement does not run the function, it only returns a generator object

for i in values:#this will call next() on the generator object repeatedly until the generator is exhausted, and gives StopIteration error
    print(i)