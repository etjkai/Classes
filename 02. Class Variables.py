class Employee:

    # Class Variables - Shared across all instances of the class
    raise_amount = 1.04
    num_of_emps = 0

    # receive Instance as first argument: self is the instance e.g. emp_1.first = "Corey"
    # Instance Variables - set for each instance
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1  # Using Class variable as logical

    # Class method to display full name

    def fullname(self):
        return f"{self.first}.{self.last}@company.com"

    def apply_raise(self):
        # Access class variable thorugh Class / Instance of class
        # self.pay = int(self.pay * Employee.raise_amount)
        # Uses specific instance's varable - allows for overriding
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# Equivalent!
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))  [# Instance (emp1) gets passed in as self]

# Attempts to access Class variable from Instance, and then Class (as a fallback)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(Employee.__dict__)

# Overwrite class variables - changing raise_amount for an Instance
# raise_amount added to emp_1 namespace
# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(emp_1.__dict__)

print(Employee.num_of_emps)
print(emp_1.num_of_emps)
