n=int(input("enter number to be checked:"))
order=len(str(n))
copy_n=n

sum=0

while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
    
if(sum==copy_n):
    print(copy_n,'is Armstrong an numer..')
else:
    print(copy_n,'is not an Armstrong number...')