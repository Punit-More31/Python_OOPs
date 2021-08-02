'''*a means variable length arguments '''


class Test:
    def sum(self,a = None,b = None, c = None):
        if a != None and b != None and c!=None:
            print('The sum of 3 number:',a+b+c)
        elif a!=None and b!=None:
            print('The sum of 2 number:',a+b)
        else : print('Please provide 2 or 3 argument')
t = Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10,0)
t.sum(10)

print('------------------------------------')

class Test:
    def m1(self, *a):
        total = ''
        for x in a :
            total = total + x
        print('The result:\n', total)

t = Test()
t.m1('durga')
t.m1('durga','10')
t.m1('durga','software','solution')

print('------------------------------------------')

'''merthod overloading and constructor overloadding are not supportd by python so when execute the method oveloading it considers only last method or last constructor'''
class Test:
    def m1(self):
        print(no-argument)
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('Two-arg method')

t = Test()
# t.m1(10) error
t.m1(10,20)                    #this consider only the last method so gives a an error becauase in lasts method there are two argument a and b. it is also applicable for constructor overloading

print('------------------------------------')

class Test:
    def __init__(self,*a):
        print("Constuctor with any number of argument")
t = Test()
t = Test(10)
t = Test(20,20)
t = Test(10,20,30)
t = Test(10,30,30,50,305,3043)


