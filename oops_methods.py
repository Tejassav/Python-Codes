class Student:
    school="Telusko"
    
    def __init__(self,m1,m2,m3): #constructor, it is a special method which is called when an object of the class is created, it is used to initialize the instance variables of the class, it takes self as first argument which is a reference to the current object
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @staticmethod #static method decorator
    #static method does not take self or cls as first argument, it behaves like a normal function but lives in the class namespace, it cannot access instance variables or class variables, its main pupose it to group functions which have some logical connection with the class but do not need to access class or instance data
    def get_class():
        print("This is class IOT & BC...in BBDU")
        
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod #class method decorator
    #class method takes cls as first argument, it can access class variables but not instance variables, it can be called using class name or instance name, its main purpose is to access or modify class state, in simple words it can access class variables and modify them
    def info(cls):
        cls.school
        
Student.get_class()

s1=Student(37,44,45)
s2=Student(33,48,49)

print(s1.avg())
print(Student.info())

#the need for having static method and class method is to provide a way to group functions which have some logical connection with the class but do not need to access class or instance data, this helps in organizing the code better and makes it more readable and maintainable.
#for example, if we have a class which represents a bank account, we can have a static method which calculates the interest rate for the account based on the type of account, this method does not need to access any instance or class data but it is logically connected to the class, similarly we can have a class method which returns the total number of accounts created, this method needs to access class data but not instance data.
        