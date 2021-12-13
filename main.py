

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


    def average_grad(self):
        step = 0
        result = 0
        for grad in self.grades.values():
            aver = sum(grad) / len(grad)
            step += 1
            result += aver
        aver_grap = result / step

    def __str__(self):
        res = f'Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за домашнее задание{self.average_grad()}\n ' \
              f'Курсы в процессе изучения:{self.courses_in_progress}\n Завершенные курсы:{self.finished_courses} '
        return res


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


    def _average_grad(self):
        result = 0
        step = 0
        for grad in self.grades.values():
            aver = sum(grad)/len(grad)
            step += 1
            result += aver
        aver_grap = result / step

    def __str__(self):
            res = f'Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за лекции: {_average_grad()} '
            return res

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

    def __str__(self):
            res = f'Имя:{self.name}\n Фамилия:{self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student)
print(cool_mentor)
# print(best_student.grades)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student.rate_lc(cool_mentor, 'Python', 8)
best_student.rate_lc(cool_mentor, 'Python', 8)
best_student.rate_lc(cool_mentor, 'Python', 8)

print(best_student)
print(cool_mentor)

# print(cool_mentor.grades)


