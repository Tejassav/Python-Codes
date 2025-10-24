#module is simply a file or a small logical component of a big code/project

from module1 import *

a=9
b=10

sub(a,b)

#__name__ variable is a built-in variable which evaluates to the name of the current module
#if the module is being run directly then the __name__ variable will have a value "__main__"
#else if the module is being imported then the __name__ variable will have a value equal to the module's name