class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):        
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания: {self.__avg_grade():.2f} \n"
                f"Курсы в процессе изучения:{self.courses_in_progress} \n"
                f"Завершенные курсы: {self.finished_courses}") 
                  
    
    def __avg_grade(self):
        list_grades =[]
        for value in self.grades.values():
            for  v  in   value:
                list_grades.append(v)
        return sum(list_grades) / len(list_grades)
    

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

    def __lt__(self, other):
        if self.__avg_grade() < other.__avg_grade():
            return f"Средний балл за ДЗ больше y студента: {other.name} {other.surname}"
        else:
            return f"Средний балл за ДЗ больше y студента: {self.name} {self.surname}" 

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 

    def __str__(self):        
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за лекции: {self.__avg_grade():.2f}")   
    
    def __avg_grade(self):
        list_grades =[]
        for value in self.grades.values():
            for  v  in   value:
                list_grades.append(v)
        return sum(list_grades) / len(list_grades)
    
    def __lt__(self, other):
        if self.__avg_grade() < other.__avg_grade():
            return f"Средний балл за лекции больше y лектора: {other.name} {other.surname}"
        else:
            return f"Средний балл за лекции больше y лектора: {self.name} {self.surname}"


        
class Reviewer(Mentor):
    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def avg_grade_hw(list_students, course):
    avg_grades = []
    for student in list_students:  
        all_grades = 0  
        for grades in student.grades[course]:
            all_grades += (grades / len(student.grades[course])) 
        avg_grades.append(all_grades) 
    # return sum(avg_grades) / len(list_students)
    print(f"Средняя оценка за домашние задания всех студентов: {sum(avg_grades) / len(list_students):.2f}")   

def avg_grade_lecturers(list_lecturers, course):
    avg_grades = []
    for lecturer in list_lecturers:  
        all_grades = 0         
        for grades in lecturer.grades[course]:                     
            all_grades += (grades / len(lecturer.grades[course]))            
        avg_grades.append(all_grades)    
    # return sum(avg_grades) / len(list_lecturers)
    print(f"Средняя оценка за лекции всех лекторов: {sum(avg_grades) / len(list_lecturers):.2f}")
   


#class Student
new_student = Student('Jane', 'Eyre', 'female')
new_student.courses_in_progress += ['Python']
new_student.add_courses('Git')
new_student.grades['Git'] = [7, 5, 9]
new_student.add_courses('Введение в программирование')
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.grades['Git'] = [10, 10, 9, 10]
best_student.courses_in_progress += ['Python', 'java']
best_student.grades['Python'] = [10, 4]

#class Lecturer
bed_lecturer = Lecturer('Jon', 'Jones')
bed_lecturer.courses_attached += ['Git', 'java', 'Python']
good_lecturer = Lecturer('Donald', 'Trump')
good_lecturer.courses_attached += ['Git', 'java', 'Python']

#class Reviewer
best_reviewer = Reviewer('Alex', 'Jones')
best_reviewer.courses_attached += ['Python']


# Testing of methods

# print(new_student)
# print(best_student)
# print(new_student > best_student)
best_student.rate_lecture(good_lecturer, 'Python', 7 )
best_student.rate_lecture(good_lecturer, 'java', 9)
best_student.rate_lecture(good_lecturer, 'Python', 10 )
best_student.rate_lecture(bed_lecturer, 'Git', 7)
best_student.rate_lecture(bed_lecturer, 'java', 4)
best_student.rate_lecture(bed_lecturer, 'Python', 3)
best_student.rate_lecture(bed_lecturer, 'java', 4)
best_student.rate_lecture(bed_lecturer, 'Python', 3)

# print(good_lecturer)
# print(bed_lecturer)
# print(bed_lecturer > good_lecturer)


# print(best_reviewer)
# print(best_reviewer.name, best_reviewer.surname, best_reviewer.courses_attached)
best_reviewer.rate_hw(new_student, 'Python', 6)
# print(new_student)
list_students = [new_student, best_student]
print(new_student.grades['Git'])
print(best_student.grades['Git'])
avg_grade_hw(list_students, 'Git')

list_lecturers = [bed_lecturer, good_lecturer]
# print(bed_lecturer.grades['Python'])
# print(good_lecturer.grades['Python'])
# avg_grade_lecturers(list_lecturers, 'Python')