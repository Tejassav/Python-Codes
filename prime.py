#prime is a number which is only divisble by 1 and the number itself 
num=int(input("enter any number:"))
for i in range (2,num):
    if num%i==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")