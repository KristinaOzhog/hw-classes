class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lr(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw_grade(self):
        sg = sum(list(self.grades.values()), [])
        ahwg = round(sum(sg) / len(sg), 1)
        return ahwg

    def __str__(self):
        str1 = ", ".join(self.courses_in_progress)
        str2 = ", ".join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_hw_grade()}\n' \
              f'Курсы в процессе изуения: {str1}\n' \
              f'Завершенные курсы: {str2}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student.')
            return
        return self.average_hw_grade() < other.average_hw_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_lecture_grade(self):
        sl = sum(list(self.grades.values()), [])
        alg = round(sum(sl) / len(sl), 1)
        return alg

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_lecture_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer.')
            return
        return self.average_lecture_grade() < other.average_lecture_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in \
                student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


first_lecturer = Lecturer('Николай', 'Прокофьев')
first_lecturer.courses_attached.append('Python')

second_lecturer = Lecturer('Юлия', 'Царева')
second_lecturer.courses_attached.append('Java')

first_student = Student('Алексей', 'Федотов', 'м')
first_student.finished_courses.append('Git')
first_student.courses_in_progress.append('Python')
first_student.courses_in_progress.append('Java')
first_student.rate_lr(first_lecturer, 'Python', 9)
first_student.rate_lr(second_lecturer, 'Java', 10)

second_student = Student('Михаил', 'Павлов', 'м')
second_student.finished_courses.append('Java')
second_student.courses_in_progress.append('Git')
second_student.courses_in_progress.append('Python')
second_student.rate_lr(first_lecturer, 'Python', 8)
second_student.rate_lr(second_lecturer, 'Java', 10)

first_reviewer = Reviewer('Анна', 'Полякова')
first_reviewer.courses_attached.append('Python')
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 9)

second_reviewer = Reviewer('Олег', 'Михайлов')
second_reviewer.courses_attached.append('Git')
second_reviewer.courses_attached.append('Java')
second_reviewer.rate_hw(first_student, 'Java', 8)
second_reviewer.rate_hw(first_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Git', 10)
second_reviewer.rate_hw(second_student, 'Git', 10)

print(first_student)
print(second_student)
print(first_student > second_student)
print(first_student < second_student)

print(first_reviewer)
print(second_reviewer)

print(first_lecturer)
print(second_lecturer)
print(first_lecturer > second_lecturer)
print(first_lecturer < second_lecturer)

student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]


def av_students_grades(students, courses):
    for student in students:
        if courses in student.grades.keys():
            sg = sum(list(student.grades.values()), [])
            ahwg = round(sum(sg) / len(sg), 1)
            return ahwg
    else:
        print('Студент не изучает данный курс.')


def av_lecturer_grades(lecturers, courses):
    for lecturer in lecturers:
        if courses in lecturer.grades.keys():
            sl = sum(list(lecturer.grades.values()), [])
            alg = round(sum(sl) / len(sl), 1)
            return alg
    else:
        print('Лектор не преподает данный курс.')


print(f'Средняя оценка студентов за курс GIT: {av_students_grades(student_list, "Git")}')
print(f'Средняя оценка студентов за курс Python: {av_students_grades(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {av_lecturer_grades(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {av_lecturer_grades(lecturer_list, "Java")}')
