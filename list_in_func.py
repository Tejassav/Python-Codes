#you have to take a list as input and then return number of even and odd numbers in that list;

#doing this using normal function or the normal way
'''even=[]
odd=[]
'''

'''def count(list):
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"number of even elements: {len(even)} \nnumber of odd elements: {len(odd)}")
    print('list of even elements: ',even)
    print('list of odd elements: ',odd)'''
    
'''count(list)'''

#same thing can be done in one line using list comprehension

list=[3,44,5,7,8,9,88]

evens = [item for item in list if item%2==0]
odds = [item for item in list if item%2!=0]
print(f"number of even elements: {len(evens)} \nnumber of odd elements: {len(odds)}")
print('list of even elements: ',evens)
print('list of odd elements: ',odds)
        