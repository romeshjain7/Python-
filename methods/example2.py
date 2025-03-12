class kill:
    a=eval(input('Enter the Number in a variable'))
    b=eval(input('Enter the Number in b variable'))

    @staticmethod
    def oper(p,q):
        return p+q,p-q,p*q,p/q
    
    @classmethod
    def operation(cls):
        print('Class method')
        out=cls.oper(cls.a,cls.b)
        return out
    
    def __init__(self):
        self.r =eval(input('Enter a number in r variable'))
        self.s =eval(input('Enter a number in s variable'))
    
    def objoperation(self):
        print('Object Method')
        res=self.oper(self.r,self.s)

obj=kill()
print(obj.operation())
print(obj.objoperation())
