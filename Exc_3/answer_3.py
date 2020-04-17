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

#handle if we only have one key or not!
ansForOne = 0
if (startOfKeys == endOfKeys):
    for index in range(numOfCases):
        if(pointedArr[index] == 0 or pointedArr[index] == 2):
            if(abs(index - startOfKeys) + 1 > ansForOne):
                ansForOne = abs(index - startOfKeys) + 1
    print('answer: IT IS WITH ONE KEY CASE')
    print('ansForOne:', ansForOne)                
else:
    if(pointedArr[startOfKeys] == 2 and pointedArr[endOfKeys] == 2):
        print('answer: ',  (endOfKeys - startOfKeys + 1) - maxDistance + firstOnes + lastOnes + 1)
    else:
        print('answer: ',  (endOfKeys - startOfKeys + 1) - maxDistance + firstOnes + lastOnes)        