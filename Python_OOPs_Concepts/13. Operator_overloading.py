'''
Polymorphism:
1.Duck Typing Phylosophy of python
2.Overloading
    Operator Overloading
    Method Overloading
    Constructor Overloading
3.Overriding 
    Method Overriding
    Constructor Overriding

    But you told that there is no concept of Constructor Overloading in python.....

    METHOD OVERLOADING AND CONSTRUCTOR OVERLOADING IS NOT SUPPORTED BY PYTHON

 ------------------------------------------

 Poly mean many
 morphs mean forms

 one name multiple forms

 Overloading:
 ---------------------------------------------------
 10+20-->30
 'Durga'+'Soft'-->durgasoft    // + same operator but use for adding as well as concatention ie.polymoephism


 10*3-->30
 'durga'*3-->durgadurgadurga

 Method Overloading: //same name different parameters
 deposit(cash)
 deposit(cheque)
 deposit(dd)

 abs(int i)
 abs(long i)
 abs(float i)

 Operator Overloading:  //in java there is no operator overloading but in python there is operator overloading.You can use same operator for your use also
 --------------------------------------------------------
 
 Operator Overloading is implemented by Magic method
 ----------------------------------------------------
 + -->__add__()
 - -->__sub__()
 * -->__mul__()
 / -->__div__()
 % -->__mod__()
 // -->__floordiv__()
 ** -->__pow__()

 += -->__iadd__()
 -= -->__isub__()
 /= -->__imul__()
 %= -->__idiv__()
 //= -->__ifloordiv__()
 **= -->__ipow__()

 > -->__gt__()
 >= -->__ge__()
 <= -->__le__()
 == -->__eq__()
 != -->__ne__()

 




whenever we add two book objects my requirement is to return the adding of book pages

when we write print(b1) internally __str__() is called  as in java tostring() is called.

if you want meaninigful string representation for your object whenver is printing then we need to overide __str__() method. i.e print(b1)      //
'''
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return self.pages+other.pages
    def __mul__(self,other):
        return self.pages*other.pages
    def __div__(self,other):
        return self.pages/other.pages

b1 = Book(100)
b2 = Book(200)
# b3 = Book(700)
# print(b1+b2+b3)     #unsupported type:'int' or 'Book'
print(b1+b2)           
print(b1*b2)         
print(b1)

print("---------------------------------------------")

class Book:
    def __init__(self,pages):
        self.pages  = pages
    
    def __str__(self):
        return "The number of pages:" + str(self.pages)
    
b1 = Book(100)
print(b1)

print("---------------------------------------------")

'''whenever we are calling + operator then __add() will be called
    whenever we are printint Book object reference
then __str__() will be called.
    + operator return type will become __add__()
method return type.

'''
class Book:
    def __init__(self,pages):
        self.pages  = pages
    
    def __str__(self):
        return "The number of pages:" + str(self.pages)
    def __add__(self,other):
        total = self.pages + other.pages
        b = Book(total)
        return b
    

b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
b4 = Book(200)
print(b1+b2+b3+b4)
print("-------------------------------")
class Book:
    def __init__(self,pages):
        self.pages  = pages
    
    def __str__(self):
        return "The number of pages:" + str(self.pages)
    def __add__(self,other):
        total = self.pages + other.pages
        b = Book(total)
        return b
    def __mul__(self,other):
        total = self.pages * other.pages
        b = Book(total)
        return b              # here we return book object

b1 = Book(100)
b2 = Book(200)
b3 = Book(300)
b4 = Book(200)
print(b1+b2*b3+b4)

print("---------------------------------------")
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __lt__(self,other):
        return self.marks<other.marks
    
s1 = Student('durga',100)
s2 = Student('ravi',200)
print(s1<s2)
print(s2<s1)

print('------------------------------')

class Employeee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __mul__(self,other):
        return self.salary * other.days
class TimeSheet:
    def __init__(self,name, days):
        self.name = name
        self.days = days
    def __mul__(self, other):
        return self.days * other.salary
e = Employeee('Surga', 500)
t = TimeSheet('Surga', 25)
print('This month salary:',e*t)
print('This month salary:',t*e)


    


