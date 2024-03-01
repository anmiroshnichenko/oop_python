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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        # super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)   

            
best_reviewer = Lecturer('Alex', 'Jones')
best_reviewer.courses_attached += ['Python']
print(best_reviewer.name, best_reviewer.surname)
print(best_reviewer.courses_attached)



# print(Reviewer.mro())

bed_lecturer = Lecturer('Jon', 'Jones')
bed_lecturer.courses_attached += ['Git', 'java']
print(bed_lecturer.name)
print(bed_lecturer.surname)
print(bed_lecturer.courses_attached)



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.grades['Git'] = [10, 10, 10, 10]
best_student.courses_in_progress += ['Python', 'java']
best_student.grades['Python'] = [10, 10]
bed_lecturer.rate_hw(best_student, 'java', 3)
best_reviewer.rate_hw(best_student, 'Python', 2)
print(best_student.grades)

# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 11)
# cool_mentor.rate_hw(best_student, 'Python', 6)
# cool_mentor.rate_hw(best_student, 'Python', 1)
# print(cool_mentor.courses_attached)
# print(best_student.grades)