from Student import Student
from Group import Group

if __name__ == "__main__":
    stud1 = Student("Vadym", "Cherkashen", 18, 1, 43)
    stud2 = Student("asd", "sad", 14, 2, 456)
    group = Group()
    group.addStudent(stud1)
    group.addStudent(stud2)
    group.printAll()
    group.findBestStudent()