class User:
    __name = None
    __surname = None
    def setName(self, name):
        self.__name = name 
    
    def getName(self):
        return self.__name 
    
    def setSurn(self, surname):
        self.__surname = surname 
    
    def getSurn(self):
        return self.__surname 

class Employee(User):
    def getFull(self):
        return self.__name + ' ' + self.__surname 

employee = Employee()
employee.setName("John")
employee.setSurn("Doe")

print(employee.getName())
print(employee.getSurn())
print(employee.getFull())

        return f"{user_info}, Age: {self.get_age()}, Salary: {self.get_salary()}"

employee = Employee("john_doe", "john@example.com", 30, 50000)
print(employee.get_employee_info())
