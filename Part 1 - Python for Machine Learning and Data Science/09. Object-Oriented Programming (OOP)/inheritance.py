#creating class B from A
class A:
    a = 1
    b = 2
    
    def method1(cls):
        print('a = ',cls.a)
        print('b = ',cls.b)

class B(A):
    c = 3
    
    def method2(cls):
        print('c = ',cls.c)
#creating object of class B, we can access all the members of both the class A & B
obj = B()
obj.method1()
obj.method2()