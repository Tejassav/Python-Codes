def sum(a,*b):#*b=> to take multiple inputs, these values are internally stored as tuple
    c=a
    print(a, end = ' ')
    for i in b:
        print(i, end= ' ')
    
sum(1,3,4,64,6,2)