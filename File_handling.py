#purpose of file handling =>to store data for a longer period
f=open("mydata","r")#r stands for read mode
#f=open("mydata","w")#w stands for write mode, will overwrite the existing data
#f=open("mydata","a")#a stands for append mode, will add data to the existing data
#f=open("mydata","r+")#r+ stands for read and write mode, will allow both reading and writing
#f=open("mydata","a+")#a+ stands for append and read mode, will allow both appending and reading

print(f.read())
#readline()=>will print only one line of the file, each time it is called, it will print the next line, 
#readline(4)=>will print only the first four characters of the line to be printed

f1=open("abc","w")
f1.write("something")

for data in f:
    f1.write(data)
