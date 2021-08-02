'''1.Abstract class are classes that contain one or more abstract methods.
2.An abstract method is a method that is daclared, but  contains no implementation
3.Abstact classes cannot be instantiated,and require subclasses to provide implementations for the abstract methods.
4.Subclasses of an abstract class in python are not required to implement abstract methods of the parent class.

ABC is a name of class which is predefined class in python

We can not create an object of an abstract class
'''

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def display(self):
        None
    
class B(A):
    def display(self):
        print('This is display method')
    
obj = B()
obj.display()

print('----------------------------------------------')

class Cal(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class C(Cal):
    def add(self):
        print(self.value+100)
    def sub(self):
        print(self.value-10)

cobj = C(100)
cobj.add()
cobj.sub()