''' Setter and getter methods are not built in method.
    insted of constructor We can use this method. we can call this method() as  instance method
    we use this method for security reasons

    print(s.name) // Direct accesss no validation
    print(s.getName()) // Provide security i.e we can write validation code here like asked for password like stuff

    Hiding data behind method===> Encapsulation

    drawback of Encapsulation::
        No. of lines of code increases and reduces execution time

    inside constuctor we cant write validation code code we can but it's not industry standards

'''
class Student:
    def setName(self, name):
        self.name = name
    def getName(self):
        return  self.name
    def setMarks(self, marks):
        self.marks= marks
    def getMarks(self):
        return  self.marks



n = int(input('Enter the no of Student: '))

for i in range(n):
    name = input('Enter the student Name: ')
    marks = int(input('Enter the marks of the student: '))
    s = Student()
    s.setName(name)
    s.setMarks(marks)

    print("Hi",s.getName())
    print("Your marks are", s.getMarks())
    print("*"*20)