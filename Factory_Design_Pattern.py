# Factory Design Pattern is the creational design pattern that provides an interface for creating object
# but allow the subclasses to decide which class to instantiate
from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def person_method(self):
        pass


class Student(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"Student's name is {self.name}")


class Teacher(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"Teacher's name is {self.name}")


class PersonFactory:
    @staticmethod
    def createPerson(input):
        if input == 1:
            return Student("S")
        elif input == 2:
            return Teacher("T")
        else:
            return -1


teacher = Teacher("Haider")
student = Student("Usman")
teacher.person_method()
student.person_method()

user_input = int(input("Press 1 for teacher and 2 for Student"))
person = PersonFactory.createPerson(user_input)
person.person_method()
