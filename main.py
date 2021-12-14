

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


    def _average_grad(self):
        result = []
        for grad in self.grades.values():
            result += grad
        aver_grad = sum(result) / len(result)
        return aver_grad

    def __str__(self):
        res = f'Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за домашнее задание{self._average_grad()}\n ' \
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
        result = []
        for grad in self.grades.values():
            result += grad
        aver_grad = sum(result) / len(result)
        return aver_grad


    def __str__(self):
            res = f'Имя:{self.name}\n Фамилия:{self.surname}\n Средняя оценка за лекции: {self._average_grad()} '
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
            return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor_r = Reviewer('Some', 'Buddy')
cool_mentor_r.courses_attached += ['Python']

cool_mentor_r.rate_hw(best_student, 'Python', 10)
cool_mentor_r.rate_hw(best_student, 'Python', 10)
cool_mentor_r.rate_hw(best_student, 'Python', 10)

print(best_student)
print(cool_mentor_r)
# print(best_student.grades)

cool_mentor_l = Lecturer('Nik', 'Rubby')
cool_mentor_l.courses_attached += ['Python']

best_student.rate_lc(cool_mentor_l, 'Python', 8)
best_student.rate_lc(cool_mentor_l, 'Python', 8)
best_student.rate_lc(cool_mentor_l, 'Python', 8)

print(cool_mentor_l)

# print(cool_mentor.grades)


