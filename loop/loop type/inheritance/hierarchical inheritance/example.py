class animal:
    def __init__(self):
        self.name=input('Enter the name')
        self.eyes=input('Enter the no of eyes')
        self.hands=input('Enter the no of hands')
    def display(self):
        print(f'Name ->{self.name}')
        print(f'Eyes ->{self.eyes}')
        print(f'Hands ->{self.hands}')
        return self
    def eat(self):
        print('This animal can eat')
        return self

    def sleep(self):
        print('This animal can sleep')
        return self

    def run(self):
        print('This animal can run')
        return self

    def walk(self):
        print('This animal can walk')
        return self

    def kill(self):
        print('This animal can kill')
        return self

    def think(self):
        print('This animal can think')
        return self

class human(animal):
    pass
class tiger(animal):
    pass
class human(animal):
    pass
class human(animal):
    pass
class human(animal):
    pass

obj =human() 
obj.display() .eat() .sleep() .run() .walk()
