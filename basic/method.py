# Create Class
# Supper Class
class Employee:
    # class variable or global variable
    _minSalary = 12000
    _maxSalary = 50000
    __companyName = "ABC Inc."

    def __init__(self, name, salary, departmentName):
        # instance variable
        self._name = name         #Public
        self.__salary = salary      #Private
        self.__department = departmentName

    def __del__(self):
       pass
    
    def _showDetail(self):
        print("DEPARTMENT : {} ".format(self.__department))
        print("NAME: {}".format(self._name))
        print("SALARY: {}".format(self.__salary))
        print("YEAR SALARY: {}".format(self._getIncome()))
    
    def _getIncome(self):
        return self.__salary*12

    def __str__(self):
        return ("DEPARTMENT: {}, NAME: {}, SALARY: {}, YEAR SALARY: {}".format(self.__department, self._name, self.__salary, self._getIncome()))

# Sub Class
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        print("-------------------")

class Programmer(Employee):
    __departmentName = "Programmer"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        print("-------------------")


class Sale(Employee):
    __departmentName = "Sale Engineer"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        print("-------------------")

# Create Object 
account1 = Accounting("Kanjanapa", 30000)
print(account1.__str__())
programmer1 = Programmer("Pongsiri", 20000)
print(programmer1.__str__())
