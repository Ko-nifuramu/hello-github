#This algorithm is not correct. It outpts wrong answers.

import math

def eggDrop(n, k):
    egg = n
    numberOfFloor = k

    if egg == 1:
        print("patern1")
        return numberOfFloor
    elif 2**(egg + 2) > numberOfFloor:
        print("patern2")
        return   int(math.log2(numberOfFloor)) + 1
    
    print("patern3")#The algorithm of patern3 may be incorrect.

    maxColumn = getMaxColumn(numberOfFloor)
    print(maxColumn)
    A = [[0 for i in range(maxColumn)] for j in range(egg-1)]
    
    nNumber = 0
    for column in range(maxColumn):
        nNumber += 1
        A[0][column] = nNumber*(nNumber+1)/2

    for row in range(egg-1):
        A[row][0] = 1    

    for i in range(1, egg-1):
        sumOfRow = 1
        for column in range(1, maxColumn):
            sumOfRow += A[i-1][column]
            
            A[i][column] = sumOfRow
            if sumOfRow > k:
                break
    print(A)
            
    for column in range(maxColumn): 
        if A[egg-2][column] > numberOfFloor:
            if egg == 2:
                return column + 1
            return column + egg -1

    print(A)      


def getMaxColumn(numberOfFloor):
    print(numberOfFloor)
    n = 1
    sumOfNumber = n*(n+1)/2
    
    while sumOfNumber < numberOfFloor:
        n += 1
        sumOfNumber = n*(n+1)/2
        
    return n

numEgg = input("Please type the number of egg : ")
numFloor = input("Please type the number of floors : ")
print(eggDrop(int(numEgg), int(numFloor)))

