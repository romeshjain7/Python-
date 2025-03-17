class hotel:
    m ='masala dosa'
    a='pay amount'

    def __init__(self):
        self.am='paid'
        self.order='ordered'

    def display(self):
        print(self.m)
        print(self.a)
obj=hotel()
print(obj.a)