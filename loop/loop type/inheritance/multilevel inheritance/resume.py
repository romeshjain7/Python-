class resume:
    print('RESUME')
    def __init__(self):
        self.place=input('Place')
        self.date=input('Date')
    def display(self):
        print(self.place)
        print(self.date)
class education(resume):
    def __init__(self):
        super().__init__()
        print('EDUCATION')

        self.per10=float(input("Enter your 10th per."))
        self.per12=float(input("Enter your 12th per."))
        self.perUG=float(input("Enter your UG per."))
    def display(self):
        super().display()
        print(self.per10)
        print(self.per12)
        print(self.perUG)
class skills(education):

    def __init__(self):
        super().__init__()
        print('Skills')

        self.s1=input('Enter your first skill')
        self.s2=input('Enter your second skill')
    def display(self):
        super().display()
        print(self.s1)
        print(self.s2)
class hobbies(skills):
    def __init__(self):
        super().__init__()
        print('HOBBY')
        self.hobby=input('Enter your hobbies')
    def display(self):
        super().display()
        print(self.hobby)
obj=hobbies()
obj.display()
