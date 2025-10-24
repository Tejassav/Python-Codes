#there are  two sorts of variables :
#1.instance variable 2.static/ class variable
#instance variables are object specific that is their value can vary from object to object
#class varibales are common to all the objects of the class that is if any change occurs in thhe value of a class variable 
#this value changes for all the  consisting objects
class Car:
    wheel=4
    def __init__(self):
         
         self.milage=10
         self.name="BMW" #both are instance variables
         
         
c1=Car()
c2=Car()

print("before changing the variables:")
print(c1.milage,c1.name,c1.wheel)
print(c2.milage,c2.name,c2.wheel)
#here we change the milage of c1 only so it will not affect the milage of c2
c1.milage=8
print("after changing the instance variable milage of c1:")
print(c1.milage,c1.name,c1.wheel)
print(c2.milage,c2.name,c2.wheel)

#but here we change the class variable wheel using the class name so it will affect all the objects of the class
Car.wheel=5

print("after changing the class variable wheel:")
print(c1.milage,c1.name,c1.wheel)
print(c2.milage,c2.name,c2.wheel)