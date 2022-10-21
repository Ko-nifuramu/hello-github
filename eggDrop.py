import math

#This algorithm is not correct. It outputs wrong answers. 
def eggDrop(n,k):
    if n == 1:
        return k

    numberOfSearchFloor = k
    egg = n

    while egg > 2:
        egg -= 1
        numberOfSearchFloor = numberOfSearchFloor // 2 

    #print("n-2 : {}".format(n-2))
    #print("numberOfSearchFloor : {}".format(numberOfSearchFloor))

    return (n-2)+twoEggDrop(numberOfSearchFloor)    



def twoEggDrop(numberOfFloor):
    n = 1
    sumOfnum = n*(n+1)/2

    while sumOfnum < numberOfFloor:
        n += 1
        sumOfnum = n*(n+1)/2

    #print(n)    
    return n
