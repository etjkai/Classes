class Employee:

    raise_amt = 1.04

    # Special dunder method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # REPR - unambiguous representation of object for debugging / logging
    # Set a format that can be used to re-create the object
    # __str__ uses __repr__ as fallback
    def __repr__(self):
        return f"Employee('{self.first}' '{self.last}' {self.pay})"

    # STR - readable representation of object for display to end user
    # More arbitrary format: output for print(xx)
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def fullname(self):
        return f"{self.first}.{self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # allows for Employee + Employee
    def __add__(self, other):
        # Return combined pay .
        return self.pay + other.pay
        # emp_1.__add__(emp_2)
        # emp_1 + emp_2

    # to allow len() to work on Employee object
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 65000)


# print(repr(emp_1))  # Calling special method - emp_1.__repr__()
# print(str(emp_1))  # emp_1.__str__()


# # Dunder __add__
# print(1+2)
# # __add__ method for int
# print(int.__add__(1, 2))
# print(str.__add__("a", 'b'))

# # dunder add method added to class
# print(emp_1 + emp_2)

print(len('test'))  # Equivalent to print('test'.__len__())
print(len(emp_1))
