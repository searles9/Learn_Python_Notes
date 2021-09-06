class Circle():
    #CLASS OBJECT ATTRIBUTE 
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi

    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
        
# Create an instance
my_circle = Circle()
# Refrence the pi attribute - 3.14
print(my_circle.pi) 
# Refrence the radius attribute 
# default is 1 becasue I didnt pass in a value when I created an instance
print(my_circle.radius)
# Use the area attribute
print(my_circle.area)
# Use the get_circumference method
print(my_circle.get_circumference())