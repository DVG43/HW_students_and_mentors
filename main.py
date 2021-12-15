

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
              f'Курсы в процессе изучения:{" ".join(self.courses_in_progress)}\n ' \
              f'Завершенные курсы:{" ".join(self.finished_courses)} '
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

 # Функция котораЯ возвращает среднюю оценку за определенный курс

def student_total_avereg_grad (stud_list, name_curs):
    if name_curs in list_of_curs:
         summa = 0
         step = 1
         for stud in stud_list:
            summa += stud._average_grad()
            step += 1
         print (f'Средняя оценка студентов за курс {name_curs}: {summa / step}')

    else: print ('Такой курс отсутсвует в учебной программе')

def mentor_total_avereg_grad (ment_list, name_curs):
    if name_curs in list_of_curs:
         summa = 0
         step = 1
         for mentor_a in ment_list:
            summa += mentor_a._average_grad()
            step += 1
         print (f'Средняя оценка менторов за курс {name_curs}: {summa / step}')

    else: print ('Такой курс отсутсвует в учебной программе')


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor_r = Reviewer('Some', 'Buddy')
# cool_mentor_r.courses_attached += ['Python']
#
# cool_mentor_r.rate_hw(best_student, 'Python', 10)
# cool_mentor_r.rate_hw(best_student, 'Python', 10)
# cool_mentor_r.rate_hw(best_student, 'Python', 10)
#
# print(best_student)
# print(cool_mentor_r)
#
#
# cool_mentor_l = Lecturer('Nik', 'Rubby')
# cool_mentor_l.courses_attached += ['Python']
#
# best_student.rate_lc(cool_mentor_l, 'Python', 8)
# best_student.rate_lc(cool_mentor_l, 'Python', 8)
# best_student.rate_lc(cool_mentor_l, 'Python', 8)
#
# print(cool_mentor_l)
#
# MENTORS Reviewer

list_of_curs = ['Python', 'Java']

a_mentor_r = Reviewer('Petr', 'Ivanov')
a_mentor_r.courses_attached += ['Python']

b_mentor_r = Reviewer('Ivan', 'Petrov')
b_mentor_r.courses_attached += ['Python']

c_mentor_r = Reviewer('Pavel', 'Sidorov')
c_mentor_r.courses_attached += ['Python']

d_mentor_r = Reviewer('Savelii', 'Morozov')
d_mentor_r.courses_attached += ['Python']

# Students
student_list = []
mentor_list = []

a_student = Student('Vasia', 'Kirilov', 'mail')
a_student.courses_in_progress += ['Python']
a_mentor_r.rate_hw(a_student, 'Python', 9)
b_mentor_r.rate_hw(a_student, 'Python', 10)
c_mentor_r.rate_hw(a_student, 'Python', 8)
d_mentor_r.rate_hw(a_student, 'Python', 7)
student_list.append(a_student)


b_student = Student('Vitalii', 'Borzov', 'mail')
b_student.courses_in_progress += ['Python']
a_mentor_r.rate_hw(b_student, 'Python', 7)
b_mentor_r.rate_hw(b_student, 'Python', 9)
c_mentor_r.rate_hw(b_student, 'Python', 6)
d_mentor_r.rate_hw(b_student, 'Python', 10)
student_list.append(b_student)

c_student = Student('Vasia', 'Kirilov', 'mail')
c_student.courses_in_progress += ['Python']
a_mentor_r.rate_hw(c_student, 'Python', 8)
b_mentor_r.rate_hw(c_student, 'Python', 9)
c_mentor_r.rate_hw(c_student, 'Python', 10)
d_mentor_r.rate_hw(c_student, 'Python', 9)
student_list.append(c_student)

d_student = Student('Boriy', 'Gukov', 'mail')
d_student.courses_in_progress += ['Python']
a_mentor_r.rate_hw(d_student, 'Python', 9)
b_mentor_r.rate_hw(d_student, 'Python', 10)
c_mentor_r.rate_hw(d_student, 'Python', 10)
d_mentor_r.rate_hw(d_student, 'Python', 9)
student_list.append(d_student)

# MENTORS Lecturer

a_mentor_l = Lecturer('Mik', 'Vuddy')
a_mentor_l.courses_attached += ['Python']
a_student.rate_lc(a_mentor_l, 'Python', 8)
b_student.rate_lc(a_mentor_l, 'Python', 7)
c_student.rate_lc(a_mentor_l, 'Python', 6)
d_student.rate_lc(a_mentor_l, 'Python', 9)
mentor_list.append(a_mentor_l)

b_mentor_l = Lecturer('Nik', 'Harry')
b_mentor_l.courses_attached += ['Python']
a_student.rate_lc(b_mentor_l, 'Python', 9)
b_student.rate_lc(b_mentor_l, 'Python', 10)
c_student.rate_lc(b_mentor_l, 'Python', 7)
d_student.rate_lc(b_mentor_l, 'Python', 6)
mentor_list.append(b_mentor_l)

c_mentor_l = Lecturer('Bob', 'Fany')
c_mentor_l.courses_attached += ['Python']
a_student.rate_lc(c_mentor_l, 'Python', 8)
b_student.rate_lc(c_mentor_l, 'Python', 6)
c_student.rate_lc(c_mentor_l, 'Python', 9)
d_student.rate_lc(c_mentor_l, 'Python', 10)
mentor_list.append(c_mentor_l)

d_mentor_l = Lecturer('Luis', 'Sandy')
d_mentor_l.courses_attached += ['Python']
a_student.rate_lc(d_mentor_l, 'Python', 7)
b_student.rate_lc(d_mentor_l, 'Python', 9)
c_student.rate_lc(d_mentor_l, 'Python', 8)
d_student.rate_lc(d_mentor_l, 'Python', 9)
mentor_list.append(d_mentor_l)

# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).

name_curs = input('Введите курс')
student_total_avereg_grad (student_list, name_curs)
mentor_total_avereg_grad (mentor_list, name_curs)
print (a_mentor_r)

