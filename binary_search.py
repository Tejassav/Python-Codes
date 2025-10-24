#in binary search all the  values should be sorted
#set lower bound(l) and upper bound(u)
#find mid index([l+u]/)
#check if the element at the mid index matches with element required
#if not =>Case 1:if the required element is less than mid element change upper bound(mid values becomes the new upper bound)
#Case 2:if the required element is greater than mid element change lower bound(mid value becomes new lower bound)
#in case mid index comes out to be 3.5 then it is takes as 3
pos =-1

def search(list,n):
    l=0
    u=len(list)-1
    
    while l<=u:
        mid =(l+u)//2
        
        if list[mid]==n:
            globals()["pos"]=mid
            return True 
        else:
            if list[mid]<n:
                l=mid;
            else:
                u=mid;
                
l=[4,5,7,8,44,77]
n=7

if search(l,n):
    print("found at",pos+1)
else:
    print("not found")
                