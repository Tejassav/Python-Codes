#python does'nt support abstract classes directly but we do it through a module "abc" which stands for abstract base classes
#methods which are only declared and are not defined(it's working or body) are  abstract methods
#and classes havng abstract methods are abstract classes
#you can't create objects of abstract classes
#unless in a sub class(of an abstract class) you define the 
# abstract class methods your sub class also remains an abstract class i.e you can't create objects of it
from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod   #decorator
    def process(self):
        pass
    
class laptop(computer):
    def process(self):
        print("Running")
    
com1=laptop()
com1.process()