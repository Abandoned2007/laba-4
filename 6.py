class Employee:
    def show(self, first_name, salary):
        return first_name + ' ' + salary
    first_name = None
    last_name = None
    age = None
    salary = None
    
    pass
employee1 = Employee()
employee1.first_name = 'Andrey'
employee1.last_name = 'Kostylev'
employee1.age = 24
employee1.salary = 50000
print(employee1.first_name, employee1.last_name ,employee1.age, employee1.salary)
print(employee1.show('Andrey', '50000'))
