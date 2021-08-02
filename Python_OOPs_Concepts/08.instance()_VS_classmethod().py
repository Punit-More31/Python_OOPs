'''* Instance methof vs class method*
    
    1.Inside the method body if we are using atleast one instance variable then compulsary we should declare that method as instance method
    2.Inside method body if we are not required to use any decorator. To declare class nethod compulsary we should use @classmethod decorator
    3.The first argument to the instance method should be self, which is reference to current object and by using self, we can access instance variable inside the method
    4.The first argument to the classmethod should be cls, which is referennce variable current class object and by using that we can access static variable 
    5.Inside instance method we can access both instance and static variabale.Inside the classmethod we can access only static variable and we cannot access instance variable
    6.we can call instance method by using object refernce. we can call classmethod either by using object reference or by using class name, but recommended to use classname.

    INSTANCE METHOD VS CLASS METHOD VS STATIC METHOD:
    1. If we are using any instance variable method body then we should go for instance method. We should call by usning objects only
    2. If we are using only static variables inside method body then this method no way related to a particular objects, we should devclre such type of method as classmethod. We can call either by using object reference or by sung class name.
    3.If we are not using any instace variable and any static variable inside method oody, to define such type of gerneral utility method we should go for static methods. we can call either by using objects reference or by using class name.

    If we are not using any decorator:
    -----------------------------------
    for classmethod , @classmethod decorator is mandatory.
    for staticmethod, @staticmethod decortor is optional
    Without any decorator the method can be either instance method or static method.
    If we are calling by using objects reference then it should be instnce method .
    If we are calling by using class name then it should be static method.

    eg.1
    class Test:
        def m1():
            print('Some method')
    t   = Test()
    t.m1()
TypeError:m1() takes 0 positional arguments but 1 was given
In above example, python will consider the method as instance method, but we are not declaring self variable. Hence we are getting error.

    eg.2 
    class Test:
        def m1():
            print('some method')
        Test.m1()

    output: Some method

    eg.3 
    class Test:
        @staticmethod
        def m1():
            print('some method')
        t = Test()
        t.m1()
    
    output:some method

    eg.4
     class Test:
        def m1(x):              //self is missing
            print('some method',x)
        t = Test()
        t.m1(10)

        TypeError:m1() takes 1 positional argument but 2 were given

'''

class Animal :
    legs = 4

    @classmethod
    def walk(cls, name):
        print('{} walks with {} legs'.format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')

''' Write  program to track no of objects created'''

class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1
    @classmethod
    def getNoOfObjects(cls):
        print('The number of objects created :',cls.count)
t1=Test()
t2=Test()
t3=Test()
t4=Test()
Test.getNoOfObjects()

class DurgaMath:
    @staticmethod
    def add(x,y):
        print('The Sum:', x+y)

    @staticmethod
    def Average():
        a= float(input('Enter the two no: '))
        b = float(input('Enter the two no: '))

        print('The average value:',int((a+b)/2))

DurgaMath.add(10, 20)
DurgaMath.Average()



