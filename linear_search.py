#objective =>to search an element from a list
#to check if 9 is in the list or not.
def search (list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i+=1
    return False
    
    
l=[5,8,4,6,9,2]
n=4

if search(l,n):
    print("found")
else:
    print("not found")
    
#time complexity => O(n) in worst case
#space complexity => O(1)

#other way to do linear search is by using 'in' keyword in python
if n in l:
    print("found")
#time complexity => O(n) in worst case
#space complexity => O(1)
    
 
 

