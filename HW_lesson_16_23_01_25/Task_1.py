# Task_1
# Class structure that will represent people in the school.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def greet(self):
        return f"Hello, my name is {self.name}."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        return f"Enrolled in course: {course}"

    def get_courses(self):
        return self.courses

    def get_details(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Student ID: {self.student_id}, "
                f"Courses: {', '.join(self.courses)}")


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.subjects = []

    def assign_subject(self, subject):
        self.subjects.append(subject)
        return f"Assigned to teach: {subject}"

    def get_subjects(self):
        return self.subjects

    def get_details(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Salary: {self.salary}, Subjects: {', '.join(self.subjects)}")


if __name__ == "__main__":
    student = Student("John Doe", 20, "S543")
    teacher = Teacher("Jane Smith", 35, 51000)

    student.enroll_course("Mathematics")
    student.enroll_course("Science")
    print(student.get_details())

    teacher.assign_subject("Physics")
    teacher.assign_subject("Chemistry")
    print(teacher.get_details())
