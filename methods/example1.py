class method:
    a=10
    b=20
    def __init__(self):
        self.p=100
        self.q=200

    def display(self):

        self.p='hai'
        self.q='hello'
        print(self.p,self.q)

    @classmethod
    def clsdisplay(cls):
        cls.a='class a is updated'
        cls.b='class b is updated'
        print(cls.a,cls.b)

    @staticmethod
    def normal():
        print('This is a normal function ')

obj=method()
obj2=method()
obj.display()
print(obj.p,obj.q)
obj.clsdisplay()
print(obj.a,obj.b) 
obj2.normal()

