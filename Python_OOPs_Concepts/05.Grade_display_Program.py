import sys
class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks =  marks 
    def display(self):
        print('Hi',self.name)
        print('Your marks:',self.marks)
    def grade(self):

        if self.marks >= 80 and self.marks<=100:
            print('First Grade')
        elif self.marks >= 60 and self.marks <= 60:
            print('seconde grade')
        elif self.marks >= 35 and self.marks <= 35:
            print('Third Grade')
        elif self.marks == 140:
             print('Invalid Choice')
             sys.exit()
        else:
            print("Choose Valid option")



      
n = int(input('Enter the no of Student: '))

for i in range(n):
    name = input('Enter the student Name: ')
    marks = int(input('Enter the marks of the student: '))
    s = Student(name, marks)
    s.display()
    s.grade()
    print('*'*20)
    