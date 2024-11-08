class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        print(f"Name: {self.name}")
        print(f"ID Number: {self.idnumber}")

    def display(self):
        print(f"Name: {self.name}, ID Number: {self.idnumber}")

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  
        self.salary = salary 
        self.post = post

    def display(self):
        super().display()  
        print(f"Salary: {self.salary}, Post: {self.post}")


a = Employee('Ayobami', 13572024, 2000000, 'Manager')
a.display()