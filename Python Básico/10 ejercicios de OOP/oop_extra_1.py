"""Extra OOP exercise"""

class Employee:
    """class that represents an employee"""
    def __init__(self, name, salary):
        """initializing the methods and attributes of the employee class"""
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        """return the employee's name"""
        return self.__name

    @property
    def salary(self):
        "return the employee's salary"
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        """validate the salary"""
        if new_salary < 0:
            raise ValueError("The salary cannot be negative")

        self.__salary = new_salary

    def promote(self, percentage):
        """increase the percentage"""
        increase = self.__salary * percentage
        final_salary = self.__salary + increase
        self.__salary = final_salary
        return self.__salary

employee = Employee("Ana", 1000)
print(employee.promote(0.10))
print(employee.salary)
