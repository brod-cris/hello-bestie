# import re

# regex = '^[a-z0-9]+[\._]?[az0-9]+[@]\w+[.]\w{2,3}$'


# def check(email):
#     if(re.search(regex, email)):
#         print("Valid Email")
#     else:
#         print("Not a valid email")


# if __name__ == "__main__":
#     email = input("Enter the email id:")
#     check(email)

# *********************

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# x = Person("John", "Puruntong")
# x.printname()

# ********************

import re
# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:",
#       x.start())

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)

txt = "The rain in Spain"
x = re.sub("\s", "fish", txt)
print(x)
