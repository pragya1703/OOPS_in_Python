#Overriding : Functions with the same definition have different behavior in different scopes. Used by a child class to change behavior it inherited from its parent.

class Parent:
 
    def fun1(self):
        print('feature_1 of class A')
         
    def fun2(self):
        print('feature_2 of class A')
     
 
class Child(Parent):
     
    # Modified function that is 
    # already exist in class Parent
    def fun1(self):
        print('Modified feature_1 of class A by class B')    
         
    def fun3(self):
        print('feature_3 of class B')
         
 
# Create instance
obj = B()
     
# Call the override function
obj.fun1()