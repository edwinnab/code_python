class Dog():
    def __init__(self, typ, color, age):
        self.typ = typ
        self.color = color
        self.age = age 
    def eating(self):
        return "{} {} loves eating meat.".format(self.typ, self.color)
dog1 = Dog("GermanSheherd", "brown", 12)
print(dog1.eating())        

class Vehicles():
    def __init__ (self,type,color,cost):
        self.type = type
        self.color = color
        self.cost = cost
    def description(self):
        return "{} {} costs Ksh = {} ".format(self.type, self.color,self.cost)
car1 = Vehicles("v8_Toyota", "brown", "23.56M" )
print(car1.description())