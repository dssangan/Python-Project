#printing a statement
print("I'm thinking of a number between"
      "1 and 100. Guess a number, and"
      "I'll tell you if you're"
      "too high, too low, or got it right"
      "Good Luck!")

#importing random between 1 to 100
import random
result = random.randint(1,100)
keepGoing = True                                #allowing to program to keep running ahead 
count=0                                         #starting the counter from 0

#starting a loop so that program keeps running until correct answer is achieved
while keepGoing:
    guess= input("Please Enter the number")     #variable created to take input from user
    guess=int(guess)                            #converting the string into integer

#checking a condition and moving forward    
    if guess>result:
        print("The number is too high, Please try again")
        count= count+1                          #adding one to counter so at the end it will tell us how many trials it took us to get correct answer
        keepGoing=True                          #allowing program to start back at from loop

#checking a condition and moving forward
    elif guess<result:
        print("The number is too low, Please try again")
        count= count+1                          #adding one to counter so at the end it will tell us how many trials it took us to get correct answer
        keepGoing=True                          #allowing program to start back at from loop

#last condition and about to exit out from the program 
    else:
        print("Great! You got it Correct")
        count= count +1                         #adding one to counter so at the end it will tell us how many trials it took us to get correct answer
        keepGoing=False                         #allowing program to quit out of loop and move to next step

#printing the amount of trials it took to get to correct answer
print("{}".format(count))
