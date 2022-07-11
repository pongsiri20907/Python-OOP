# Create Class

class Employee:
    # class variable or global variable
    _minSalary = 12000
    _maxSalary = 50000

    def __init__(self, name, salary):
        # instance variable
        self._name = name         #Public
        self.__salary = salary      #Private

    def __del__(self):
       pass
    
    # Protected
    def _showDetail(self):
        print("NAME: {}".format(self._name))
        print("SALARY: {}".format(self.__salary))

# Create Object 
member1 = Employee("Pongsiri", 20000)
member1._showDetail()    
# show minSalary โดยไม่ต้องสร้าง object 
print("The Salary is = " + str(Employee._minSalary))       

