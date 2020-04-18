numOfCases, numOfKeys, numOfBalls = [int(tower) for tower in input().split()]
keysPosition = [int(tower) for tower in input().split()]
ballsPosition = [int(tower) for tower in input().split()]
print('numOfCases: ', numOfCases)
print('numOfKeys: ', numOfKeys)
print('numOfBalls: ', numOfBalls)
print('keysPosition: ', keysPosition)
print('ballsPosition: ', ballsPosition)
print('-_-_-_-_-_-_-_-_-_-_-')
pointedArr = []

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
print('pointedArr:', pointedArr)

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
maxDistance = 0
maxBallBallDistance = 0
maxKeyKeyDistance = 0
totalDistance = 0
startKeyFlag = False
for index in range(startOfKeys + 1, endOfKeys + 1):
    newDistance = index - tempIndex
    if( (pointedArr[tempIndex] == 0 or pointedArr[tempIndex] == 2) and (pointedArr[index] == 0 or pointedArr[index] == 2) ): # ball - ball
        print('in ball - ball')
        print('tempIndex: ', tempIndex + 1)
        print('index: ', index + 1)
        if(newDistance - 1 > maxBallBallDistance):
            maxBallBallDistance = newDistance
            totalDistance += maxBallBallDistance
    if( (pointedArr[tempIndex] == 1 or pointedArr[tempIndex] == 2) and (pointedArr[index] == 0 or pointedArr[index] == 2) and pointedArr[startOfKeys] != 2 ): # key - ball
        print('in key - ball')
        print('tempIndex: ', tempIndex + 1)
        print('index: ', index + 1)
        startKeyFlag = True
        if(newDistance > maxDistance):
            maxDistance = newDistance
    if( (pointedArr[tempIndex] == 0 or pointedArr[tempIndex] == 2) and (pointedArr[index] == 1 or pointedArr[index] == 2) and pointedArr[endOfKeys] != 2 and startKeyFlag): # ball - key
        print('in ball - key')
        print('tempIndex: ', tempIndex + 1)
        print('index: ', index + 1)
        if(newDistance > maxDistance):
            maxDistance = newDistance
        totalDistance += maxDistance
        maxDistance = 0
    if( (pointedArr[tempIndex] == 1 or pointedArr[tempIndex] == 2) and (pointedArr[index] == 1 or pointedArr[index] == 2) ): # key - key
        print('in key - key')
        print('tempIndex: ', tempIndex + 1)
        print('index: ', index + 1)
        if(newDistance > maxKeyKeyDistance):
            maxKeyKeyDistance = newDistance
            totalDistance += maxKeyKeyDistance
    if( (pointedArr[tempIndex] == 0 or pointedArr[tempIndex] == 1 or pointedArr[tempIndex] == 2) and (pointedArr[index] == 0 or pointedArr[index] == 1 or pointedArr[index] == 2)):
        tempIndex = index # renew indexes
    maxBallBallDistance = 0
    maxKeyKeyDistance = 0
    print('-------------')
    print('totalDistance: ', totalDistance)
    print('-------------')

#Find from start to first element
firstOnes = 0
for index in range(startOfKeys):
    if(pointedArr[index] == 0 or pointedArr[index] == 2):
        firstOnes = startOfKeys - index
        break

print('-_-_-_-_-_-_-_-_-_-_-')
#Find from start to first element
lastOnes = 0
for index in range(endOfKeys + 1, numOfCases):
    print('index in endOfKeys: ', index)
    if(pointedArr[index] == 0 or pointedArr[index] == 2):
        lastOnes = index - endOfKeys
print('start balls range: ', firstOnes)
print('end balls range: ', lastOnes)
print('-_-_-_-_-_-_-_-_-_-_-')
print('startOfKeys: ', startOfKeys)
print('endOfKeys: ', endOfKeys)
print('maxDistance: ', maxDistance)

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
    print('tempStartIndex:', tempStartIndex)
    print('tempEndIndex:', tempEndIndex)
    print('answer1: ', tempEndIndex - tempStartIndex + 1)
else:
    if(lastOnes or firstOnes):
        print('answer2: ',  (endOfKeys - startOfKeys + 1) - totalDistance + firstOnes + lastOnes + 1)
    else:
        print('answer2: ',  (endOfKeys - startOfKeys + 1) - totalDistance + firstOnes + lastOnes)