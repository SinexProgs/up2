from datetime import datetime


class Student:
    _surname = None
    _birthdate = None
    _group_number = None
    _grades = [0] * 5

    def set_surname(self, surname):
        self._surname = surname

    def set_birthdate(self, birthdate):
        self._birthdate = datetime.strptime(birthdate, '%d-%m-%Y').date()

    def set_group_number(self, group_number):
        self._group_number = group_number

    def add_grade(self, grade : int):
        if grade < 1 or grade > 5:
            return
        self._grades[grade - 1] += 1

    def _get_avg_grade(self):
        grades_count = sum(self._grades)
        grades_sum = 0
        for i in range(len(self._grades)):
            grades_sum += (i + 1) * self._grades[i]
        return grades_sum / grades_count

    def _stringify_grades(self):
        grades = []
        for i in range(len(self._grades)):
            grades.append(f"{i + 1}: {self._grades[i]}")
        return ", ".join(grades)

    def print_information(self):
        print(f"Surname: {self._surname}")
        print(f"Birthdate: {self._birthdate}")
        print(f"Group number: {self._group_number}")
        print(f"Grades: {self._stringify_grades()}")
        print(f"Average grade: {self._get_avg_grade()}")

    def print_if_matching(self, surname, birthdate):
        if self._surname == surname and self._birthdate == datetime.strptime(birthdate, '%d-%m-%Y').date():
            self.print_information()


cur_student = Student()
cur_student.set_surname(input("Enter student's surname: "))
cur_student.set_birthdate(input("Enter student's birthdate (DD-MM-YYYY): "))
cur_student.set_group_number(int(input("Enter student's group number: ")))
print("Enter student's grades: ")
while True:
    cur_grade = int(input())
    if cur_grade < 1 or cur_grade > 5:
        break
    cur_student.add_grade(cur_grade)

cur_student.print_if_matching(input("Enter desired student's surname: "),
                              input("Enter desired student's birthdate (DD-MM-YYYY): "))