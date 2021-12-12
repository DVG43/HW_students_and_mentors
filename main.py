

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student.rate_lc(cool_mentor, 'Python', 8)
best_student.rate_lc(cool_mentor, 'Python', 8)
best_student.rate_lc(cool_mentor, 'Python', 8)

print(cool_mentor.grades)


# мы     реализовали    возможность    выставлять    студентам    оценки    за    домашние    задания.Теперь    это
# могут    делать    только    Reviewer(реализуйте    такой    метод)! А    что    могут    делать    лекторы? Получать
# оценки    за    лекции    от    студентов:) Реализуйте    метод    выставления    оценок    лекторам    у    класса
# Student(оценки    по    10 - балльной    шкале, хранятся    в    атрибуте - словаре    у    Lecturer, в    котором
# ключи – названия    курсов, а    значения – списки    оценок).Лектор    при    этом    должен    быть    закреплен
# за    тем    курсом, на    который    записан    студент.