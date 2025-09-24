from Group import Group

class Faculty:
    def __init__(self, name: str, specialties: list):
        self.__name = name
        self.__specialties = specialties
        self.__groups = []

    def addGroup(self, group: Group):
        if group not in self.__groups:
            if group.specialty in self.__specialties:
                self.__groups.append(group)
            else:
                print("Group specialty no in faculties specialties")
        else:
            print("Group already in faculty")