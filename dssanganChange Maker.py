#created variable  that takes the input for price of an item
x = input("Price of the item: ")


#converting integers to floating points number so that we dont have difficulty with decimal numbers.
x = float(x)


#created variable that takes input for the amount given by customer for purchased item
y = input("cash tendered: ")



#converting integers to floating points number so that we dont have difficulty with decimal numbers.
y = float(y)


#created variable that tells us how much amount we have to payback to customer
result = (y - x)



#converting integers to floating points number so that we dont have difficulty with decimal numbers.
result = float(result)


#rounding decimal numbers to 2 digits after decimal points
result = round(result,2)


#prints the change we have to pay to customer
print("Change: {}".format(result))



#all the below program gives us the no.of bills we have to use to payback
#gives no.of $50.00bills we have to give
remainderZ=result%50            #gives the amount left
Z=result//50                    #gives the no.of bills to give
remainderZ=round(remainderZ,2)  #rounds up the amount left to 2 decimal points
print("fifty: {}".format(Z))    #prints the no.of bills to give



#gives no.of $20.00bills we have to give
remainderA=remainderZ%20        #gives the amount left
A=remainderZ//20                #gives the no.of bills to give
remainderA=round(remainderA,2)  #rounds up the amount left to 2 decimal points
print("twenty: {}".format(A))   #prints the no.of bills to give



#gives no.of $10.00bills we have to give
remainderB=remainderA%10        #gives the amount left
B=remainderA//10                #gives the no.of bills to give
remainderB=round(remainderB,2)  #rounds up the amount left to 2 decimal points
print("ten: {}".format(B))      #prints the no.of bills to give



#gives no.of $5.00bills we have to give
remainderC=remainderB%5         #gives the amount left
C=remainderB//5                 #gives the no.of bills to give
remainderC=round(remainderC,2)  #rounds up the amount left to 2 decimal points
print("fives: {}".format(C))    #prints the no.of bills to give



#gives no.of $1.00bills we have to give
remainderD=remainderC%1         #gives the amount left
D=remainderC//1                 #gives the no.of bills to give
remainderD=round(remainderD,2)  #rounds up the amount left to 2 decimal points
print("one: {}".format(D))      #prints the no.of bills to give



#gives no.of $0.25coins we have to give
remainderE=remainderD%0.25      #gives the amount left
E=remainderD//0.25              #gives the no.of bills to give
remainderE=round(remainderE,2)  #rounds up the amount left to 2 decimal points
print("quarter: {}".format(E))  #prints the no.of bills to give



#gives no.of $0.10coins we have to give
remainderF=remainderE%0.10      #gives the amount left
F=remainderE//0.10              #gives the no.of bills to give
remainderF=round(remainderF,2)  #rounds up the amount left to 2 decimal points
print("dime: {}".format(F))



#gives no.of $0.05coins we have to give
remainderG=remainderF%0.05      #gives the amount left
G=remainderF//0.05              #gives the no.of bills to give
remainderG=round(remainderG,2)  #rounds up the amount left to 2 decimal points
print("nickel: {}".format(G))   #prints the no.of bills to give



#gives no.of $0.01oins we have to give
remainderH=remainderG%0.01      #gives the amount left
H=remainderG//0.01              #gives the no.of bills to give
remainderH=round(remainderH,2)  #rounds up the amount left to 2 decimal points
print("penny: {}".format(H))    #prints the no.of bills to give




 
