# Create Class
from socket import getnameinfo


class Employee:
    # Create method
    def __init__(self, name, salary):
        self.__name = name        #Public
        self.__salary = salary  #Private

    def __del__(self):
       pass
    
    # Protected
    def __showDetail(self):
        print("NAME: {}".format(self.__name))
        print("SALARY: {}".format(self.__salary))

    # Setter method 
    def setName(self, newName):
        self.__name = newName
    def setSalary(self, newSalary):
        self.__salary = newSalary

    # Getter method
    def getName(self):
        return self.__name

# Create Object 
member1 = Employee("Pongsiri", 20000)
member1.__salary = 4000000      # ไม่สามารถเปลี่ยนค่า salary ได้ เนื่องจาก เป็นแบบ pirvate แต่สามารถ run code ผ่าน
member1.setName("IRON MAN")  
member1.setSalary(400000000)
#member1.__showDetail()           
name  = print(member1.getName())
