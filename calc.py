a=int(input("enter a number:"))
b=int(input("enter other number:"))
choice=input("enter operation:")
def calc(a,b):
    if choice=='add':
        print(a,"+",b," = ",a+b)
    elif choice=='sub':
        print(a,"-",b," = ",a-b) 
    elif choice=='mul':
        print(a,"*",b," = ",a*b) 
    elif choice=='div':
        if b!=0:
             print(a,"/",b," = ",a/b)
        else:
            print("can't divide by zero")
    else:
        print("not a valid operation")  
        
calc(a,b)
