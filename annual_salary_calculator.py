class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show_salary(self):
        return self.salary*12
    
e1=employee("muskan",80000)
print("annual salary:",e1.show_salary())
      