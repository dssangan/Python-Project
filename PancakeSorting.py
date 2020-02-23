# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def reverseArray(array, index):
    count=0
    while count < index:
        temp = array[index]
        array[index] = array[count]
        array[count] = temp
        count += 1
        index -= 1

#gets the index of the max value in the array
def getIndex(array, size):
    counter = 0
    actualSize = size
    while actualSize>1:
        index=0
        print("\n Before getting index \n")
        printArray(array, size)
        for i in range(actualSize):
            if array[i]>array[index]:
                index = i
                print("index is" + str(index))
        print("\n after getting index")        
        printArray(array,size)      
        if index != actualSize-1:
            counter += 1
            print("\n before reversing first time")
            printArray(array,size)   
            reverseArray(array, index)
            print("\n after reversing first time & before reversing second time")
            printArray(array,size)
            reverseArray(array, actualSize-1)
            print("\n after reversing second time")
            printArray(array,size)
            
        actualSize -= 1 

    return array, counter

def printArray(arrayPrint, sizeArray):
    for i in range(sizeArray):
        print(str(arrayPrint[i]), end=", ")
 
def main():
    array = [1,3,5,7,9,2,4,6]
    sizeArray = len(array)
    sortedArray, counter = getIndex(array, sizeArray)
    print("Reversing happended " + str(counter) + " times, with 0th index as starter")
    printArray(sortedArray, sizeArray)
    
main()