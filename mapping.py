class Course:
    def __init__(self, course):
        self.course = course
        self.students = []
        self.check = False

    def getstudents(self):
        return self.students

    def enrollstudent(self, student):
        self.students.append(student)
        self.check = True
        return self.students

    def removestudent(self, student):
        if student in self.students:
            self.check = True
            self.students.remove(student)
            return self.students
        else:
            print(f"{student} is not enrolled in {self.course}.")
            self.check = False

course = Course("Cs3")

class Student:
    def __init__(self, student, course):
        self.name = student
        self.course = course

    def enroll(self):
        self.course.enrollstudent(self.name)
        print(f"{self.name} has been enrolled in {self.course.course}.")
        print(f"Current students in {self.course.course}: {self.course.students}\n")

    def drop(self):
        self.course.removestudent(self.name)
        if self.course.check == False:
            students = self.course.getstudents()
            print(f"Current students in {self.course.course}: {students}\n")
        else:
            print(f"{self.name} has dropped {self.course.course}.")
            print(f"Current students in {self.course.course}: {self.course.students}\"\n")

student1 = Student("Abrenica", course)
student2 = Student("Myke", course)
student3 = Student("Gabriel", course)


student1.enroll()
student2.enroll()
student3.enroll()
student1.drop()
student1.drop()
