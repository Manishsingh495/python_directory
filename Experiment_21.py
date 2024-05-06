# Single Inheritance

# Write a python program to perform single inheritance.



class Parent:
    def __init__(self, data1):
        self.data1 = data1

    def display(self):
        print("Data 1 =", self.data1)


class Child(Parent):
    def __init__(self,  data1, data2):
        super().__init__(data1)
        self.data2 = data2

    def display(self):
        super().display()
        print("Data 2 =", self.data2)


obj = Child(10, 20)
obj.display()