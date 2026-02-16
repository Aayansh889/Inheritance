class Person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)
class employee(Person):
    def __init__(self,name,id_number,salary,post):
            self.salary=salary
            self.post=post            
            Person.__init__(self, name, id_number)
a=employee("Rahul",18901990,200000,"Intern")
a.display()