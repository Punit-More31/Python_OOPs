'''super()
to call parent class members from child class, we use super().Giggest advantage is code reusability

To invoke parent class constuctor form the chid purpose we use super().

'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
    def display(self):
        print('name:',self.name) 
        print('age:',self.age)
        # 100 properties
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks
    
    def display(self):
        # print('name:',self.name) 
        # print('age:',self.age)
        super().display()
        print('Roll no:',self.rollno)
        print('marks:',self.marks)

class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.salary = salary
        self.subject = subject

    def display(self):
        # print('name:',self.name) 
        # print('age:',self.age)
        super().display()
        print('salary:',self.salary)
        print('subject:',self.subject)

s  = Student('Ravi',23,101,90)
p = Teacher('Surga',62,10000,'Python')
s.display()
print('---------------------------------------')
p.display()

print('-------------------------------------------')

# HOW TO CALL A PARTICULAR PARENT CLASS METHOD BY USING SUPER()

class A:
    def m1(self):
        print('A class Method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    # def m1(self):
    #     print('D class method')
    pass
class E(D):
    def m1(self):
        # print('E class method')
        super().m1()
e = E()
e.m1()

# HOW TO CALL A PARTICULAR PARENT CLASS METHOD BY USING SUPER():
# THERE ARE TWO WAYS
# 1.parentclassname.methodname(self) ie.B.m1(self)
# 2.super(D, self).m1()  superof D mean C' ,method
print('------------------------------------------------')

class A:
    def m1(self):
        print('A class Method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    # def m1(self):
    #     print('D class method')
    pass
class E(D):
    def m1(self):
        # print('E class method')
        super(B,self).m1()
        # B.m1(self)
        # super(C, self).__init__()
        
e = E()
e.m1()
print('--------------------------------------------------')
# Loop Holes in Super()


# from child class by using super() We can't call parent class instance variables. We should use self only
# From child class by using super() method we can call parent class static variable

class P:
    a = 10
    def __init__(self):
        self.b = 20
class C(P):
    def m1(self):
        print(super().a)
        print(self.b)
c = C()

print("------------------------------------")

class P:
    def __init__(self):
        print('parent Constuctor')
    def m1(self):
        print("parent instance method")
    @classmethod
    def m2(cls):
        print('parent class method')
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    # def method1(self):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c = C()
# c.method1()
 