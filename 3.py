class Employee:
    first_name = None
    last_name = None
    age = None
    salary = None
    pass    
employee = Employee()
employee.first_name = 'Andrey'
employee.last_name = 'Kostylev'
employee.age = 24
employee.salary = 50000
print(employee.first_name, employee.last_name ,employee.age, employee.salary)