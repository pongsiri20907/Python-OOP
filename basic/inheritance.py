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
    
    # Protected
    def _showDetail(self):
        print("DEPARTMENT : {} ".format(self.__department))
        print("NAME : {}".format(self._name))
        print("SALARY: {}".format(self.__salary))

# Sub Class
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showDetail()
        print("-------------------")

class Programmer(Employee):
    __departmentName = "Programmer"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showDetail()
        print("-------------------")


class Sale(Employee):
    __departmentName = "Sale Engineer"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showDetail()
        print("-------------------")

# Create Object 
account1 = Accounting("Kanjanapa", 30000)
programmer1 = Programmer("Pongsiri", 20000)

