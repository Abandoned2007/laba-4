class Student:
    name = 'Danila'
    surname = 'Kostylev'
    
    def show(self):
        return self.name + ' ' + self.surname
    
student = Student()
print(student.name, student.surname)