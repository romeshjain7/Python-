class Hdfc:
    def __init__(self):
        self.bankname='HDFC'
        self.branch='BTM'
        self.bal=1230

class yes(Hdfc):
    def __init__(self):
        super().__init__()
        self.name='Yesbank'
        self.place='BTM'
        self.age=20
    
    def display(self):
        print(self.name)
        print(self.place)
        print(self.age)
        print('HDFC Details')
        print(self.bankname)
        print(self.branch)
        print(self.bal)

obj=yes()
obj.display()

