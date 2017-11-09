from tkinter import *                                           #import everything from tkinter 
import sqlite3                                                  #import sqlite 3 library

class monthly(Tk):                                              #class monthly created which will be executed into different program.
    def __init__(self):                                         #define initializer
        Tk. __init__(self)                                      #calling initializer

        self.title("Make monthly statement")                    #define title of our window
        
        self.custmername= Label(self, text="Customer Name")     #creates label called customer name
        self.custmername.grid(row=0, column=0)                  #assings position to the label

        self.txtname=Entry(self)                                #creates entry field where we can input our data
        self.txtname.grid(row=0, column=1)                      #assigns position to the label

        self.frmdate= Label(self, text="From Date:")            #creates labe called from date
        self.frmdate.grid(row=1, column=0)                      #assigns position to the label

        self.txtfrm= Entry(self)                                #creates entry field where we can input our data
        self.txtfrm.grid(row=1, column=1)                       #assigns position to the entry field

        self.todate=Label(self, text="TO Date:")                #creates label called to date
        self.todate.grid(row=1, column=2)                       #assigns position to the label

        self.txttodate= Entry(self)                             #creates entry field 
        self.txttodate.grid(row=1 , column=3)                   #assigns position to the entry field

        self.butnview= Button(self, text="Preview" )            #creates button called preview
        self.butnview.grid(row=2, column=2)                     #assings position to the button
        self.butnview["command"]=self.preview                   #assigns when button is pressed execute preview method

        self.blank= Label(self, text="")                        #creates blank label
        self.blank.grid(row=3, column=0)                        #assigns position to empty label

        scrollbar=Scrollbar(self)                               #create scrollbar
        self.outputbox= Listbox(self)                           #creates listbox
        self.outputbox.insert(1, "Date              Quantity   ReceiptNumber  Time")        #insert this text into row 1 of the list box
        self.outputbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W+E)    #assigns position and pads it internally

    def preview(self):                                          #method preview defined

        #clears out the older entry for different person
        self.outputbox.delete(1, END)
        

        Name= str(self.txtname.get())                           #gets txtname and stores into variable name
        Date= (self.txtfrm.get())                               #gets txtfrm and stores into variable name date
        toDate= (self.txttodate.get())                          #gets txttodate and stores into variable toDate


        #open or creates database if it doesn't exists (in this case it just openeing it)
        self.input = sqlite3.connect('recieptentry.db')

        #the cursor traverses(travels through) the records
        self.theCursor= self.input.cursor()

        #selects distinct data when certain conditions are met    
        vew= self.input.execute('SELECT DISTINCT ID, DATE, QUANTITY, RECEIPT, TIME from Receipt where CUSTOMER =? and DATE >= ? and DATE <= ?' ,(Name,Date, toDate))
 
        
        #receieves the list of data that holds results and saves into certain variable which will be outputted into GUI listbox
        for col in vew:
            cust_id= col [0]
            cust_date=col[1]
            qaunti = col [2]
            number= col[3]
            time= col[4]
            #all the values gain from database  is printed out in listbox
            self.outputbox.insert(cust_id, str(cust_date)+"       "+str(qaunti)+"                    "+str(number)+"              "+str(time))
                   
        #clears all the entry made in guid
        self.txtname.delete(0, "end")
        self.txtfrm.delete(0, "end")
        self.txttodate.delete(0, "end")
            
            
        

        
        
