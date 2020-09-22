class Employee:

    # receive Instance as first argument: self is the instance e.g. emp_1.first = "Corey"
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # Class method that displays full name
    def fullname(self):
        return f"{self.first}.{self.last}@company.com"


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# Equivalent!
print(emp_1.fullname())
print(Employee.fullname(emp_1))  # emp1 gets passed in as self
