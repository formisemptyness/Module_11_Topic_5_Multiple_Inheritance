'''
Program: multiple_inheritance.py
Author: Joshua M. McGinley
Last date modified: 11/09/2022

A manager is a Person and Employeemultiple inheritance UML for assignment
Write a class Manager that inherits from Person and Employee.

    Add attribute department
    Add list direct_reports of type Employee that report to the manager

Include a driver that

    Creates a Manager object (select a meaningful name) with your name, start date today, starting salary $40,000
    Displays the Manager object
    Creates at least 3 direct_reports of type Employee that report to Manager
    Displays the Manager object's direct_reports including Employee object name, start_date, salary
    Change salary to $42,000
    Displays the Manager object
'''

class Person:
    """Person class"""
    def __init__(self, lname, fname, addy, phnumber):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phnumber

    def display(self):
        return self.last_name + ", " + self.first_name

class Employee:
    def __init__(self, s_date, sal):
        self.start_date = s_date
        self.salary = sal

    def give_raise(self, new_sal):
        self.salary = new_sal

    def display(self):
        return self.last_name + ", " + self.first_name

class Manager(Person, Employee):
    def __init__(self, last_name, first_name, start_date, dept='', salary=40000, d_reports = []):
        super().__init__(last_name, first_name) #start_date) #salary)
        self.department = dept
        self.direct_reports = d_reports

    def give_raise(self, new_sal):
        self.salary = new_sal

    def display(self):
        return self.last_name + ", " + self.first_name


man = Manager('McGinley', 'Joshua', '11-9-2022',)
print(man.display())

#Code is not working... Will revise


