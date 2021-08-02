'''inheritance
Compostion
Types of inheritance
Multiple inheritance
MRO(method REsolution Order)
-----------------------------------
Polymorphism:
Overloading
    operator Overloading
overriding
duck typing
-------------------------------
encapsulation 
interface
abstract class
public, private, protected methods
---------------------------------
Overloading:
    When ever methods parent has by default available to the child through inheritance.Some times child may not satisfy with parent methof implementatin. This process is called overriding 
    *The parent class method which is overriden is called overriden method
    *The child class me thod ehich is overriding is called overriding method

'''

'''How to access Members of one class inside another class:
By Composion(HAS-A RELATIONSHIP)
By Inheritance(IS-A RELATIONSHIP)

By Composition(HAS-A relationship):
---------------------------------------------
By using class name or by creating object we can access members of one class inside another class..... composition

class Engine:
    engine specific functionality

class Car:
    e = Engine()
    e.m1()
    e.m2()

   
    class Car has-a engine reference code reusability
'''
# class Engine:
#     a = 10
#     def __init__(self):
#         self.b = 20

#     def m1(self):
#         print('Engine specific functionality')
# class Car:
#     def __init__(self):
#         self.e = Engine()
#     def m2(self):
#         print('Class Car using Engine class functionality')
#         print(Engine.a)
#         print(self.e.b)
#         self.e.m1()
# c = Car()
# c.m2()
# print("------------------------------------")
class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color =color
    def getInfo(self):
        print('car name:',self.name)
        print('car model',self.model)
        print('car color',self.color)

class Employee:
    def __init__(self,eno,ename,car):
        self.eno = eno
        self.ename = ename
        self.car = car
    def empInfo(self):
        print('Employee Number:', self.eno)
        print('Employee name:',self.ename)
        print('car Information...')
        self.car.getInfo()

car = Car('Innova','2.5v','Gray')
emp = Employee(100,'Durga',car)
emp.empInfo()
print('-----------------------------')

# IS-A RELATIONSHIP 

class P:
    a = 10
    def __init__(self):
        self.b = 10
    def m1(self):
        print("parent class instance method ")
    @classmethod
    def m2(cls):
        print('parent class method')
    @staticmethod
    def m3():
        print('parent class method')

class C(P):
    
        pass
    

c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
print("-------------------------------")

class P:
    a = 20
    def __init__(self): 
        self.b = 10
class C(P):
    
    def __init__(self): #only this construor is initialize
        # super().__init__()
        self.d = 40
c = C()
print(c.a,c.d)


print('-------------------------------------')

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat_n_drink(self):
        print("Eat Biryani and drink beer")
    
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
    def work(self):
        print('Coding Python')
    def empInfo(self):
        print("Employee name:",self.name)
        print("Employee Age:",self.age)
        print('Employee number',self.eno)
        print('Employee Salary:',self.esal)

e  = Employee('Durga', 32,928393,2010)
e.eat_n_drink()
e.work()
e.empInfo()

print('-----------------------------')


''' *When we should go for IS-A Relation and HAS-A Relation
IS-A  VS  HAS-A:
-------------------------------------------------------
  
*when We should Go for inheritance:
when I want to extend the existing functionality with some of more extra functionality then we should go for inheritance

*When we should go for HAS-A relationship:
when I want/to use some class functionality but I don't want to extend then we should go for HAS-A relationship

'''


class Car:
    def __init__(self,name,model,color):
        self.name= name
        self.model = model
        self.color = color
    def getInfo(self):
        print('\t Car Name:{}\t Car Model:{}\t Car color:{}'.format(self.name,self.model,self.color ))
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat_n_drink(self):
        print("Eat Biryani and drink beer")
    
class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
        self.car = car
    def work(self):
        print('Coding Python')
    def empInfo(self):
        print("Employee name:",self.name)
        print("Employee Age:",self.age)
        print('Employee number',self.eno)
        print('Employee Salary:',self.esal)
        print('Car Info')
        self.car.getInfo()

c = Car('Innova','3.5v','Gray')
e  = Employee('Durga', 32,928393,2010,car)
e.eat_n_drink()
e.work()
e.empInfo()

'''HAS-A relation Types:
-----------------------------
Composition vs Agregation
------------------------------


Without existing container object if there is no chance of contained objects then container object and contained object are strongly associated. This strong association is called composition ie without existing university object there is no existnace of department objects

Without existing container object if there may be chance of existing contained object  then container object and contained objects are weakly association.This weak association is called Aggregation.

'''
class Student:
    college_name = "DURGASOFT"
    def __init__(self,name):
        self.__init__(self,name):
        