#heap memroy has objects
#these objects take memory and thus have some memory address associated to them
#we can check this address(of object)with the help of id function
#size of object depends on the number of variables of object
#memory allocation is done by constructor

class Computer:
    def __init__(self):
        self.name="Ravi"
        self.age=19
        
    def update(self):
        self.age=20
    
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
        
c1=Computer()
c2=Computer()

c2.name="teju"


if c1.compare(c2):
    print("They are same")
    
else:
    print("they  are different")
    
print(c1.name)
print(c2.name)