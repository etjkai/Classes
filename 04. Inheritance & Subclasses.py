class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first}.{self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    # Method Resolution Order - if does not find __init__ when Developer instantiated, walk up chain of inheritance to find what it's looking for

    # Changes to subclass without affecting Parent
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # Let Parent Class handle first, last, pay
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("->>", emp.fullname())


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# print(mgr_1.email)

# # Show current employees
# mgr_1.print_emps()

# # Add Employees
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# # Add then remove Employees
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# # Inheriting email from Parent class
# print(dev_1.email)
# print(dev_1.prog_lang)

# # Uses Developer Class raise_amt variable
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# isinstance() - shows if Object is instance of a class
# print(isinstance(mgr_1, Developer)) -> False
# print(isinstance(mgr_1, Manager)) -> True

# issubclass() - shows if Class is Subclass of another
# print(issubclass(Developer, Employee)) -> True
# print(issubclass(Manager, Developer)) -> False
