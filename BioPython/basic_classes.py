#!/usr/bin/env python3
# basic_classes.py

class Circle():
    '''Class which returns daimeter, circufrence, and colour as according to the radius and colour passed along with class object
    '''
    def __init__(self, color, radius):
        # Initialization of variables
        self.color = color
        self.radius = float(radius)
    
    def daimeter(self):
        # Daimeter
        return (self.radius * 2)

    def circumfrence(self):
        # Circufrence
        return (2 * 3.14 * self.radius)

    def isRed(self):
        '''If colour is red pass TRUE else FALSE
        '''
        if self.color == "red":
            return True
        else:
            return False


class GraduateStudent():
    '''Class Returns the year of education matriculated
    '''
    def __init__(self, first_name, last_name, year, major):
        # Initial function
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    def year_matriculated(self):
        # Function for year matriculated
        return (2020 - self.year)


circle1 = Circle("red", 4)
print(circle1.daimeter())
print(circle1.circumfrence())
print(circle1.isRed())

grad = GraduateStudent("Ris","Nar", 2018, "Bioinfo")
print(grad.year_matriculated())
