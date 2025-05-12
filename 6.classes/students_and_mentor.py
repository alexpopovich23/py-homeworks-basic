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

#Студенты
student1 = Student('Мария', 'Петрова', 'женский')
student1.courses_in_progress += ['Python']

student2 = Student('Сергей', 'Сергеев', 'мужской')
student2.courses_in_progress += ['Python']

 #Лектора
lecturer1 = Lecturer('Елена', 'Еленина')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Дмитрий', 'Дмитриев')
lecturer2.courses_attached += ['Python']

# Рецензенты
reviewer1 = Reviewer('Ольга', 'Ольгина')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Андрей', 'Андреев')
reviewer2.courses_attached += ['Python']


reviewer1.rate_student(student1, 'Python', 8)
reviewer1.rate_student(student1, 'Python', 9)
reviewer1.rate_student(student2, 'Python', 7)
reviewer1.rate_student(student2, 'Python', 6)

reviewer2.rate_student(student1, 'Python', 10)
reviewer2.rate_student(student2, 'Python', 9)


student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Python', 8)

student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 7)


def average_student_grade(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    return total_grades / total_students if total_students > 0 else 0


def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    return total_grades / total_lecturers if total_lecturers > 0 else 0

students_list = [best_student, student1, student2]
lecturers_list = [cool_lecturer, lecturer1, lecturer2]


print(f'Средняя оценка студентов по курсу Python: {average_student_grade(students_list, "Python"):.1f}')
print(f'Средняя оценка лекторов по курсу Python: {average_lecturer_grade(lecturers_list, "Python"):.1f}')
