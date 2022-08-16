
from calendar import weekday


class Employee():
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emps +=1 
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)# we also use "self instead of Employee here"
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def form_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        Employee(first, last, pay)
        cls(first, last, pay)


    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
emp_1 = Employee('Sangram', 'Bahadur', 20000000)
emp_2 = Employee('Vansh', 'Bahadur', 20000000)

import datetime

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workingday(my_date))# it will return True or False based on day.

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'stive-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
new_emp_1 = Employee.form_string(emp_str_1)
#print(new_emp_1.email)
#print(new_emp_1.pay)

# first, last, pay = emp_str_1.split('-')

# emp_1.set_raise_amt(1.08)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)