from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def draw(self):
        pass

class SimpleShape(IShape):
    def __init__(self,name):
        self.name=name
    def draw(self):
        print(f"Drawing {self.name}")


class CompositeShape(IShape):
    def __init__(self,name):
        self.name=name
        self.__children=[]
    def add(self,other):
        self.__children.append(other)
    def remove(self,other):
        self.__children.append(other)
    def draw(self):
        print(f"Drawing {self.name}")
        for shape in self.__children:
            print(f"Drawing {shape.name}")

Line=SimpleShape("Line")
Circle=SimpleShape("Circle")
PolyGon=CompositeShape("PolyGon")
PolyGon.add(Line)
PolyGon.add(Circle)
PolyGon.draw()
