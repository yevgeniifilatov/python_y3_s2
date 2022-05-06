#!/usr/bin/python3

from random import randrange

class Student:

    def __init__(self):
        self.name: str
        self.surname: str
        self.birthdate: int
        self.acceptance_date: int
        self.name = "Yehor"
        self.surname = "Besedin"
        self.birthdate = 21032001
        self.acceptance_date = 1092018


class BudgetStudent(Student):

    def __init__(self):
        super().__init__()
        self.scholarship: float
        self.contract_sum: float
        self.scholarship = 1299
        self.contract_sum = 2992.5


class Group:

    def __init__(self, *students: Student):
        self.students = students
        self.group_number: str
        self.group_number = "515i"


class Discipline:

    def __init__(self):
        self.name: str
        self.credits: int
        self.semester: int
        self.name = "random"
        self.credits = randrange(100, 299)
        self.semester = randrange(1, 9)


class Lector:

    def __init__(self, *dcp: Discipline):
        self.name: str
        self.surname: str
        self.middle_name: str
        self.birthdate: int
        self.exp: int  # or could be type float if counted in increments shorter than a year
        self.dcp = dcp

    def total_subject(self):
        total_sub = len(self.dcp)
        if total_sub <= 0:
            print("No disciplines have been added")
            exit(0)
        print("Total number of subjects: %i" % total_sub)
        total_credits = sum([self.dcp[i].credits for i in range(total_sub)])
        print("Total number of credits: %i" % total_credits)
        return total_sub, total_credits


if __name__ == '__main__':
    student1 = Student()
    std2 = Student()
    std3 = Student()
    b_std_2 = BudgetStudent()
    b_std_1 = BudgetStudent()
    grp1 = Group(student1, std2, std3, b_std_1, b_std_2)
    dcp1 = Discipline()
    dcp4 = Discipline()
    dcp3 = Discipline()
    dcp2 = Discipline()
    lector1 = Lector(dcp1, dcp2, dcp3, dcp4)
    lector1.total_subject()
