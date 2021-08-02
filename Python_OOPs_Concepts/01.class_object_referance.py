for i in range(1,11):
    print(i,i*3,i*4,i*5, end="\n")
    


class Student:
    cname = "DURGASOF"                # This is static variable or class level variable where only one cpy is created 
    def __init__(self, eno, ename):
        self.eno = eno
        self.ename = ename

    def display(self):#compulsary Self variable as first Argument
        print("Hello Eno = ", self.eno)
        print("Hello Ename = " +self.ename)

    @classmethod 
    # it is a decorator for clss level 
    # variable to acccess                            
    def getCollegeName(cls):
        print("Collge Name =" +cls.cname)

    @staticmethod
    def findAverage(x, y):# No way related to object and class
        print("Average =",(x+y)/2)


s1 = Student(100, "Sedha")
s1.display()
Student.getCollegeName()# To access class level objects or 
Student.findAverage(10,20)# We can call static method or genral method using both class name as well as objecr name
s1.findAverage(30,29)

