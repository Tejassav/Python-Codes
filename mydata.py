#opening the file
#f=open('mydata','r')
#reading the file
'''data = f.read()
print(f'\n{data}\n')''' #these lines are commented to avoid reading the file twice, because if a string is not assigned to a variable then it is ignored by python interpreter and hence the file pointer moves to the end of the file after first read() call
#closing the file   
#f.close()

'''with open('mydata', 'r') as f:
    data = f.read()
    print(f'\n{data}\n')'''
#no need to explicitly close the file when using 'with' statement, it automatically closes the file after the nested block of code is executed

#to append data to the file
'''with open('mydata', 'a') as f:
    f.write('\nthis is appended line')'''
    

'''with open('mydata', 'r') as f:
    data = f.read()
    print(f'\n{data}\n')'''
    
#to write data to the file
'''with open('mydata', 'w+') as f:
    f.write("this text overwrites previous text")
    f.seek(0)  #to move the file pointer to the beginning of the file
    data = f.read()
    print(f'\n{data}\n')'''
    
f = open('mydata', 'r')
data = f.readlines()
f.seek(0)
position = f.tell()
print(f'current position of pointer: {position}')