"""
Using encapsulation is an important feature. It allows binding of data and logic in a single feature. 
It restrict access to methods and variables. This prevents data from direct modification
"""

class Credential:
    def __init__(self, name):
        #We denote private attributes _ and __ as prefix
        self.__password = "Avtkl"
        self.name = name
    
    def showPassword(self):
        print("Hi {} Your current password is {}".format(self.name, self.__password))
    
    def updatePassword(self, password, name):
        self.__password = password
        self.name = name

#Used __init__() method to store the password
user = Credential("Person1")
user.showPassword()
#Output: Hi Person1 Your current password is Avtkl

#tried to update password using updatePassword
user.updatePassword("JKJKJK", "Person2")
user.showPassword()
#Output: Hi Person2 Your current password is JKJKJK

#Can't change it because Python treats  __password as private attributes.
user.__password = "jhjsd"
user.name = "Person3"
user.showPassword()
#Output: Hi Person3 Your current password is JKJKJK
