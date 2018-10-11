"""
Created on Tue Aug 28 15:45:54 2018

@author: Darshan Sangani
"""
import numpy as np
import pandas as pd
from numpy import genfromtxt
from datetime import datetime

#Reading Necessary files
#df = pd.read_csv('FOB History.csv')
my_data = genfromtxt('FOB.csv', delimiter=',', dtype =(str))

#Creating new array where the new data will be stored
New_data = np.empty([10000,3], dtype = '<U18')

#Giving head titles to the new array set
New_data[0,0] = "Name"
New_data[0,1] = "Date"
New_data[0,2] = "Total Time"

'''
Employee_Name = my_data[1,2]+my_data[1,3]
Starting_Date = my_data[1,0]
Starting_Time = my_data[1,1]
Ending_Time = my_data[1,9]
'''
#Total_time = (datetime.strptime(Ending_Time, '%H:%M') - datetime.strptime(Starting_Time, '%H:%M'))
i=1
j=i
x=1
for i in range(1,4027):
    current_date = my_data[j,0]
    #print("Current data is:  " + current_date)
    New_data[i,1] = current_date
    New_data[i,0] = my_data[j,2] + " " +my_data[j,3]
    #print("Name of an employee:  " + New_data[i,0])
    Total_time = "00:00"
    Total_time = datetime.strptime(Total_time, '%H:%M')
    #print("Total Time :  " + str(Total_time))
    for k in range(x,4027):
        #print("value of j is : " + str(j))
        Start_date = my_data[j,0]
        #print("Start  Data :  " + Start_date)
        Start_time = my_data[j,1]
        #print("Start Time :  " + Start_time)
        k = k+1
        j = j+1
        #print("value of j is : " + str(j))
        End_date = my_data[j,0]
        #print("End Date :  " + End_date)
        End_time = my_data[j,1]
       # print("End Time :  " + End_time)
        if(Start_date == current_date):
            #print("Inside First IF statement Start_data == current_date")
            if(Start_date == End_date):
               # print("Entering first condition of first if statement")
                Final_time = datetime.strptime(End_time, '%H:%M')- datetime.strptime(Start_time, '%H:%M')
               # print("Final Time:  " + str(Final_time))
                Total_time = Total_time + Final_time
                New_data[i,2] = str(datetime.strftime(Total_time, '%H:%M'))
                j=j+1
                k=k+1
                #print("Total_Time is:  " + str(Total_time))
                #print("value of j is : " + str(j))
            elif (Start_date != End_date):
                #print("value of j is : " + str(j))
                j=j-1
                #print("value of j is : " + str(j))
                Start_date = my_data[j,0]
                #print("Start  Date :  " + Start_date)
                Start_time = my_data[j,1]
                #print("Start Time :  " + Start_time)
                j=j-1
                End_date = my_data[j,0]
                #print("End Date :  " + End_date)
                End_time = my_data[j,1]
                #print("End Time :  " + End_time)
                if(Start_date == current_date):
                    #print("Entering first condition of first if statement")
                    Final_time = datetime.strptime(End_time, '%H:%M')- datetime.strptime(Start_time, '%H:%M')
                    #print("Final Time:  " + str(Final_time))
                    Total_time = Total_time + Final_time
                    New_data[i,2] = str(datetime.strftime(Total_time, '%H:%M'))
                    j=j+2
                    x = j
                    break
                elif(Start_date != current_date):
                    #print("Entering second condition of first elif statment")
                    New_data[i,2] = "Forget to clock out"
                    x = j
                    break
        elif(Start_date != current_date):
            #print("Entered second if condition")
            x=j
            j=j-1
            break
    df = pd.DataFrame(New_data)
    df.to_csv("Final_Report2.csv")
