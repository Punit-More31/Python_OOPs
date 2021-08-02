'''
Types of Variable
=========================
instance variable 
static variable 
local variable

Types of Method
=========================
instance method 
static method 
class method

'''
'''
1.instance variable
==================================================================================================
If the value of variable varied from object to object such type of variable for every variable a seperate copy will be created
    * Where we have to declare instance variable *
    1.Inside constructor by using self
    2.Inside instance method by using self
    3.From outside of the class by using object reference 
    
    * How to access instance variable *
    1.1.Within the class by using self
    1.2.From outside of the class by using object  reference 

    * How to delete instance variable *
    1.1.1 Withi the class
          del self.a
    1.2.2 outside from the class
          del objectReference.variable_name
'''

class Student:
    def __init__(self, name,roll_no):
        self.name = name                # 1
        self.roll_no = roll_no

    def info(self):                     #2
        self.marks = 60

s1 = Student("Rohan", 20)
s1.info()
print(s1.__dict__)
s1.age = 20                           # 3
print(s1.__dict__)                    # It gives the dictionary of total instance variable

print("-----------------------------------------------------------------------------------------")

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def m1(self):
        self.d =40

    def m2(self):
        self.e = 50

t1 = Test()
t1.m1()
t2 = Test()
t2.m2()
t2.s = 200
t2.y = 400
print(t1.__dict__)
print(t2.__dict__)

print("-----------------------------------------------------------------------")

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def info(self):
        print("Name is = ", self.name)              #1.1
        print("Roll no = ", self.rollno)

f1 = Student("mahi", 20)
f1.info()
print(f1.name, f1.rollno)                           #1.2

print("-------------------------------------------------------------------------")

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def delete(self):
        del self.a                          #1.1.1
        del self.c
    
d1 = Test()
print(d1.__dict__)                          #2.2.2
d1.delete()                         
print(d1.__dict__)
