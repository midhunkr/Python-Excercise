class Animal:
    def __init__(self):
        self.name="Animal"
        self.alive=True
    def isAlive(self):
        if(self.alive):
            print("This animal is alive")
    
class Man(Animal):
    def __init__(self):
        self.name="Man"
        self.age=90
    def say_hello(self):
        print("hi i am "+self.name+" and i am",self.age," years old")

man=Man()
man.say_hello()
anm=Animal()
anm.isAlive()
