#class rectangle created
class Rectangle():
    def __init__(self, width=0, height=0):          #defining the intializer(constructor which links to the class) with certain parameters which will take instance from main()function.
        self.setwidth(width)                        #(using self parameter links to the current class)parameter calls the method with certain values inside from main function
        self.setheight(height)                      #same as above
        self.setarea()                              #parameter calls method that does further calculation in program
        self.setperimeter()                         #same as above

    #setter and getter method are defined    
    def setwidth(self, width):                      #setting width method, which takes the parameter and certain values and stores it
        self.__width  = width                       #parameter private width defined which is equal to width.

    def getwidth(self):                             #getting width method, which takes the parameter and certain values and stores it               
        return self.__width                         #returns the private width parameter define above.
    
    def setheight(self, height):                    #setting heigh method, which takes the parameter and certain values and stores it
        self.__height = height                      #parameter private height defined which is equal to height.

    def getheight(self):                            #getting height method, which takes the parameter and certain values and stores it
        return self.__height                        #returns the private height parameter define above.

    def setarea(self):                              #setting area method, which takes the parameter and certain values and stores it
        self.__area= self.__width*self.__height     #parameter private area defined which is equal to parameter private width * private height.

    def getarea(self):                              #getting area method, which takes the parameter and certain values and stores it
        return self.__area                          #returns the private area parameter define above.

    area= property(fset= setarea ,fget=getarea)     #set area equal to property setarea and getarea so it can follow up with main function
    
    def setperimeter(self):                                 #setting perimeter method, which takes the parameter and certain values and stores it
        self.__perimeter=(2*self.__width)+(2*self.__height) #parameter private area defined which is equal to (2*parameter private width) +(2* parameter private height.)

    def getperimeter(self):                                 #getting area method, which takes the parameter and certain values and stores it
        return self.__perimeter                             #returns the private perimeter parameter define above.

    perimeter= property(fget= getperimeter, fset=setperimeter)  #set perimeter equal to property setperimeter and getperimeter so it can follow up with main function

    def getStats(self):                             #getStats method defined which takes the self parameter
        self.setarea()                              #recalls parameter setarea and setperimeter methods.
        self.setperimeter()
        return "widht: {} \nheight: {} \narea: {} \nperimeter: {}".format(self.__width, self.__height, self.__area, self.__perimeter) #simple print statment that recalls the width,heiht,area and perimeter parameter
    

def main():                                         #defining main function
    print ("Rectangle a:")                          #simple print statement that will give details about rectangle a
    a = Rectangle(5, 7)                             #Variable instance "a" created that will recall class Rectangle with given width and height inside rectangle class
    print ("area:      {}".format(a.area))          #print statement that will print out the area by recalling area property which will getarea from the class
    print ("perimeter: {}".format(a.perimeter))     #print statement that will print out the perimeter by recalling perimeter property which will getperimeter from the class
    
    print ("")                                      #smiple print statement that creates empty line
    print ("Rectangle b:")                          #print statment that will print Rectangle b details
    b = Rectangle()                                 #variable instance "b" is created which will start Rectangle class and 
    b.setwidth(10)                                  #instance b takes setwidth method with the value of width 
    b.setheight(20)                                 #instance b takes setheight method with the value of height
    print (b.getStats())                            #prints out the instance b getStats method

                
main()                                              #execute the main function
