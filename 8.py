class Student:
    name = 'danila'
    surname = 'kostylev'
    
    def show(self):
        return self.cape(self.name + ' ' + self.surname)
        
    def cape(self,stri):
        return stri.upper()
    
    def iitials(self):
        return self.cape(self.name[0] + ' ' + self.surname[0])
student = Student()
print(student.show())
print(student.iitials())

