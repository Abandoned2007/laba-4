class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def raise_salary(self, amount=300):
        self.salary += amount
        print("Зарплата была увеличена.")

    def get_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Должность:", self.position)
        print("Зарплата:", self.salary)

emp1 = Employee("Иван", 25, "менеджер", 3000.0)
emp1.get_info()  
emp1.raise_salary()  
emp1.get_info() 