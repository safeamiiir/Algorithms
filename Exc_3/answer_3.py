numOfCases, numOfKeys, numOfBalls = [int(tower) for tower in input().split()]
keysPosition = [int(tower) for tower in input().split()]
ballsPosition = [int(tower) for tower in input().split()]
pointedArr = []
maxDistance = 0

# Initialize pointedArr with -1
for index in range(numOfCases):
    pointedArr.append(-1)

'''
-1 =>  Empty
 0 =>  Ball
 1 =>  Key
 2 =>  Ball and Key
'''
bothFlag = '_'
for index in range(numOfCases): # Change pointedArr which should be 0
    if(len(ballsPosition) and index == ballsPosition[0] - 1):
        bothFlag = index
        ballsPosition.pop(0) # Pop element
        pointedArr[index] = 0
    if(len(keysPosition) and index == keysPosition[0] - 1):
        if(bothFlag == index):
            bothFlag = '_'
            pointedArr[index] = 2
        else:   
            pointedArr[index] = 1
        keysPosition.pop(0) # Pop element

# Find range of keys
# if start == end  ==> it has only one key!
startOfKeys = -1
endOfKeys = -1
endFlag = False
for index in range(numOfCases):
    #set index of start of the key
    if( (pointedArr[index] == 1 or pointedArr[index] == 2) and not endFlag):
        startOfKeys = index
        endFlag = True
    #set index of end of the key
    if( (pointedArr[index] == 1 or pointedArr[index] == 2) and endFlag):
        endOfKeys = index

#Calculates max distance
tempIndex = startOfKeys
for index in range(startOfKeys + 1, endOfKeys + 1):
    newDistance = index - tempIndex
    if(pointedArr[index] == 0 or pointedArr[index] == 1 or pointedArr[index] == 2):
        if(newDistance > maxDistance):
            maxDistance = newDistance
        tempIndex = index

#Find from start to first element
firstOnes = 0
for index in range(startOfKeys):
    if(pointedArr[index] == 0 or pointedArr[index] == 2):
        firstOnes = startOfKeys - index
        break

#Find from start to first element
lastOnes = 0
for index in range(endOfKeys + 1, numOfCases):
    if(pointedArr[index] == 0 or pointedArr[index] == 2):
        lastOnes = index - endOfKeys

####### ANSWERS #######
#handle if we only have one key or not!
tempStartIndex = 0
tempEndIndex = 0
endIndexFlag = False
if (startOfKeys == endOfKeys):
    for index in range(numOfCases):
        if((pointedArr[index] == 0 or pointedArr[index] == 1 or pointedArr[index] == 2) and not endIndexFlag):
            tempStartIndex = index
            endIndexFlag = True
        if((pointedArr[index] == 0 or pointedArr[index] == 1 or pointedArr[index] == 2) and endIndexFlag):
            tempEndIndex = index
    print(tempEndIndex - tempStartIndex + 1)
else:
    if(pointedArr[startOfKeys] == 2 and pointedArr[endOfKeys] == 2):
        print((endOfKeys - startOfKeys + 1) - maxDistance + firstOnes + lastOnes + 1)
    else:
        print((endOfKeys - startOfKeys + 1) - maxDistance + firstOnes + lastOnes)