# import random
# a=random.randint(600,900)

class hdfc:
    def __init__(self):
        import random
        self.a=random.randint(500,900)
        # self.a=a

    def check(self):
        if 750<=self.a<=900:
            print(self.a,'Loan Approved by hdfc bank')
class yes(hdfc):
    def __init__(self):
        super().__init__()
        
    def display(self):
            super().check()
            if 650<=self.a<750:
                print(self.a,' Loaned Approved by yes bank')
            else:
                print(self.a,"Loan not approved")
obj=yes()

obj.check()