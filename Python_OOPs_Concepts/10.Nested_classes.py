class Person:
    def __init__(self, name, dd,mm,yyyy):
        self.name = name
        self.dob = self.DOB(dd,mm,yyyy)
    def display(self):
        print('Name:',self.name)
        self.dob.display()
     
    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy
        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd,self.mm,self.yyyy))

p = Person('Sunny', 24, 5, 2001)
p.display()
p.dob.display()

print('------------------------------------------')

class Human:
    def __init__(self):
        self.name = 'Durga'
        self.head = self.Head()

    def display(self):
        print('Name:',self.name)
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            print('Talking...')

        class Brain:
            def think(self):
                print('Thinking...')

h = Human()
h.display()
