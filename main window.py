from tkinter import *                           #importing everything from tkinter library
from monthlystatement import *                  #inherting the monthlystatement program     
import time                                     #importing time library 
import sqlite3                                  #importing sqlite3 library to work in databases
class project1(Tk):                             #creating class project which calls our tk library, which is going to help us build our GUI
    entry = 0                                   #assinging variable entry so far to be equal 0
    theCursor = 0                               #assigning varaible theCursor value of 0
    def __init__(self):                         #defining intializer
        Tk. __init__(self)                      #calling intializer 

        self.title("Software")                  #titles our gui window as "software"

        self.blank=Label(self,text="")          #Creates an empty label
        self.blank.grid(row=0,column=0)         #assings the position of empty label in GUI window

        #headlbl label created                           
        self.headlbl=Label(self, text="Business Name")  #creating label called "Business Name"
        self.headlbl.grid(row=0, column=1)              #asssings the position to the headlbl
        self.headlbl.config(font=("Arial",64))          #configures the font type and size of label text

        #phone label created
        self.phone=Label(self,text="Contact Info:+1(123)-456-7891")     #creates label called "contact info....."
        self.phone.grid(row=0, column=2)                                #assings position to the label
        self.phone.config(font=("Times New Roman",12))                  #configure the label text font type and size

        #Date label created
        self.date=Label(self,text="Date:")              #creates label called date
        self.date.grid(row=1,column=0)                  #assings posisiton to label date
        self.date.config(font=("Times New Roman",14))   #configures label date text font type and size

        #txtdate label created 
        self.txtdate= Label(self, text=time.strftime("%d%m%Y") ,bg="#fff", anchor='w', relief="groove" , width=20, height=2) #creates a label that looks like entry box and get time from the statement and prints out as text
        self.txtdate.grid(row=1, column=1)              #assigns position to the label txtdate

        self.blnk=Label(self,text="")                   #creates empty label helpful to other labels to get them assign in determined position
        self.blnk.grid(row=1,column=1)                  #assigns position to empty label

        self.blnk=Label(self,text="")                   #creates empty label helpful to get other labels assigned in determined position
        self.blnk.grid(row=2,column=0)                  #assings position to empty label
        
        self.ricptnum=Label(self,text = "Reciept Number:") #creats ricptnum label
        self.ricptnum.grid(row=3,columnspan=1)             #assing position to label
        self.ricptnum.config(font=("Arial",24))            #configures the label text font type and size

        self.txtreciept=Entry(self)                         #creates entry field to enter reciept number
        self.txtreciept.grid(row=3, column=1)               #assings position to entry field
                        
        self.cmpny=Label(self,text="Customer Name:")        #creates label called customer name
        self.cmpny.grid(row=3,column=2)                     #assigns position to the label
        self.cmpny.config(font=("Arial",24))                #configures label text font type and size

        self.txtcmpny=Entry(self, width=30)                 #creates entry field for the above label 
        self.txtcmpny.grid(row=3, column=3)                 #assigns position to entry field

        self.blnk1=Label(self,text="")                      #creates empty label
        self.blnk1.grid(row=4,column=1)                     #assigns position to empty label

        self.describe=Label(self,text="Item Description")   #creates label called item description
        self.describe.grid(row=5,column=0)                  #assigns position to label describe
        self.describe.config(font=("Arial",24))             #configures label text font type and size

        self.quantity=Label(self,text="No. of Quantity:")   #creates label called quantity
        self.quantity.grid(row=5,column=1)                  #assings position to label
        self.quantity.config(font=("Arial",24))             #configures label text font type and size

        self.time=Label(self, text="Delivery time")         #creates label called time
        self.time.grid(row=5, column=2)                     #assigns position to label
        self.time.config(font=("Arial",24))                 #configures label text font type and size

        self.txtdescribe= Label(self, bg="#fff", anchor="w", relief="groove", text=" item description", height=12, width=25)    #creates entry field look like label and has text about item description
        self.txtdescribe.grid(row=6, column=0)              #assigns position to label that looks like entry field

        self.entryquantity= Entry(self, width=10, font=("Arial",24))            #creates entry field, and with every entry it changes the 
        self.entryquantity.grid(row=6, column=1, ipady=80)                      #assigns position to entry field and adds optional vertical internal padding

        self.entrytime= Entry(self, width=10, font=("Arial",24))                #creates entrytime entry field which intakes the time from user
        self.entrytime.grid(row=6, column=2, ipady=80)                          #assigns position to entry field and adds optional vertical internal padding

        self.blnk2=Label(self, text="")                 #creates empty label to help other label get positioned into proper layout
        self.blnk2.grid(row=7, column=0)                #assigns position to the label 

        self.blnk2=Label(self, text="")                 #creates empty label to help other label get positioned into proper layout
        self.blnk2.grid(row=8, column=0)                #assigns position to the label


        self.monthly=Button(self, text="Make Monthly Statement", bg="grey")     #creates button called make monthly statement with grey background
        self.monthly.grid(row=9, column=0, ipadx=20, ipady=20)                  #assigns position to the button and padded the internal with the defined values
        self.monthly["command"]=monthly                                         #when the button is pressed it executes the class monthly that is inhereted from monthly statement program

        self.btnsave=Button(self, text="Save", bg="grey")                       #creates button called save with grey background
        self.btnsave.grid(row=9,column=2, ipadx=20, ipady=20)                   #assigns position to the button and pads the internals with defined values
        self.btnsave["command"]=self.savedata                                   #executes the method called savedata

        #open or create database if doesn't exists
        self.entry= sqlite3.connect('recieptentry.db')                          

        #The cursor traverses(travels through) the records
        self.theCursor= self.entry.cursor()

        #create the table if it doesn't exist
        try:
            self.entry.execute('''CREATE TABLE if not exists Receipt
                               (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                DATE INTEGER NOT NULL, CUSTOMER TEXT NOT NULL,
                                QUANTITY INTEGER NOT NULL,
                                RECEIPT TEXT NOT NULL,
                                TIME INTEGER NOT NULL); ''')


            #save everything into database file
            self.entry.commit()

        #or else check for error and print out if error occurs
        except sqlite3.OperationalError:
            print("table not created")

    def savedata(self):
                
        #Insert the receipts info into database taking it from gui
        self.entry.execute("INSERT INTO Receipt (DATE, CUSTOMER, QUANTITY, RECEIPT, TIME)" +
                           "VALUES('"+self.txtdate.cget("text")+"', '"+self.txtcmpny.get()+"', '"+self.entryquantity.get()+"', '"+self.txtreciept.get()+"', '" +self.entrytime.get()+"')")

        #save all entry into database
        self.entry.commit()

        print("INSERT INTO Receipt (DATE, CUSTOMER, QUANTITY, RECEIPT, TIME)" +
                           "VALUES('"+self.txtdate.cget("text")+"', '"+self.txtcmpny.get()+"', '"+self.entryquantity.get()+"', '"+self.txtreciept.get()+"', '" +self.entrytime.get()+"')")
        
        #clears all the entry box
        self.txtreciept.delete(0,"end")
        self.entryquantity.delete(0,"end")
        self.entrytime.delete(0,"end")
        self.txtcmpny.delete(0,"end")

            
#main function defined which executes the class project1
def main():
    App= project1()             #variable called app is executes the class project
    App.mainloop()              #loops through the project which

main()                          #executes the main function
