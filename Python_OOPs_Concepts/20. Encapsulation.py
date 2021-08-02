'''WHAT IS ENCAPSULATION?
1.IN AN OBJECT ORIENTED PYTHON PROGRAM, YOU CAN RESTRICT ACCESS TO METHOD AND VARIABLE.
2.THIS CAN PREVENT THE DATA FROM BEING MODIFIED BY ACCIDENT AND IS KNOWN AN ECAPSULATION.
3.ENCAPSULATION CAN BE ACHIECED USINF PRIVATE VARIABLES AND PEIVATE METHODS.

TYPE:                     Description
Public methods          : Accessible form anywhere.
private methods         : Accessible only in their own 
                          class starts with two underscores.
------------------------------------------------------------  

public variable         : Accessible form anywhere.
private variables       : Accessible form anywhere
                        : Accessible only in their own 
                          class or by a method if defined starts with two underscores.



'''
#private variable can be access only within the method
from typing import ClassVar


class myClass:
  __a = 10

  def disp(self):
    print(self.__a)
obj = myClass()
obj.disp()

# print(myClass.__a)#we can not access because it is private variable

print('----Private method demo-------------------')
class myClass:
  def __disp(self):
    print('This is disp1 method')

  def disp2(self):
    print('This is disply2 method')
    self.__disp()

obj = myClass()
# obj.__disp1()#not correct
obj.disp2()

''' HOW TO ACCESS PRIVATE VARIABLE AND MEHTOD OUTSIDE OF THE CLASS'''
#WE CAN ACCESS THE PRIVATE VARIABLE OUTSIDE OF THE CLASS INDIRECTLY USING METHOD
print('---------------------')
class myClass1:
  __empid=101
  def getEmpId(self,empid):
    self.__empid=empid

  def dispempid(self):
    print(self.__empid)
obj = myClass1()
obj.getEmpId(104)
obj.dispempid()
