class P:
    a=10
    b=20
class c(P):
    c=30
    d=40
class c1(c):
    e=50
    f=60
class c2(c1):
    g=70
    h=80
class c3(c2):
    i=90
    j=100
obj=c3()
print(obj.a,obj.b,obj.c,obj.d,obj.e,obj.f,obj.g,obj.h,obj.i,obj.j)