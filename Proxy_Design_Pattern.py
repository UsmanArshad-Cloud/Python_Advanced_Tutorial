# Proxy design patterns are just like decorators we can add functionality of an object without changing its functionality
# The main purpose is to add extra layer of functionality and control to thr real object
from abc import ABC, abstractmethod


class IClass(ABC):
    @abstractmethod
    def get_costly_data(self):
        pass


class RealClass(IClass):
    def get_costly_data(self):
        print("Now doing some costly work for real")


class ProxyClass(IClass):
    def __init__(self):
        self.realobject = None

    def get_costly_data(self):
        if self.realobject == None:
            self.realobject = RealClass()
        self.realobject.get_costly_data()


proxyobj = ProxyClass()
proxyobj.get_costly_data()
