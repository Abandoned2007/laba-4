class Position:
    def __init__(self, title):
        self.title = title

class Department:
    def __init__(self, name):
        self.name = name

class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


position = Position("Software Engineer")
department = Department("Development")


user = User("Alice", position, department)


print(f"Name: {user.name}")
print(f"Position: {user.position.title}")
print(f"Department: {user.department.name}")
