class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_rate(self):
        if len(self.grades.items()) == 0:
            return 0
        else:
            sum_of_rates = 0
            amount_of_rates = 0
            for course, rate in self.grades.items():
                sum_of_rates += sum(rate)
                amount_of_rates += len(rate)
            return sum_of_rates / amount_of_rates

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за домашние задания: ' \
               + str(self.get_average_rate()) + '\n' + 'Курсы в процессе изучения: ' + ', '.join(
            self.courses_in_progress) + '\n' \
               + 'Завершенные курсы: ' + ', '.join(self.finished_courses)

    def __gt__(self, other):
        return self.get_average_rate() > other.get_average_rate()

    def __lt__(self, other):
        return self.get_average_rate() < other.get_average_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def get_average_rate(self):
        if len(self.lecture_grades.items()) == 0:
            return 0
        else:
            sum_of_rates = 0
            amount_of_rates = 0
            for course, rate in self.lecture_grades.items():
                sum_of_rates += sum(rate)
                amount_of_rates += len(rate)
            return sum_of_rates / amount_of_rates

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за лекции: ' \
               + str(self.get_average_rate())

    def __gt__(self, other):
        return self.get_average_rate() > other.get_average_rate()

    def __lt__(self, other):
        return self.get_average_rate() < other.get_average_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname


def get_all_students_average_rate(student_list, course_name):
    sum_all_rates = 0
    amount_all_rates = 0
    for student in student_list:
        for course, rate in student.grades.items():
            if course == course_name:
                sum_all_rates += sum(rate)
                amount_all_rates += len(rate)
    if amount_all_rates != 0: return sum_all_rates / amount_all_rates
    return 0


def get_all_lecturers_average_rate(lecturers_list, course_name):
    sum_all_rates = 0
    amount_all_rates = 0
    for lecturer in lecturers_list:
        for course, rate in lecturer.lecture_grades.items():
            if course == course_name:
                sum_all_rates += sum(rate)
                amount_all_rates += len(rate)
    if amount_all_rates != 0: return sum_all_rates / amount_all_rates
    return 0


first_student = Student('Max', 'Ivanov', 'M')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['C++']
first_student.finished_courses += ['Java']

second_student = Student('Maria', 'Ivanova', 'F')
second_student.courses_in_progress += ['Java']
second_student.courses_in_progress += ['C#']
second_student.finished_courses += ['C++']

first_lecturer = Lecturer('Alex', 'Alexeev')
first_lecturer.courses_attached += ['Java']
first_lecturer.courses_attached += ['C#']

second_lecturer = Lecturer('Dan', 'Mishin')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['C++']

first_reviewer = Reviewer('Anastasia', 'Ydalova')
first_reviewer.courses_attached += ['Java']
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Sam', 'Marov')
second_reviewer.courses_attached += ['C#']
second_reviewer.courses_attached += ['C++']

first_student.rate_lector(second_lecturer, 'Python', 10)
first_student.rate_lector(second_lecturer, 'Python', 7)
first_student.rate_lector(second_lecturer, 'C++', 9)
first_student.rate_lector(second_lecturer, 'C++', 4)

second_student.rate_lector(first_lecturer, 'Java', 6)
second_student.rate_lector(first_lecturer, 'C#', 10)
second_student.rate_lector(first_lecturer, 'C#', 9)
second_student.rate_lector(first_lecturer, 'Java', 7)

first_reviewer.rate_hw(second_student, 'Java', 9)
first_reviewer.rate_hw(second_student, 'Java', 10)
first_reviewer.rate_hw(first_student, 'Python', 4)
first_reviewer.rate_hw(first_student, 'Python', 5)

second_reviewer.rate_hw(second_student, 'C#', 9)
second_reviewer.rate_hw(second_student, 'C#', 10)
second_reviewer.rate_hw(first_student, 'C++', 4)
second_reviewer.rate_hw(first_student, 'C++', 5)

print("Студент 1:")
print(first_student)

print('----------------------------------')

print("Студент 2:")
print(second_student)

print('----------------------------------')

print("Лектор 1:")
print(first_lecturer)

print('----------------------------------')

print("Лектор 2:")
print(second_lecturer)

print('----------------------------------')

print("Ревьювер 1:")
print(first_reviewer)

print('----------------------------------')

print("Ревьювер 2:")
print(second_reviewer)

print('----------------------------------')
print(first_student > second_student)
print(first_lecturer > second_lecturer)

print('----------------------------------')

print(first_student < second_student)
print(first_lecturer < second_lecturer)

print('----------------------------------')

print('Средняя оценка по курсу Python для 1 и 2 студента: ' +
      str(get_all_students_average_rate([first_student, second_student], 'Python')))

print('----------------------------------')

print('Средняя оценка лекторов по курсу Python: ' +
      str(get_all_lecturers_average_rate([first_lecturer, second_lecturer], 'Python')))

print('----------------------------------')

print('Средняя оценка лекторов по курсу C++: ' +
      str(get_all_lecturers_average_rate([first_lecturer, second_lecturer], 'C++')))
