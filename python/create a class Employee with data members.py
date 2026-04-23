class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def print_info(self):
        print(f"Employee name: {self.name}")
        print(f"    department: {self.department}")
        print(f"    salary: {self.salary}")

emp1 = Employee("Aarya Gaikwad", "CS", 75000)
emp1.print_info()