class Student_Base:
    def input(self):
        self.name = input("enter student name: ")
        self.rollno = input("enter roll number: ")
        self.department = input("enter department: ")

class Student(Student_Base):
    def display(self):
        print("Student Information:")
        print("name:", self.name)
        print("roll no:", self.rollno)
        print("department:", self.department)

s = Student()
s.input()
s.display()