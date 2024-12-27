class Employee:
    first_name = None
    salary = None
    
    def show_name(self):
        print(self.first_name)
        
    def show_salary(self):
        print(self.salary)
    
    pass    
employee = Employee()
employee.first_name = 'Andrey'
employee.salary = 50000
employee.show_name()
employee.show_salary()

