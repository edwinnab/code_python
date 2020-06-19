#class is a blueprint of an instance
class Students:
    def __init__(self, first_name,second_name, course,age):
        self.first_name = first_name
        self.second_name = second_name
        self.course = course
        self.age = age
        self.email = first_name + second_name + "@gmail.com"
        #methods atomatically takes the self instance
    def fullname(self):
        return "{} {}".format(self.first_name, self.second_name)

#class has attributes and methods
#instance of a class
stude_1 = Students("Edwinna", "Bikeri", "Computer Science", 18)
stude_2 = Students("Stella", "Achieng", "Computer Science", 23)
#instance variables contain data that is specific to each instance
"""stude_1.first_name = "Edwinna"
stude_1.second_name = "Jovial"
stude_1.email = "edwinnajovial@gmail.com"
stude_1.course = "Computer science"
stude_1.age = 23

stude_2.first_name = "winna"
stude_2.second_name = "vial"
stude_2.email = "winnavial@gmail.com"
stude_2.course = "Computer engineering"
stude_2.age = 23"""

#print(stude_1.email)
#print(stude_2.email)
#calling the method using the class
print(Students.fullname(stude_1))
print(Students.fullname(stude_2))
#calling the method fullname using the instance
#print(stude_1.fullname())
#print(stude_2.fullname())