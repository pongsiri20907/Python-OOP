# Create Class
class Employee:
    # Create method
    def __init__(self, name, salary):
        print("default constructor")
        self.name = name
        self.salary = salary
        print("Created new member ...")

    def __del__(self):
        print("Call destructor")
    
    def showDetail(self):
        print("NAME: {}".format(self.name))
        print("SALARY: {}".format(self.salary))
 
# Create Object 
member1 = Employee("Pongsiri", 20000)
member1.showDetail()
 
member2 = Employee("Kanjanapa", 30000)
member2.showDetail()

