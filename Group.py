from Student import Student

class Group:
    def __init__(self, specialty: int, name: str):
        self.__students = []
        self.__specialty = specialty
        self.__name = name
    
    def addStudent(self, student: Student):
        if student.specialty == self.__specialty:
            self.__students.append(student)
        else:
            print("specfiality dont matches")

    def removeStudent(self, id):
        for student in self.__students:
            if student.id == id:
                self.__students.remove(student)

    def printAll(self):
        for student in self.__students:
            student.printInfo()

    def findBestStudent(self):
        bestMark = 0
        for student in self.__students:
            if student.grade > bestMark:
                bestMark = student.grade
        for student in self.__students:
            if student.grade == bestMark:
                return student

    @property
    def specialty(self):
        return self.__specialty
    
    @property
    def name(self):
        return self.__name