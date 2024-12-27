class Employee:
    def show(self):
        return '+++'
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
print(employee1.show())

employee2 = Employee()
employee2.first_name = 'Sergey'
employee2.last_name = 'Romanov'
employee2.age = 25
employee2.salary = 40000
print(employee2.first_name, employee2.last_name ,employee2.age, employee2.salary)
print(employee2.show())
