class Student:
    
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def __add__(self,other):
        m1=self.m1
        m2=self.m2
        s3=Student(m1,m2)
        
        return s3
        
        
        
        
        
s1=Student(65,46)
s2=Student(24,56)
s3=s1+s2
print(s3.m1)