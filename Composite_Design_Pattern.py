#Diff Classes inherited from the same interface class but one class can contains multiple other classes.

from abc import ABC, abstractmethod

# Component interface
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

# Leaf (Simple Shape)
class SimpleShape(Graphic):
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f"Drawing {self.name}")

# Composite (Complex Shape)
class ComplexShape(Graphic):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, graphic):
        self.children.append(graphic)

    def remove(self, graphic):
        self.children.remove(graphic)

    def draw(self):
        print(f"Drawing {self.name}")
        for child in self.children:
            child.draw()

# Usage:
line = SimpleShape("Line")
circle = SimpleShape("Circle")
rectangle = SimpleShape("Rectangle")

polygon1 = ComplexShape("Polygon 1")
polygon1.add(line)
polygon1.add(circle)

polygon2 = ComplexShape("Polygon 2")
polygon2.add(rectangle)
polygon2.add(polygon1)

# Drawing the entire graphical scene
polygon2.draw()
