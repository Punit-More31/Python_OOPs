''' Local Variables
--------------------
    Method Level variables 
    we should not use self, cls , classname

    GLOBAL VARIABLE
----------------------
    from the clacc we can access the global variable direclty 
    Within the method of a class we can declare global variables by using global keyword
'''

x = 100         #Global variable 
class Test:
    x = 300
    def m1(self):
        global z
        z = 2
        print(x)
        print(self.x)
    def m2(self):
        print(x)
        print(self.x)

t=Test()
t.m1()
t.m2()
print(z)