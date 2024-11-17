class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class PermanentEmployee(Employee):
    def __init__(self, name, id,salary):
        self.salary = salary
        super().__init__(name, id)
    def calculate_salary(self):
        return self.salary
class ContractEmployee(Employee):
    def __init__(self, name, id,perHour,workHour):
        self.rate = perHour
        self.hour = workHour
        super().__init__(name, id)
    def calculate_salary(self):
        return self.rate*self.hour
P_employee = PermanentEmployee("Enamul","1946",12000)
print(P_employee.calculate_salary())

e2 = ContractEmployee("Employee 2","15454",60,12)
print(e2.calculate_salary())