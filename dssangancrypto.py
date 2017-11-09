# two list of characters that are encoded into another list
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"


#main function created and defines as follow
def main():

  #defining a condition
  keepGoing = True

  #loop starts while checking the condition
  while keepGoing:

    #variable created giving value of menu function, which will execute menu function
    response = menu()

    #condition being defined and states what to do if it is true
    if response == "1":
      plain = input("text to be encoded: ")      #takes userinput and stores into variable called plain      
      print(encode(plain))                       #Print's word, after encode function is executed it encodes the "plain" variable and print out the word.

    #second condition being define saying what to do if it is true.  
    elif response == "2":
      coded = input("code to be decyphered: ")  #takes input from user and stores into variable called coded
      print (decode(coded))                     #Print's word, after decode function is executed it decodes the "coded" variable and print out the word.

    # third condition being defined saying what to do if it true
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.") #print's a simple sentence for user
      keepGoing = False                                    #end of loop after this condition is true

    #last condition defined if none of the above condition are true
    else:
      print ("I don't know what you want to do...")   #simple print statment stating it cannot understand user

#menu function created and defined
def menu():
  print("Secret Decoder Menu")  
  print("\n0) Quit")
  print("1) Encode")
  print("2) Decode")
  respond=input("\nwhat do you want?")
  return respond

#encode function created which retrieves the variable plain and the word from it
def encode(plain):

  #the word that we are suppose to encode 
  alphaWord = ' '

  #position of the word in alpha list
  place = 0

  #variable created that stores the answer we will get after encoding the word
  keyWord = ' '

  #variable created which will keep in mind about the characters we have encoded so far
  count= -1

  #it will tell us when we are done with all characters of word we are suppose to encode
  end=((len(plain))-1)

  #variable result created that will give us our result of the word we encode
  result = ''
  
 #loop created to move around in our list of alpha 
  for a in alpha:
    count=(count+1)                 #tell's us about the characters we have encoded so far
    alphaWord= plain[count]         #character that we want to encode that we got from above line
    alphaWord = alphaWord[0].upper()#converts all userinput into uppercase so that we don't have to worry about the characters that we have in alpha

    #condition being defined, specfically saying if alphaword is not equals just a space then run this condition
    if(alphaWord != ' '):
      place = alpha.index(alphaWord) #determines the place of character of word in alpha list
      keyWord = key[place]           #maps to place in key list and stores it into variable keyWord
      result = (result + keyWord)    #stores result which is equal what we had previously and adds the new character encoded to it

    #other condition being defined saying if it is a simple space then do this    
    else:
      keyWord= '_'              #variable store empty space as underscore
      result=(result+keyWord)   #stores result which is equal what we had previously and adds the new character encoded to it.

    #last condition defined stating if our count is equals to end then it will return back to the last reault in the loop.
    if (count==end):
      return result         #reutrns back to last result in the loop
    

#deocde function created which retrieves the variable coded and the word from it
def decode(coded):

  #the word that we are suppose to decode 
  keyWord = ' '

  #position of the word in key list
  place = 0

  #variable created that stores the answer we will get after decoding the word
  alphaWord = ' '

  #variable created which will keep in mind about the characters we have encoded so far
  count= -1

  #it will tell us when we are done with all characters of word we are suppose to decode
  end=((len(coded))-1)

  #variable result created that will give us our result of the word we decode
  result = ''

  #loop created to move around in our list of alpha  
  for k in key:
    count=(count+1)         #tell's us about the characters we have decoded so far
    keyWord= coded[count]   #character that we want to decode that we got from above line
    keyWord = keyWord[0].upper()#converts all userinput into uppercase so that we don't have to worry about the characters that we have in key list

    #condition being defined, specfically saying if keyword is not equals just a space then run this condition
    if(keyWord != ' '):
      place = key.index(keyWord)     #determines the place of character of word in key list   
      alphaWord = alpha[place]       #maps to place in alpha list and stores it into variable alphaWord
      result = (result + alphaWord)  #stores result which is equal what we had previously and adds the new character encoded to it

    #other condition being defined saying if it is a simple space then do this 
    else:
      alphaWord= '_'              #variable store empty space as underscore
      result=(result+alphaWord)   #stores result which is equal what we had previously and adds the new character encoded to it.

    #last condition defined stating if our count is equals to end then it will return back to the last reault in the loop
    if (count==end):
      return result     #reutrns back to last result in the loop


# main function is executed which has sub-parts into menu, encode, and decode. All of them executes as the main function runs    
main()
