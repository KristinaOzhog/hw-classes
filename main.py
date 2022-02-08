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

    def __average_hw_grade(self):
        ahwg = sum(self.grades) / len(self.grades)
        return ahwg

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за домашнее задание: {self.__average_hw_grade}\n'\
              f'Курсы в процессе изуения: {self.courses_in_progress}\n'\
              f'Завершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student.')
            return
        return self.__average_hw_grade < other.__average_hw_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __average_lecture_grade(self):
        alg = sum(self.grades) / len(self.grades)
        return alg

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за лекции: {self.__average_lecture_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer.')
            return
        return self.__average_lecture_grade < other.__average_lecture_grade

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}'
        return res

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']


first_lecturer = Lecturer('Николай', 'Прокофьев')
first_lecturer.courses_attached.append('Python')

second_lecturer = Lecturer('Юлия', 'Царева')
second_lecturer.courses_attached.append('Java')

first_student = Student('Алексей', 'Федотов', 'м')
first_student.finished_courses.append('Git')
first_student.courses_in_progress.append('Python')
first_student.courses_in_progress.append('Java')
first_student.rate_lr(first_lecturer, 'Python', 10)
first_student.rate_lr(second_lecturer, 'Java', 6)

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
second_reviewer.rate_hw(first_student, 'Git', 8)
second_reviewer.rate_hw(first_student, 'Java', 9)
second_reviewer.rate_hw(second_student, 'Git', 10)
second_reviewer.rate_hw(second_student, 'Java', 8)



print(second_lecturer)