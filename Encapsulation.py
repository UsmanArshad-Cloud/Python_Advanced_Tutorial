class MyClass:
    count = 0

    def __init__(self, var1, var2, var3):
        self.public_variable = var1
        self._protected_variable = var2
        self.__private_variable = var3
        MyClass.count+=1

    @property
    def private_variable(self):
        return self.__private_variable

    @private_variable.setter
    def private_variable(self, value):
        self.__private_variable = value

    @staticmethod
    def objectCounter():
        return MyClass.count

class NewClass(MyClass):
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)

    def print_protected(self):
        print(f"This is protected{self._protected_variable}")


obj = MyClass(1, 2, 3)
print(obj.public_variable)
print(obj.private_variable)
obj.private_variable = 4
print(obj.private_variable)
obj1 = NewClass(1, 2, 3)
obj1.print_protected()

print(MyClass.objectCounter())
