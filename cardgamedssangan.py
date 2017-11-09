""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random           #importing the random library

NUMCARDS = 52           # Assign the NUMCARDS value of 52, it basically means there are 52 number of cards
DECK = 0                # Assign value to DECK so that it defines the palce of the DECK, so in 52 cards if the value is 0 then it means that it belongs to Deck  
PLAYER = 1              # Assign value to DECK so that it defines the palce of the DECK, so in 52 cards if the value is 0 then it means that it belongs to Player
COMP = 2                # Assign value to DECK so that it defines the palce of the DECK, so in 52 cards if the value is 0 then it means that it belongs to Comp

cardLoc = [0] * NUMCARDS #Assign card location a value, in this specific case we are multiplying 0 to 52 numbers of cards. So the location of each card is set to 0 in this case, which means all the cards are in deck.

#Assign suitName a string that contains all suit names that we have in 52 cards.
suitName = ("hearts", "diamonds", "spades", "clubs")

#Assign rankName a string that contains the rank of cards from Ace to king, in 52 cards.
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
#Assign playerName a string that contains the name of player who are playing with the cards/
playerName = ("deck", "player", "computer")

def main():                     #Defining the main function
  clearDeck()                   #Calling cleardeck() functin

  for i in range(5):            #For loop created that runs for 5 five times and assign's card to player and Comp
    assignCard(PLAYER)          #assignCard() function is called which assign's card to the player, in this the case the player is itself called Player.
    assignCard(COMP)            #assignCard() function is called which assign's card to the player, in this the case the player is called Comp.

  showDeck()                    #showDeck() function is called which basically shows all the cards in the deck
  showHand(PLAYER)              #showDeck() function is called which basically shows all the card in the player's hand
  showHand(COMP)                #showDeck() function is called which basically shows all the card in the Comp's hand

#cleardeck function is defined, which bascially bring all the cards back into the deck, i.e, no player has cards everything is inside Deck
def clearDeck():
    cardLoc=[0]*NUMCARDS        #Assign card location a value, in this specific case we are multiplying 0 to 52 numbers of cards. So the location of each card is set to 0 in this case, which means all the cards are in deck.
    return cardLoc              #return the value of cardLoc back.

#assigncard() function is defined, which bascially tells us to whom we are handing over the cards, for exmaple are we giving it to player, comp or keep it in the deck.
def assignCard(hnd_over):
    findCard=True                          #making a condition true which will allow while loop to run
    while findCard:                        #while loop is created so that it can keep running until the condition we made above is false.
        location=random.randint(0,51)      #choosing random location from given range,which is basically the no of cards we have i.e, 52.
        if cardLoc[location] == 0:         #checking condition that if the location we choose randomly, is equal to 0 in the cardlocation then execute the following code.
            cardLoc[location]=hnd_over     #when the above condition is correct it will hand over the card to the person, and will save its location saying this card has been given to this person
            findCard=False                 #this statement tell that the condition we made is false now so it will quit out from the loop

#translateCard is being defined, which basically converts translate the location of the card into the its name.
def translateCard(CardNum):
    suit_Num=int(CardNum/13)       #this statement gives us the suit number of the card which we will use to define actual suit name from the "suitName" string, by taking its location, and the "int" function is used to convert the answer into intger form.
    rank_Num=CardNum%13            #this statement gives us the rank number of the card which we will use to define actual rank name from the "rankName" string, by taking its location.
    Suit=suitName[suit_Num]        #this statement gets the acutal suit name from the string"suitName" by looking at the suit number and use that number to identify the suit location in the string.
    Rank=rankName[rank_Num]        #this statement gets the acutal rank name from the string"rankName" by looking at the rank number and use that number to identify the rank location in the string.
    output= Rank + ' of ' + Suit   #this statement define what output should look like
    return output                  #returning the value output

#showdeck is being defined, which will bascially show the whole deck, including all the card name and who is it assigned to5
def showDeck():
    print(" # 	     card 	 	 location")  #simple print statement, that meets the requirement for output shown on assignment page

    for i in range(0,52):                            #for loop created show that it can display all the cards, basically it is saying to run in the range given
        if cardLoc[i]==0:                            #first condition made saying, if the cardlocation value is 0 then execute the below code
            locText='Deck'                           #if the condition is true than loctext is equal to deck, which basically means the location of the card is in deck

        elif cardLoc[i]==1:                          #condition being made saying, if the cardlocation value is then execute the below code
            locText='Player'                         #if the condition is true than loctext is equal to Player, which basically means the location of the card is in Player's hand.

        elif cardLoc[i]==2:                          #condition made saying, if the cardlocation value is 2 then execute the below code
            locText='Computer'                       #if the condition is true than loctext is equal to Comp, which basically means the location of the card is in Comp's hand.

        print("{0:2}      {1:20}      {2:6}".format(i,translateCard(i),locText)) #this is a print statement and it calls transaltecard function, that prints out the number of card in deck, the actual card with its suit and rank name,
                                                                                 #and last but not least it shows who holds the text. The alignment is done by assigning the location between two points.

def showHand(person):                               #showhand function is being defined, which bascially shows what cards does person have in their hands.
    if person == 1:                                 #making condition if the person number is  1, then execute the following code
        print('\nDisplaying Hand of player')        #this basically prints a statement that is in new line, saying "Displaying Hand of Player"

    elif person == 2:                               #defining condition saying if the person number is 2, then execute the following code.
        print('\nDisplaying Hand of Comp')          #Basic print statement, that will print a statement to new line saying "displaying hand of Comp"

    for i in range(0,52):                           #for loop created that runs in the given range, which is basically equal total number of card we have.
        if cardLoc[i]==person:                      #condition being made saying if the condition is true execute the following code, this statement basically determines who is the person from above conditions and shows the hand of that specific person.
            print("{}".format(translateCard(i)))    #print statement calls translatecard function and basically prints the card with its suit name and rank name.
    

main()                                              #calling main function, which will make main function to run and main function will run its sub-function. 

                    
        
    
    
