#importing tkinter library
from tkinter import *
class BMI(Tk):                  #creating class BMI calling tk library, which creates our GUI
    def __init__(self):         #defining intializer
        Tk.__init__(self)

        self.title("Calculate Your BMI")                    #title of the program

        #Weight label created 
        self.weightLbl = Label(self, text = "Weight(lbs) :") #this sentence basically created label called "Weight(lbs)" in our GUI
        self.weightLbl.grid(row =0, column =0)               #defines place in GUI where "weight(lbs)" label is created

        #entry box created
        self.txtWeight = Entry(self)                         #creates entry box where we can insert values for weight
        self.txtWeight.grid(row =0, column =1)               #defines place where entry box is placed in our GUI

        #height label created
        self.height1Lbl = Label(self, text ="Height(ft) :")  #this sentence basically creates label called "Height(ft)" in our GUI
        self.height1Lbl.grid(row= 1, column=0)               #defines place in GUI where "height(ft)" label is created

        #entry box created
        self.txtHeight1 = Entry(self)                        #creates entry box where we can insert values for weight
        self.txtHeight1.grid(row =1, column =1)              #defines place where entry box is placed in our GUI

        #height label created
        self.height2Lbl = Label(self, text ="Height(in) :")  #this sentence basically creates label called "Height(in)" in our GUI
        self.height2Lbl.grid(row= 2, column=0)               #defines place in GUI where "height(in)" label is created

        #entry box created
        self.txtHeight2 = Entry(self)                        #creates entry box where we can insert values for weight
        self.txtHeight2.grid(row =2, column =1)              #defines place where entry box is placed in our GUI

        #makes gap
        self.blank = Label(self, text = "")                  #this sentence basically creates empty label in our GUI so we can leave gap
        self.blank.grid(row =3, column =0)                   #defines place in GUI where empty label is created 

        self.blank1 = Label(self, text = "")                 #this sentence basically creates empty label in our GUI so we can leave gap
        self.blank1.grid(row =4, column =0)                  #defines place in GUI where empty label is created 

        #this shows output of our BMI index
        Label(self, text="BMI: ").grid(row =6, column =0)    #this sentence basically creates label called "BMI" in our GUI and also defines place where label"BMI" is created
        self.txtBMI = Label(self, bg = "#fff", anchor = "w", relief = "groove") #label is craeted with some extra-ordinary attributes which makes our label look as an entry box, but in real it is not an entry box it is just a label. Where bg= background color, anchor determines alignment, relief is border.
        self.txtBMI.grid(row =6, column =1, sticky="we")     #defines place in GUI where our label that look like entry box is created, where sticky is property in grid which changes height and widhth

        #this shows output of BMI status
        Label(self, text = "Status: ").grid(row=7, column=0) #this sentence basically creates label called "status" in our GUI and also defines place where label "status" is created
        self.stats = Label(self, bg = "#fff", anchor = "w", relief = "groove")#label is craeted with some extra-ordinary attributes which makes our label look as an entry box, but in real it is not an entry box it is just a label. Where bg= background color, anchor determines alignment, relief is border.
        self.stats.grid(row =7, column =1, sticky="we")      #defines place in GUI where our label that look like entry box is created, where sticky is property in grid which changes height and widhth


        self.btnCalculate = Button(self, text = "Calculate Your BMI") #Button is created called calculate your BMI, which will calculate on our BMI
        self.btnCalculate.grid(row=5 , columnspan=2)        #defines place in GUI where button "calculate your BMI" is created.
        self.btnCalculate["command"] = self.calculate       #this defines when the button is placed execute calculate method define below
        
    #this is where we take all the inputs given in entry box for weight, height and calculate our BMI and its status
    def calculate(self):                                    #calculate method being defined
        weight=int(self.txtWeight.get())                    #this gets our weight value entered in the entry box and saves it into variable called weight
        hight1=int(self.txtHeight1.get())                   #this gets our weight value entered in the entry box and saves it into variable called hight1
        hight2=int(self.txtHeight2.get())                   #this gets our weight value entered in the entry box and saves it into variable called hight2
        height=(12*hight1)+(hight2)                         #variable height is created which is used to convert height in inches
        result1= (weight / height**2)                       #this our formula to calculate BMI
        BMI= result1*703                                    #this is our final value of BMI

        self.txtBMI["text"]= "%.2f" %BMI                    #this prints out BMI value in the lable that looks like entry box which we created above

        #this is used to print out our BMI status based on BMI index value
        if BMI < 18.5:                              #if BMI index value is less then 18.5, then it will execute the below code otherwise it will check for next condition and do the same.
            status="underweight"                    #it assigns variable status value of "underweight" as above condition is true
            self.stats["text"]= "%s" %status        #this prints out status value in the lable that looks like entry box which we created above
        elif BMI<24.9:
            status="normal"
            self.stats["text"]= "%s" %status
        elif BMI<29.9:
            status="overweight"
            self.stats["text"]= "%s" %status
        elif BMI>30:
            status="obese"
            self.stats["text"]= "%s" %status

        
#main function is defined
def main():             
    app= BMI()                  #app variable is given value of BMI(), which will execute the BMI() class created above
    app.mainloop()              #it is looping until we exit, it is part of tk library which we used to created out BMI() class

main()                          #executes main function, which will execute BMI() class.
