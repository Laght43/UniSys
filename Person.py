from abc import ABC

class Person(ABC):
    def __init__(self, name: str, surname: str, age: int):
        self._name = name
        self._surname = surname
        self._age = age

    def printInfo(self):
        print("Name: ", self._name, " Age: ", self._age)