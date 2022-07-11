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
member2 = Employee("Kanjanapa", 30000)

# Check
print(isinstance(member1, Employee)) # member1 คือ obj ของ class Employee หรือไม่ ถ้าใช่ return true
print(dir(member1)) # check ว่า object มี attribute อะไรบ้าง
print(member1.__class__) # Check ว่า member1 มาจาก class อะไร