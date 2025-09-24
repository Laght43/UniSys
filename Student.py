from Person import Person
from Group import Group

class Student(Person):
    def __init__(self, name:str, surname: str, age: int, id: int, grade: int, specialty: int, group: Group):
        super().__init__(name, surname, age)
        self.__id = id
        self.__grade = grade
        self.__specialty = specialty
        self.__group = group

    def printInfo(self):
        print("Name: ", self._name, " Surname: ", self._surname, " Age: ", self._age, " Specialty: ", self.__specialty, " ID: ", self.__id, " Group: ", self.__group, " Grade: ", self.__grade)

    @property
    def id(self):
        return self.__id
    
    @property
    def grade(self):
        return self.__grade
    
    @property
    def specialty(self):
        return self.__specialty
    
    @property
    def group(self):
        return self.__group