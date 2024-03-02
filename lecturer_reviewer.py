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

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
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
        self.grades = {}      

class Reviewer(Mentor):
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

            
# best_reviewer = Reviewer('Alex', 'Jones')
# best_reviewer.courses_attached += ['Python']
# print(best_reviewer.name, best_reviewer.surname, best_reviewer.courses_attached)

bed_lecturer = Lecturer('Jon', 'Jones')
bed_lecturer.courses_attached += ['Git', 'java', 'Python']
print(bed_lecturer.name, bed_lecturer.surname, bed_lecturer.courses_attached)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.grades['Git'] = [10, 10, 10, 10]
best_student.courses_in_progress += ['Python', 'java']
best_student.grades['Python'] = [10, 4]
# best_reviewer.rate_hw(best_student, 'Python', 6)
# print(best_student.grades)
best_student.rate_lecture(bed_lecturer, 'Git', 7)
best_student.rate_lecture(bed_lecturer, 'java', 7)
best_student.rate_lecture(bed_lecturer, 'Python', 3)
print(bed_lecturer.grades)

# print(Reviewer.mro())
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]

# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)