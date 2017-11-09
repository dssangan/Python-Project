#showing inheritance from its parent program which will run the whole program
from OOPRectangledssangan import *

#this part will run throught the class and show us the results
print ("\nRectangle a:")                    #simple print statement
a = Rectangle(10, 15)                       #defining a variable a;which is an intence in our class, which will recall class rectangle given parameters that width and heigh are 10 and 15 respectively.
print ("area:      {}".format(a.area))      #Print out area, by accessing the area property which gets answers from the method in the rectangle class.
print ("perimeter: {}".format(a.perimeter)) #Print out perimeter, by accessing the perimeter property which gets answers from the method in the rectangle class.

print ("")                  #simple print statement that is just used to create a blank line
print ("Rectangle b:")      #simple print statement that will show rectangle b and its properties
b = Rectangle()             #assign variable b;which is our instance in a class,  a value such that it will execute class Rectangle
b.setwidth(20)              #since we have made our property private we have to use assign values inside a method
b.setheight(5)              #Our property is private therefore we have to assign value inside a method
print (b.getStats())        #basically prints out all getStats method inside the rectangle class.
