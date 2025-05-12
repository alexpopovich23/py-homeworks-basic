
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка: Лектор не прикреплен к курсу или студент не записан на курс.'

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')



best_student = Student('Иван', 'Иванов', 'мужской')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Кирилл', 'Кириллов')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Александра', 'Александрова')
cool_reviewer.courses_attached += ['Python']


cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 9)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)


best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)


print(f'Оценки студента {best_student.name} {best_student.surname}: {best_student.grades}')
print(f'Оценки лектора {cool_lecturer.name} {cool_lecturer.surname}: {cool_lecturer.grades}')


print(best_student)
print(cool_lecturer)
print(cool_reviewer)


another_lecturer = Lecturer('Алексей', 'Алексеев')
another_lecturer.courses_attached += ['Python']
best_student.rate_lecturer(another_lecturer, 'Python', 8)


print(cool_lecturer > another_lecturer)   # на больше
print(cool_lecturer >= another_lecturer)  # на больше или равно
print(cool_lecturer == another_lecturer)  # на равенство
print(cool_lecturer != another_lecturer)  # на неравенство
print(cool_lecturer < another_lecturer)   # на меньше
print(cool_lecturer <= another_lecturer)  # на меньше или равно
