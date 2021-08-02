'''
mro(O) = OBJECT
MRO(A) = A,O 
MRO(B) =B,O 
MRO(C) = C,O 
MRO(X) = X,A,B,O 
MRO(Y) = Y,B,C,O 
MRO(P) = P,X,Y,C,A,B,O  //

C3 Algorithm:
mro(P) = P+Merge(mro(X),mro(Y),mro(C),XYC)
mro(P) = P+Merge(XABO, YBCO, CO, XYC)
mro(P) = P+X+Merge(ABO, YBCO, CO, YC)
mro(P) = P+X+A+Merge(BO, YBCO, CO, YC)
mro(P) = P+X+A+Y+Merge(BO, BCO,CO,C)
mro(P) = P+X+A+Y+B+Merge(O, CO, CO,C)
mro(P) = P+X+A+Y+B+C+Merge(O,O,O)
mro(P) = P+X+A+Y+B+C+O

If head element of the first list not present inhte tail part of the other list then consider that element in the 
result and remove that element from all the lists 

 ABCDEF 
accept head all the remaining consider as tail part

'''

class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(X.mro())
# OUTPUT : [<class '__main__.X'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]