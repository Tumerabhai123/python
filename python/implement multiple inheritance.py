class Skills_adapted:
    def skills(self):
        print("Skills: Python, DSA")

class Salary_got:
    def salary(self):
        print("Salary: 5000 per month")

class Employee(Skills_adapted, Salary_got):
    def details_show(self):
        print("Employee details:")

s = Employee()


s.details_show() 
s.skills()       
s.salary()       