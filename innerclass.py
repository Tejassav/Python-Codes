class Student:
    def __init__(self,name,roll):#instance method
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
        
    def show(self):#instance methods
        print(self.name,self.roll)
        self.lap.show()
        
    class Laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
            
        def show(self):
            print(self.brand,self.cpu,self.ram)
        
s1=Student("navin",12)
s2=Student("jenny",13)

s1.show()
s2.show()

