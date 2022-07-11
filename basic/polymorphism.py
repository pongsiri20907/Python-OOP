# Create Class
# Overloading
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
        print("DEPARTMENT: {}".format(self.__department))
        print("NAME: {}".format(self._name))
        print("SALARY: {}".format(self.__salary))

    def _getIncome(self):
        return self.__salary*12

    def _getIncome(self, bonus=0):
        return (self.__salary*12)+bonus

    # def __str__(self):
    #     return ("DEPARTMENT: {}, NAME: {}, SALARY: {}, YEAR SALARY: {}".format(self.__department, self._name, self.__salary, self._getIncome()))

# Sub Class
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.age = age
    
    def _showDetail(self):
        super()._showDetail()
        print("AGE: {}".format(self.age))
        print("YEAR SALARY: {}".format(self._getIncome(200)))
        print("-------------------------------")
    
class Programmer(Employee):
    __departmentName = "Programmer"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.exp = experience
        self.skill = skill
    
    def _showDetail(self):
        super()._showDetail()
        print("EXPERINCE: {}".format(self.exp))
        print("SKILL: {}".format(self.skill))
        print("YEAR SALARY: {}".format(self._getIncome(5000)))
        print("-------------------------------")

class Sale(Employee):
    __departmentName = "Sale Engineer"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area

    def _showDetail(self):
        super()._showDetail()
        print("AREA: {}".format(self.area))
        print("YEAR SALARY: {}".format(self._getIncome(3000)))
        print("-------------------------------")

# Create Object 
account1 = Accounting("Kanjanapa", 30000, 24)
account1._showDetail()
programmer1 = Programmer("Pongsiri", 20000, 1, "IIoT")
programmer1._showDetail()
