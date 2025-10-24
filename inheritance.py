class A:
    def feature1(self):
        print("feature1 is working")
        
    def feature2(self):
        print("feature2 is working")
        
class B(A):
    def feature3(self):
        print("feature3 is working")
        
    def feature4(self):
        print("feature4 is working")
           
a1=A()
b1=B()


b1.feature1()
b1.feature2()

b1.feature3()
b1.feature4()