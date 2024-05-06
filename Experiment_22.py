class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
class C(A,B):
    def __init__(self):
        self.c='c'
        super().__init__()
        print(self.c)
obj=C(15,20)
obj.print()                       
     