class Singleton:
    __instance = None
    _initialized = False

    def __init__(self, name, age):
        if not self._initialized:
            self.name = name
            self.age = age
            Singleton._initialized = True

    @staticmethod
    def get_instance(name, age):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton(name, age)
        return Singleton.__instance

    def print_method(self):
        print(f"Printing Singleton Object {self.name} {self.age}")


singleton1 = Singleton("Usman", 21)
#singleton2 = Singleton("Ali", 23)
singleton1.print_method()
#singleton2.print_method()
