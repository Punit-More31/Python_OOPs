# from one class we can access  members of other class once your have that object reference

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename =ename
        self.esal = esal
    
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)


class Test:
    def modify(emp):
        emp.esal = emp.esal+10000
        emp.display()

e = Employee(2323, 'Arun', 20000)
Test.modify(e)  
print('---------------------------------------------')
'''* INNER CLASSES * 
1. The class which is declared inside another class
2. Without existing one type of objects if there is no chance of existing another type of object then we should go for inner classes.

eg.
class Car:
    ---
    class Engine:
        ----

eg.
class University:
    class Department:
    
Without existing outer class objects there is no chance of existing inner class objects. Inner class objects is always associated wuth outer class object.



'''


class Outer:
    def __init__(self):
        print('Outer class objects creation...')
    def m2(self):
        print('Outer class method')
    class Inner:
        def __init__(self):
            print('Inner class objects creation..')

        def m1(self):
            print("Inner class method")

o = Outer()
i = o.Inner()
i.m1()
o.m2()
''' i = Outer().Inner()
    i.m1()
        or
    Outer().Inner().m1()
'''

print('----------------------------------------')

class Person:
    def __init__(self):
        self.name = 'Punit'
        self.dob = self.DOB()
    def display(self):
        print('Name:',self.name)
        self.dob.display()
     
    class DOB:
        def __init__(self):
            self.dd = 15
            self.mm = 5
            self.yyyy = 1999
        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd,self.mm,self.yyyy))


p = Person()
p.display()
