class main:
    def __init__(self):
        self.a=int(input('Enter a number in  variable a'))
        self.b=int(input('Enter a number in  variable b'))
    def display(self):
        print(self.a+self.b)
class c1(main):
    def __init__(self):
        super().__init__()
        self.c=int(input('Enter a number in variable c'))
        self.d=int(input('Enter a number in variable d'))
    def display(self):
        super().display()
        print(self.a-self.b-self.c-self.d)
class c2(c1):
    def __init__(self):
        super().__init__()
        self.e=int(input('Enter a number in variable e'))
        self.f=int(input('Enter a number in variable f'))
    def display(self):
        super().display()
        print(self.a*self.b*self.c*self.d*self.e*self.f)
obj=c2()
obj.display()
        