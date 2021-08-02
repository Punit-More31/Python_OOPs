'''Types of inheritance
1.Single Level Inhritance
2.Mult level inheritance
3.Hierachical
4.Multiple
5.Hybrid
6.Cyclic

'''
# single Inheritance
class P:
    def m1(self):
        print('Parent method')
class C(P):
    def m2(self):
        print('Child Method')
c = C()
c.m1()
c.m2()

print('-----------------------------')
# Multi level Inhetitance
class P:
    def m1(self):
        print('Parent method')
class C(P):
    def m2(self):
        print('Child Method')
class CC(C):
    def m3(self):
        print("sub-child method")
c = CC()
c.m1()
c.m2()
c.m3()

print("------------------------------------------")

# Hierachical Inheritance
class P:
    def m1(self):
        print('Parent method')
class C1(P):
    def m2(self):
        print('Child Method')
class C2(P):
    def m3(self):
        print("sub-child method")
class C3(P):
    def m4(self):
        print('su b-sub-child')
c = C3()
c.m4()
c.m1()

print('-----------------------------------')

# Mulltiple Inheritance
# If Both paratns having a same method which method will be executed in order of parent class declareation but in java Multiple inheritance is not supported because of ambiguily in choosing the method if both class having the same method name:
class P1:
    def m1(self):
         print('P1 Method')
class P2:
    def m1(self):
        print('P2 method')
class C(P1,P2):
# class C(P2,P1):
    pass

c = C()
c.m1()

# Hybrid Inheritance
# mixute of two or more inheritance


# Cyclic inheritance


 



