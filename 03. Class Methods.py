import datetime


class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    # [A] Regular methods take in Instance (self) as first argument
    def fullname(self):
        return f"{self.first}.{self.last}@company.com"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # [B] Class method - takes in class as first argument
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # Using Class methods as alternative constructor (for the object)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # Use cls variable, instead of Employee
        return cls(first, last, pay)

    # [C] Static methods - do not pass cls (class) / self (instance)
    # Included in class due to logical connections with class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Using the Class method - set Class variable
Employee.set_raise_amt(1.05)
# equivalent to Employee.raise_amt = 1.05

emp_str_1 = "John-Doe-700000"
new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

my_date = datetime.date(2020, 9, 21)
# print(Employee.is_workday(my_date))
