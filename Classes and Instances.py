# Python Object- Oriented Programming


class Employee():#class name is Employee
    def __init__(self, first, last, pay):# __init__ is a constructor here and self is first argument of this.
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = email
        self.email = first + '.' + last + '@gmail.com'

emp_1 = Employee('Anky', 'Dhurve', 1000000)# emp_1 is instance of class Employee
emp_2 = Employee('vashu', 'Dhurve', 2000000)# we have to pass arguments here.

# emp_1.first = "Sangram"# we are conecting here to the field "first".
# emp_1.last = "Bahadur"
# emp_1.email = "dh.sangram@gmail.com"
# emp_1.pay = 1000000# we are conecting here to the field "pay".

# emp_2.first = "Vansh"
# emp_2.last = "Bahadur"
# emp_2.email = "vanshdhurve83@gmail.com"
# emp_2.pay = 1100000

# print(emp_2.email)
# print(emp_1.email)
# print('{} {}'.format(emp_1.first, emp_1.last))
# print('{} {}'.format(emp_2.first, emp_2.last))

#PART------------------>2
class Employee():#class name is Employee
    def __init__(self, first, last, pay):# __init__ is a constructor here and self is first argument of this.
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = email
        self.email = first + '.' + last + '@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
emp_11 = Employee('papa', 'Dhurve', 1000000)
emp_12= Employee('jitu', 'Dhurve', 3000000)
# print(emp_12.fullname())
# print(emp_11.fullname())
print(Employee.fullname(emp_11))