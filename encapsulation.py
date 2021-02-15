"""
Using encapsulation is an important feature. It allows binding of data and logic in a single feature. 
It restrict access to methods and variables. This prevents data from direct modification
"""

class Credential:
    def __init__(self):
        #We denote private attributes _ and __ as prefix
        self.__password = "Avtkl"
    
    def showPassword(self):
        print("Your current password is {}".format(self.__password))
    
    def updatePassword(self, password):
        self.__password = password

#Used __init__() method to store the password
user = Credential()
user.showPassword()
#Output: Your current password is Avtkl

#tried to update password using updatePassword
user.updatePassword("JKJKJK")
user.showPassword()
#Output: Your current password is JKJKJK

#Can't change it because Python treats the __password as private attributes.
user.__password = "jhjsd"
user.showPassword()
#Output: Your current password is JKJKJK