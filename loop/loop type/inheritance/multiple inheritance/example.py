class add:
    @staticmethod
    def addd(a,b):
        return a+b
class sub:
    @staticmethod
    def subt(a,b):
        return a-b
class mul:
    @staticmethod
    def multi(a,b):
        return a*b
class div:
    @staticmethod
    def division(a,b):
        return a/b
    
class operation(add,sub,mul,div):
    def __init__(self):
        self.a=int(input('Enter the first number'))
        self.b=int(input('Enter the second number'))
        self.op=(input('Enter the operation in  + - * / only '))

        if self.op=="+":
            print(self.addd(self.a,self.b))
        if self.op=="-":
            print(self.subt(self.a,self.b))
        if self.op=="*":
            print(self.multi(self.a,self.b))

        if self.op=="/":
            print(self.divison(self.a,self.b))    

obj =operation() 