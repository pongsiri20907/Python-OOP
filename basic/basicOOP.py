# Create Class
class Employee:
    # Create method
    def detail(self, name, salary):
        self.name = name
        self.salary = salary
        print("Created new member ...")
    
    def showDetail(self):
        print("NAME: {}".format(self.name))
        print("SALARY: {}".format(self.salary))
 
# Create Object 
member1 = Employee()
member1.detail("Pongsii", 20000)
member1.showDetail()
 
member2 = Employee()
member2.detail("Kanjanapa", 30000) 
member2.showDetail()

