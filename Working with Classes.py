
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

emp_1 = Employee('Sangram', 'Bahadur', 20000000)
emp_2 = Employee('Vansh', 'Bahadur', 20000000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)
# for accessing the all details of emp_1
print(emp_1.__dict__)# it will return all values in the form of dictionary
# if I want to get all details of all employee then
print(Employee.__dict__)
# we can give manually amount
Employee.raise_amount = 2.05# instead of Employee we can give specific employe name
print(Employee.raise_amount)
emp_2.raise_amount = 3.00
print(emp_2.raise_amount)
print(Employee.num_of_emps)