a=5
b=4

print("Before swapping: a =",a," b =",b)
#swapping with temp variable
temp=a
a=b
b=temp

print("After swapping: a =",a," b =",b)
#swapping without temp variable
a,b=b,a
print("After swapping without temp variable: a =",a," b =",b)



