#when you create object of sub class it will call init of sub class first
#if you have called super then it will call the init of super class first then the init of sub class 
#MRO =>method resolution order>>it means init goes from left to right(This is for init inheritance)
class A:
    def __init__(self):
        print("in init A")
    
    def feature1(self):
        print("feature1 is working in A")
        
    def feature2(self):
        print("feature2 is working")
        
class B():
    def __init__(self):
        print("in init B")
    
    def feature1(self):
        print("feature1 is working in B")
        
    def feature4(self):
        print("feature4 is working")
        
class C(A,B):
    
    def __init__(self):
        super().__init__()
        print("in C init")
        
    def feature5(self):
        print("feature5 is working")
        
    def feature6(self):
        print("feature6 is working")
 
 
a1=C() 
a1.feature1()  

#see here in the output that it only calls the init of A(and feature 1 of A) and not of B 
#This is because of MRO as C inherits A and B and A comes in the left hence it is executed
           
