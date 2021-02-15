"""
Inheritance is child class inherits attributes and behaviours from parent class. 
The newly formed class is a derived class (or child class). The existing class is a base class (or parent class).
Inheritance is used for code reusability purpose.

"""


#Class is a blue print of object. Defining a class does not allocate any memory whereas Instance creation of an object dose.
class Employee:
    #class Attribute empID are same for all instances of a class
    empID = 0
    def __init__(self, name):
        #Instance attribute name is different for different object
        print("Welcome to the company {}".format(name))
    def yourEmpID(self):
        print("Your EmpID is {}".format(self.empID))

class HR(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        Employee.empID +=1

    def department(self):
        print("Welcome to HR Department")

class Administration(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)
        Employee.empID +=1
        
    def department(self):
        print("Welcome to Administration Department")


#Object Instantiation an Object has an attribute which can be class attribute and object attribute and behaviour which is a method

emp1 = HR("Priya")
emp1.yourEmpID()
emp1.department()

emp2 = Administration("Pawri")
emp2.yourEmpID()
emp2.department()

emp3 = Administration("Sam")
emp3.yourEmpID()
emp3.department()