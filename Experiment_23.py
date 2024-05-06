import math

class complex1:
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,c2):
        return(self.num1+c2.num2)
class complex2:
    def __init__(self,num2):
        self.num2=num2
c1=complex1(10+ i5)
c2=complex2(15+ i7)
c3=c1+c2
print(c3)