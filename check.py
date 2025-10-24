l=['a','b','c']

#syntax of list comprehension
#newlist=[expression for item in iterable if condition==True]


x=[i for i in l if i!='a']

#this is equivalent to
#newlist=[]
#for item in iterable:
#    if condition==True:
#        newlist.append(expression)
print(x)