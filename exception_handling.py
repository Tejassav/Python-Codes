#syntactical errors =>errors like wrong spelling or forgetting to use colon after if are some of the syntactical errors or they are also called as compile time errors
#next are logical errors =>these errors are compiled and their output is presented wihtout any problem but the output is wrong that is their was a mistake in the logic of the code
#run time errors =>one of the reasons for these errors is due to wrong input given  by the user for eg..if we divide two numbers a/b and the user gives the value of b as 0 then run time error will be raised
#our main purpose of handling errors is that even if there are exceptions or errors our execution should not stop
#Exception is the collective world for all sorts of error or we can  say that all errors come under Exception

a=5
b=0



try:
    print("file opened")
    num=int(input("enter a number:"))
    print(num)
    print(a/b)
    print("file closed")
    
except ZeroDivisionError as e:#doubt =>why in the output it didn't show this error?
    print("you can't divide by zero",e)
    
except ValueError as e:
    print("wrong type of input")
    
except Exception as e:
    print("something went wrong..")
    
finally:
    print("Bye..")
    
    
print("code executed successfully")#this line will now be executred even if there is an error in the try block because we have handled the exception

