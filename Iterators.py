#l=[1,2,3,44,5,]
#it=iter(l)

#print(it.__next__())
#print(next(it))

#for i in l:
 #   print(i)
 
#an iterator is an object that contains a countable number of values
#iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#iterable is an object which will return an iterator when called using iter() method.
#Examples of iterable objects are lists, tuples, strings etc.
#the difference between iterator and iterable is that an iterable is an object that can be iterated upon, while an iterator is the object that does the actual iterating.
#the iterable gives an iterator using iter() method. This iterator object can then be used to iterate through the iterable.
#because iterator object implements the __next__() method, which returns the next value from the object.
#and when there are no more values to return, it raises a StopIteration exception.
#an iterator is able to traverse through all the values of an iterable one at a time because it has all the elements of the iterable stored in it.

 
class TopTen: #iterator class
    def __init__(self):
        self.num=1
        
    def __iter__(self):#iter will give you the object of iterator
        return self
    
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values=TopTen()
print(next(values))

for i in values:
    print(i)
