''''
STATIC VARIABLE
--------------------------
FOR ALL OBJECTS A SINGLE COPY IS MAINTAIN AT CLASS LEVEL 

*What are the various places to declare static variable*
1.Within the class directly but outside of the any method
2.Inside constructor by using class name
3.Inside the instance method using a class name
4.Inside the class method using the cls variable or using class name
5.Inside the static method usign the class name
6.from outside of the class by using the class name

*How to access static variable*
We can access static variable either ny classname or by object reference

within the class:
    classname, cls, self
outside the class:
    object refernce , classname

* How to modify static variables/How to delete static variable *
Within the class we should use classname, cls variable

from outside of the class : only classname




'''
class Student:
    cname = "DURGASOFT"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    
s1 = Student("Pari", 20)
s2 = Student("hari", 30)
print(s1.name, s1.rollno, Student.cname)
print(s2.name, s2.rollno, Student.cname)

print("-----------------------------------------------------------------------------------")

class Test:
    a = 10
    def __init__(Self):
        Test.b = 30
        Test.c = 293
    def m1(self):
        Test.d = 39

    @classmethod
    def m2(cls):
        cls.e = 29
        Test.f = 2
    
    @staticmethod
    def m3():
        Test.g = 29
Test.h = 84
print(Test.__dict__)

print("---------------------------------------------------")

class Test:
    a = 20
    def __init__(self):
        print("Inside the contructor")
        print(Test.a)
        print(self.a)
    def m1(self):
        print("inside the instnce method")
        print(Test.a)
        print(self.a)
    @classmethod
    def m2(cls):
        print('inside the classmethod')
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print('inside the static method')
        print(Test.a)

t = Test()
t.m1()
t.m2()
t.m3()
print('from outside of the class ')
print(Test.a)
print(t.a)

print('----------------------------------------------')

class Test:
    a  = 20
    def __init__(self):
        Test.a = 30
    @classmethod
    def m1(cls):
        cls.a = 49
        Test.a = 40
    @staticmethod
    def m2():
        Test.a = 50

t = Test()
t.m1()
t.m2()
Test.a = 60
print(Test.a)
print(t.a)